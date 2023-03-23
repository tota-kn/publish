import glob
import os
import re
import shutil

INPUT_DIRECTORY = "/Users/yt/Dropbox/obsidian/publish/"
OUTPUT_DIRECTORY = os.path.dirname(__file__) + "/../docs/"


def read_file_text(file_path: str):
    text: str = ""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def write_text_file(output_path: str, text: str):
    dir_path = os.path.dirname(output_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def get_content(file_path: str, file_name: str):
    content = read_file_text(file_path)
    content = re.sub("# ", "## ", content)
    content = re.sub(r"(#{1}[^\t\n\r\f\v #]+)", r"`\1`", content)
    content = "\n".join(
        [
            f"# {os.path.splitext(file_name)[0]}",
            content,
        ]
    )
    return content


def main():
    shutil.rmtree(OUTPUT_DIRECTORY)
    shutil.copytree(INPUT_DIRECTORY, OUTPUT_DIRECTORY)

    path_list = glob.glob(f"{OUTPUT_DIRECTORY}**/*.md")

    for path in path_list:
        file_name = os.path.basename(path)
        print(f"writing {file_name} ...")
        write_text_file(path, get_content(path, file_name))


main()
