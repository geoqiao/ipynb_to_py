import os

import nbformat


def main():
    """
    convert your `.ipynb` file to `.py` file
    Prerequired:
        1. Find you `.ipynb` files's Folder Path
        2. Run this script and input the Folder Path you found
        3. Better put all the `.ipynb` files into one folder(not mandatory)
    """
    folder_path = input("Folder_Path you want to convert: ")
    folder_path_output = input("Folder_Path you want to save: ")

    if folder_path == "":
        exit("Invalid path")
    if folder_path_output == "":
        folder_path_output = folder_path

    ipynb_files = [file for file in os.listdir(folder_path) if file.endswith(".ipynb")]

    for ipynb_file in ipynb_files:
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, ipynb_file)

        # 读取.ipynb文件
        with open(file_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        # 构建.py文件名
        py_file = os.path.splitext(ipynb_file)[0] + ".py"

        # 构建.py文件路径
        py_file_path = os.path.join(folder_path_output, py_file)

        # 将.ipynb文件转换为.py文件
        with open(py_file_path, "w", encoding="utf-8") as f:
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    source = cell.source
                    f.write(source)
                    f.write("\n")

    print("successfully converted")


if __name__ == "__main__":
    main()
