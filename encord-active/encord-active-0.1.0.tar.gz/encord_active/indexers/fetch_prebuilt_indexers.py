import os
import shutil
from pathlib import Path

import gdown

# Google Drive links for the projects will be added here
PREBUILT_PROJECTS = {
    "[open-source][validation]-coco-2017-dataset": "https://drive.google.com/file/d/1iWx_y0r9I9Aay-nCo0ZMob2bI176v95b/view?usp=sharing",
    "[open-source][test]-limuc-ulcerative-colitis-classification": "https://drive.google.com/file/d/1Bw3uBIxDqyOlt7hincYbFgusU9FVf-OT/view?usp=sharing",
    "[open-source]-covid-19-segmentations": "https://drive.google.com/file/d/1Alo-4cqeGd1gcwQRxr3axz_QL8au1mjo/view?usp=sharing",
    "[open-source][validation]-bdd-dataset": "https://drive.google.com/file/d/1mJisC2yLU_5lzrrZquIXe5KJ2txkgdXx/view?usp=sharing",
}


def fetch_index(project_n: str, out_dir: Path):
    """
    Prebuilt indexes for publicly available datasets can be downloaded via this script.
    As long as we keep using Google Drive, we should keep zipped file names same for each project.
    Otherwise, Google Drive may update the links, which makes the below links obsolete.
    """
    url = PREBUILT_PROJECTS[project_n]
    output_file_name = "index_output.zip"
    output_file_path = out_dir / output_file_name
    print(f"Output destination: {out_dir}")
    if not out_dir.is_dir():
        exit()

    gdown.download(url=url, output=output_file_path.as_posix(), quiet=False, fuzzy=True)
    print("Unpacking zip file. May take a bit.")
    shutil.unpack_archive(output_file_path, out_dir)
    os.remove(output_file_path)

    print("To view the data, run: \n" f"python scripts/visualise.py {out_dir}")
