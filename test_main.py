import os
from pathlib import Path


def find_ipynbs(folder_path: Path) -> list[Path]:
    """for find all the `ipynb` in target Path"""
    notebooks = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipynb"):
                notebooks.append(os.path.join(root, file))
    return notebooks


if __name__ == "__main__":
    p = "/Users/geoqiao/data_env/src/machine_learning"
    count = 0
    for root, dirs, files in os.walk(p):
        count += 1
        print(f"{count}: root:{root},dirs:{dirs},files:{files}")
        print("\n")
