import os
from pathlib import Path

import nbformat
from nbconvert import PythonExporter


def main(folder_path: Path, is_format: bool = True) -> None:
    # find all the `.ipynb` file path in given folder
    notebooks: list[Path] = find_ipynbs(folder_path)

    # make `.py` file path list from found `.ipynb` file path
    pys: list[Path] = make_py_path(notebooks)

    # convert to python file
    convert_ipynb(notebooks)

    # check and format `.py` file with `ruff`
    if is_format:
        format_by_ruff(pys)


def find_ipynbs(folder_path: Path) -> list[Path]:
    """for find all the `ipynb` in target Path"""
    notebooks = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipynb"):
                notebooks.append(os.path.join(root, file))
    return notebooks


def make_py_path(notebooks: list[Path]) -> list[Path]:
    """for making `.py` files'path for func format_by_black"""
    pys = []
    for notebook in notebooks:
        base_name = os.path.splitext(notebook)[0]
        py_file = base_name + ".py"
        pys.append(py_file)
    return pys


def convert_ipynb(notebooks: list[Path]):
    """for converting `.ipynb` to `.py` in the same path"""
    exporter = PythonExporter()
    for notebook in notebooks:
        base_name = os.path.splitext(notebook)[0]
        py_file = base_name + ".py"
        with open(notebook, "r", encoding="utf-8") as nb_file:
            nb = nbformat.read(nb_file, nbformat.NO_CONVERT)
            py_code, _ = exporter.from_notebook_node(nb)
            with open(py_file, "w", encoding="utf-8") as py_file:
                py_file.write(py_code)


def format_by_ruff(py_path: list[Path]):
    """for formatting `.py` file using `ruff`"""
    for py_file in py_path:
        os.system(f"ruff check --fix {py_file}")
        os.system(f"ruff format {py_file}")


if __name__ == "__main__":
    path = Path(input("Paste your path here: "))
    main(path)
