from loguru import logger

from encord_active.common.indexer import AnnotationType, DataType, Indexer, IndexType
from encord_active.common.iterator import Iterator
from encord_active.common.utils import get_iou, get_polygon
from encord_active.common.writer import CSVIndexWriter

logger = logger.opt(colors=True)


class AnnotationDuplicates(Indexer):
    TITLE = "Annotation Duplicates"
    SHORT_DESCRIPTION = "Ranks annotations by how likely they are to represent the same object"
    LONG_DESCRIPTION = r"""Ranks annotations by how likely they are to represent the same object. 
> [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) 
is used to measure closeness of two annotations."""
    INDEX_TYPE = IndexType.GEOMETRIC
    DATA_TYPE = DataType.IMAGE
    ANNOTATION_TYPE = [
        AnnotationType.OBJECT.BOUNDING_BOX,
        AnnotationType.OBJECT.POLYGON,
    ]

    def __init__(self, threshold: float = 0.6):
        # todo expose additional parameters along with their meaning
        # threshold: used along with Jaccard similarity coefficient to calculate likelihood of duplicates in annotations
        super().__init__()
        self.threshold = threshold

    def test(self, iterator: Iterator, writer: CSVIndexWriter):
        valid_annotation_types = {annotation_type.value for annotation_type in self.ANNOTATION_TYPE}
        found_any = False

        for data_unit, _ in iterator.iterate(desc="Looking for duplicates"):
            objects = [obj for obj in data_unit["labels"]["objects"] if obj["shape"] in valid_annotation_types]
            polygons = [get_polygon(obj) for obj in objects]

            duplicated_annotations = set()
            for i, obj1 in enumerate(objects):
                score = 0.0
                match = None
                for j, obj2 in enumerate(objects):
                    if j == i or obj1["featureHash"] != obj2["featureHash"]:
                        continue
                    cur_score = get_iou(polygons[i], polygons[j])
                    if cur_score > score:
                        score = cur_score
                        match = obj2

                identifiers = [obj1]
                if match is None or score < self.threshold:
                    description = "Possible non duplicated object"
                elif (obj1["objectHash"], match["objectHash"]) in duplicated_annotations:
                    # avoid reporting twice same annotation pair (in case (obj2, obj1) was previously analysed)
                    continue
                else:
                    identifiers.append(match)
                    description = "Possible duplicates"
                    duplicated_annotations.add((match["objectHash"], obj1["objectHash"]))

                writer.write_score(objects=identifiers, score=score, description=description)
                found_any = True

        if not found_any:
            logger.info(
                f"<yellow>[Skipping]</yellow> No object labels of types {{{', '.join(valid_annotation_types)}}}."
            )
