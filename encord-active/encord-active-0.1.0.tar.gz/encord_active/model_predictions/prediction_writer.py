import json
import logging
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import cv2
import numpy as np
import pandas as pd
import pycocotools.mask as mask_utils
import torch
from encord import Project
from torchvision.ops import box_iou
from tqdm import tqdm

from encord_active.common.prepare import prepare_data

logger = logging.getLogger(__name__)
BBOX_KEYS = {"x", "y", "w", "h"}
BASE_URL = "https://app.encord.com/label_editor/"


class PredictionType(Enum):
    FRAME = "frame"
    BBOX = "bounding_box"
    POLYGON = "polygon"


PREDICTION_CSV_COLUMNS = ["identifier", "url", "img_id", "class_id", "confidence", "x1", "y1", "x2", "y2", "rle", "iou"]
LABEL_CSV_COLUMNS = ["identifier", "url", "img_id", "class_id", "object_hash", "x1", "y1", "x2", "y2", "rle"]


class LKey(Enum):
    ID = 0
    URL = 1
    IMG_ID = 2
    CLASS = 3
    OBJ_ID = 4
    X1 = 5
    Y1 = 6
    X2 = 7
    Y2 = 8
    RLE = 9


class PKey(Enum):
    ID = 0
    URL = 1
    IMG_ID = 2
    CLASS = 3
    CONF = 4
    X1 = 5
    Y1 = 6
    X2 = 7
    Y2 = 8
    RLE = 9


def polyobj_to_nparray(o: dict, width: int, height: int) -> np.ndarray:
    return np.array(
        [(o["polygon"][str(i)]["x"] * width, o["polygon"][str(i)]["y"] * height) for i in range(len(o["polygon"]))]
    )


# def rle_encode(mask_image):
#     """
#     Compute run length encoding of mask.
#     """
#     pixels = mask_image.flatten()
#     pixels[0] = 0
#     pixels[-1] = 0
#     runs = np.where(pixels[1:] != pixels[:-1])[0] + 2
#     runs[1::2] = runs[1::2] - runs[:-1:2]
#     return runs.reshape(-1, 2)
#


def points_to_mask(points: np.ndarray, width: int, height: int):
    mask = np.zeros((height, width), dtype=np.uint8)
    mask = cv2.fillPoly(mask, [points.astype(int)], 1)
    return mask


def get_img_ious(detections: list, ground_truth_img: list):
    # Note: we assume that all labels and predictions are of same type, i.e., either segmentations or bboxes.
    if ground_truth_img[0][1][LKey.RLE.value] is not None:  # Segmentation
        det_coco_format = [i[1][PKey.RLE.value] for i in detections]
        gt_coco_format = [i[1][LKey.RLE.value] for i in ground_truth_img]

        return torch.tensor(mask_utils.iou(det_coco_format, gt_coco_format, [False for _ in ground_truth_img]))
    else:
        _pred_boxes = torch.tensor([d[1][PKey.X1.value : PKey.Y2.value + 1] for d in detections])  # type: ignore
        _label_boxes = torch.tensor([l[LKey.X1.value : LKey.Y2.value + 1] for _, l in ground_truth_img])
        return box_iou(_pred_boxes, _label_boxes)


def precompute_MAP_features(
    pred_boxes: List[List[Any]],
    true_boxes: List[List[Any]],
) -> Tuple[torch.Tensor, Dict[int, Dict[int, List[Dict[str, Any]]]]]:
    """
    Calculates mean average precision for given iou threshold and rec_thresholds.
    Parameters:
        pred_boxes: list of lists containing all bboxes with each bboxes
            specified as::

                [
                    train_idx (int),
                    class_prediction(int),
                    prob_score (float),
                    x1 (float[0, img_width]),
                    y1 (float[0, img_height]),
                    x2 (float[0, img_width]),
                    y2 (float[0, img_height]),
                ]

        true_boxes: Similar as pred_boxes except all the correct ones.
            I.e., the prob_score doesn't matter and will be ignored.

    Returns:
        ious: used as input for the next call to the function.
        ground_truths_matched: used as input for the next call to the function.
    """
    # Do all the heavy lifting of computing ious and matching predictions to objects.
    ground_truths: Dict[Tuple[int, int], List[Any]] = {}
    predictions: Dict[Tuple[int, int], Tuple[int, List[Any]]] = {}
    pred_boxes.sort(key=lambda x: x[PKey.CONF.value], reverse=True)

    for lidx, true_box in enumerate(true_boxes):
        ground_truths.setdefault((true_box[LKey.IMG_ID.value], true_box[LKey.CLASS.value]), []).append((lidx, true_box))

    ground_truths_matched: Dict[int, Dict[int, List[Dict[str, Any]]]] = {}
    for (img_id, class_idx), img_cls_labels in ground_truths.items():
        ground_truths_matched.setdefault(class_idx, {})[img_id] = [
            {"lidx": lidx, "pidxs": []} for lidx, _ in img_cls_labels
        ]

    for pidx, pred_box in enumerate(pred_boxes):
        predictions.setdefault((pred_box[PKey.IMG_ID.value], pred_box[PKey.CLASS.value]), []).append((pidx, pred_box))  # type: ignore

    ious = torch.zeros(len(pred_boxes), dtype=float)  # type: ignore
    for (img_idx, pred_cls), detections in tqdm(predictions.items(), desc="Matching predictions to labels"):
        ground_truth_img = ground_truths.get((img_idx, pred_cls))
        label_matches = ground_truths_matched.get(pred_cls, {}).get(img_idx, [])

        if not ground_truth_img:
            continue

        img_ious = get_img_ious(detections, ground_truth_img)
        best_gt_idxs = torch.argmax(img_ious, dim=1, keepdim=False)
        best_ious = torch.amax(img_ious, dim=1, keepdim=False)

        for i, (best_gt_idx, best_iou) in enumerate(zip(best_gt_idxs, best_ious)):
            if best_iou > 0:
                pidx = detections[i][0]  # type: ignore
                label_matches[best_gt_idx]["pidxs"].append(pidx)
                ious[pidx] = best_iou

    return ious, ground_truths_matched


class PredictionWriter:
    def __init__(
        self,
        cache_dir: Path,
        project: Project,
        prefix: str = "",
        custom_object_map: Optional[Dict[str, int]] = None,
        **kwargs,
    ):
        self.cache_dir = (cache_dir / "predictions").expanduser().absolute()
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        file_name = "predictions.csv"
        if prefix:
            file_name = f"{prefix}_{file_name}"
        self.file_path = self.cache_dir / file_name
        logger.info(f"Storing predictions at {self.file_path}")

        self.predictions_file = None
        self.object_predictions: List[List[Any]] = []  # [[key, img_id, class_id, confidence, x1, y1, x2, y2], ...]

        self.project = project
        self.object_lookup = {o["featureNodeHash"]: o for o in self.project.ontology["objects"]}

        logger.info("Fetching project label rows to be able to match predictions.")
        self.label_rows, _ = prepare_data(project, cache_dir, use_images=False, **kwargs)
        self.label_row_meta = {lr["label_hash"]: lr for lr in self.project.label_rows if lr["label_hash"] is not None}

        self.__prepare_lr_lookup()
        self.__prepare_image_id_lookup()
        self.__prepare_class_id_lookups(custom_object_map)
        self.__prepare_label_list()

    def __prepare_lr_lookup(self):
        logger.debug("Preparing label row lookup")
        # Top level data hashes
        self.lr_lookup: Dict[str, str] = {d["data_hash"]: d["label_hash"] for d in self.project.label_rows}
        # Nested data hashes for every data unit in the project
        for lr in self.label_rows.values():
            self.lr_lookup.update({du_hash: lr["label_hash"] for du_hash in lr["data_units"]})

    def __prepare_image_id_lookup(self):
        logger.debug("Preparing image id lookup")
        self.image_id_lookup: Dict[Tuple[str, Optional[int]], int] = {}  # d[(du_hash, frame)]: int
        for lr in self.label_rows.values():
            data_type = lr["data_type"]
            for du in lr["data_units"].values():
                if "im" in data_type:  # img_group or image
                    frame = int(du["data_sequence"])
                    self.image_id_lookup[(du["data_hash"], frame)] = len(self.image_id_lookup)
                else:  # Video
                    for fr in du["labels"]:
                        frame = int(fr)
                        self.image_id_lookup[(du["data_hash"], frame)] = len(self.image_id_lookup)

    def __prepare_class_id_lookups(self, custom_map: Optional[Dict[str, int]]):
        logger.debug("Preparing class id lookup")
        self.custom_map = False
        if custom_map:
            feature_hashes = {o["featureNodeHash"] for o in self.project.ontology["objects"]}
            custom_hashes = set(custom_map.keys())
            if not all([c in feature_hashes for c in custom_hashes]):
                raise ValueError("custom map keys should correspond to `featureNodeHashes` from the project ontology.")

            self.object_class_id_lookup = custom_map
            self.custom_map = True
        else:
            self.object_class_id_lookup = {}
            for obj in self.project.ontology["objects"]:
                self.object_class_id_lookup[obj["featureNodeHash"]] = len(self.object_class_id_lookup)

        self.classification_class_id_lookup: Dict[str, int] = {}
        for obj in self.project.ontology["classifications"]:
            self.classification_class_id_lookup[obj["featureNodeHash"]] = len(self.classification_class_id_lookup)

    def __prepare_label_list(self):
        logger.debug("Preparing label list")
        self.object_labels: List[List[Any]] = []

        def append_object_label(du_hash: str, frame: int, o: dict, width: int, height: int):
            class_id = self.get_class_id(o)
            if class_id is None:  # Ignore unwanted classes (defined by what is in `self.object_class_id_lookup`)
                return

            label_hash = self.lr_lookup[du_hash]
            row = [
                f"{label_hash}_{du_hash}_{frame:05d}_{o['objectHash']}",
                f"{BASE_URL}{self.label_row_meta[label_hash]['data_hash']}&{self.project.project_hash}/{frame}",
                self.get_image_id(du_hash, frame),  # Image id
                class_id,  # Class id
                o["objectHash"],  # Object hash
                None,  # bbox.x1
                None,  # bbox.y1
                None,  # bbox.x2
                None,  # bbox.y2
                None,  # RLE encoding of mask
            ]

            if o["shape"] == "bounding_box":
                x, y, w, h = [o["boundingBox"][k] for k in ["x", "y", "w", "h"]]
                row[LKey.X1.value] = round(x * width, 2)  # bbox.x1
                row[LKey.Y1.value] = round(y * height, 2)  # bbox.y1
                row[LKey.X2.value] = round((x + w) * width, 2)  # bbox.x2
                row[LKey.Y2.value] = round((y + h) * height, 2)  # bbox.y2
            elif o["shape"] == "polygon":
                points = polyobj_to_nparray(o, width=width, height=height)
                mask = points_to_mask(points, width=width, height=height)
                x1, y1 = points.min(axis=0)
                x2, y2 = points.max(axis=0)
                row[LKey.X1.value] = x1  # bbox.x1
                row[LKey.Y1.value] = y1  # bbox.y1
                row[LKey.X2.value] = x2  # bbox.x2
                row[LKey.Y2.value] = y2  # bbox.y2
                row[LKey.RLE.value] = mask_utils.encode(np.asfortranarray(mask))
            else:
                # Only supporting polygons and bounding boxes.
                return
            self.object_labels.append(row)

        for label_hash, lr in tqdm(self.label_rows.items(), desc="Preparing labels"):
            data_type = lr["data_type"]
            for du_hash, du in lr["data_units"].items():
                height = int(du["height"])
                width = int(du["width"])

                if "im" in data_type:  # img_group or image
                    frame = int(du["data_sequence"])
                    for obj in du["labels"]["objects"]:
                        append_object_label(du_hash, frame, obj, width, height)
                else:  # Video
                    for fr, labels in du["labels"].items():
                        frame = int(fr)
                        for obj in labels["objects"]:
                            append_object_label(du_hash, frame, obj, width, height)

    def get_image_id(self, data_hash: str, frame: Optional[int]):
        return self.image_id_lookup.setdefault((data_hash, frame), len(self.image_id_lookup))

    def get_class_id(self, obj_dict):
        fh = obj_dict["featureHash"]
        if "objectHash" in obj_dict and fh in self.object_class_id_lookup:
            return self.object_class_id_lookup[fh]
        elif "classificationHash" in obj_dict and fh in self.classification_class_id_lookup:
            return self.classification_class_id_lookup[fh]
        return None

    def __enter__(self):
        self.predictions_file = self.file_path.open("w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Do the matching computations
        ious, ground_truths_matched = precompute_MAP_features(self.object_predictions, self.object_labels)

        # 0. The predictions
        logger.info("Saving predictions")
        pred_df = pd.DataFrame(self.object_predictions, columns=PREDICTION_CSV_COLUMNS[:-1])
        pred_df["iou"] = ious
        pred_df.to_csv(self.file_path)

        # 1. The labels
        logger.info("Saving labels")
        df = pd.DataFrame(self.object_labels, columns=LABEL_CSV_COLUMNS)
        df["rle"] = df["rle"].map(
            lambda x: " ".join(x.reshape(-1).astype(str).tolist()) if isinstance(x, np.ndarray) else x
        )
        df.to_csv(self.file_path.with_name("labels.csv"))

        # 2. The GT matches
        logger.info("Saving GTs matched")
        with (self.cache_dir / "ground_truths_matched.json").open("w") as f:
            json.dump(ground_truths_matched, f)

        # 3. The class idx map
        logger.info("Saving class index")
        class_index = {}
        for k, v in self.object_class_id_lookup.items():
            if k[0] == "_" or v in class_index:
                continue

            class_index[v] = {
                "featureHash": k,
                "name": self.object_lookup[k]["name"],
                "color": self.object_lookup[k]["color"],
            }

        with (self.cache_dir / "class_idx.json").open("w") as f:
            json.dump(class_index, f)

    @staticmethod
    def __check_bbox(bbox):
        bbox_keys = set(bbox.keys())
        if not len(bbox_keys.intersection(BBOX_KEYS)) == 4:
            raise ValueError(f"Bbox dict keys were {bbox_keys} but should be {BBOX_KEYS}")
        if not all([isinstance(v, (int, float)) for v in bbox.values()]):
            raise ValueError("Bbox coordinates should be floats")

    def add_prediction(
        self,
        data_hash: str,
        class_uid: str,
        confidence_score: float,
        bbox: Optional[Dict[str, Union[float, int]]] = None,
        polygon: Optional[Union[np.ndarray, List[Tuple[int, int]]]] = None,
        frame: Optional[int] = None,
    ):
        mask = None
        label_hash = self.lr_lookup.get(data_hash, "unmatched")
        du = self.label_rows[label_hash]["data_units"][data_hash]
        if du is None:
            logger.warning(f"Couldn't match data hash `{data_hash}` to any label row")
            return

        ptype: PredictionType
        if bbox is None and polygon is None:
            raise NotImplementedError("Frame level classifications are not supported at the moment.")
            # ptype = PredictionType.FRAME
        elif bbox is None and isinstance(polygon, (np.ndarray, list)):
            ptype = PredictionType.POLYGON
            if isinstance(polygon, list):
                polygon = np.array(polygon)
            if polygon.ndim != 2:
                raise ValueError("Polygon argument should have just 2 dimensions: [h, w] or [N, 2]")

            if polygon.shape[1] != 2:  # Polygon is mask
                mask = polygon
                x1, y1, w, h = cv2.boundingRect(polygon)
            else:  # Polygon is points
                # Read image size from label row
                width = int(du["width"])
                height = int(du["height"])
                mask = points_to_mask(polygon, width=width, height=height)
                x1, y1, w, h = cv2.boundingRect(polygon.reshape(-1, 1, 2).astype(int))
            x2, y2 = x1 + w, y1 + h
            points = [x1, y1, x2, y2]
            mask = mask_utils.encode(np.asfortranarray(mask))

        elif isinstance(bbox, dict) and polygon is None:
            ptype = PredictionType.BBOX
            self.__check_bbox(bbox)
            points = list(map(float, [bbox["x"], bbox["y"], bbox["x"] + bbox["w"], bbox["y"] + bbox["h"]]))
        else:
            raise ValueError(
                "Something seems wrong. Did you use the wrong types or did you parse both a bbox and polygon?"
            )

        # === Write key similar to the index writer (though object_hash will not be accessible here) === #
        label_hash = self.lr_lookup.get(data_hash, "unmatched")
        key = f"{label_hash}_{data_hash}"

        _frame = -1
        if frame is None:  # Try to infer frame number from data hash.
            if label_hash != "unmatched":
                label_row = self.label_rows[label_hash]
                data_unit = label_row["data_units"][data_hash]

                if "data_sequence" in data_unit:
                    _frame = int(data_unit["data_sequence"])
        if _frame != -1:
            key += f"_{_frame:05d}"

        class_id = self.object_class_id_lookup.get(class_uid)
        if class_id is None:
            raise ValueError(
                f"`class_uid` didn't match any key in the "
                f"{'`custom_object_map`' if self.custom_map else 'project ontology'}.\n"
                f"Options are: [{', '.join(self.object_class_id_lookup.keys())}]"
            )

        ontology_object = self.object_lookup[class_uid]
        if ontology_object["shape"] != ptype.value:
            raise ValueError(
                f"You've passed a {ptype.value} but the provided class id is of type " f"{ontology_object['shape']}"
            )

        image_id = self.get_image_id(data_hash, _frame)
        url = f"{BASE_URL}{self.label_row_meta[self.lr_lookup[data_hash]]['data_hash']}&{self.project.project_hash}/{_frame}"
        self.object_predictions.append([key, url, image_id, class_id, confidence_score] + points + [mask])
