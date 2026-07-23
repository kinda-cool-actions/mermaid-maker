from glob import glob
from os import environ
import json


def get_input_files(input_dir, input_file_extension, output_file):

    if input_dir == "all":
        input_files_glob_pattern = f"**/*.{input_file_extension}"
    else:
        input_files_glob_pattern = f"{input_dir}/**/*.{input_file_extension}"

    input_files = []
    for file in glob(input_files_glob_pattern, recursive=True):
        input_files.append(file)

    with open(output_file, "a") as file:
        print("input_files=" + json.dumps(input_files), file=file)


if __name__ == "__main__":
    get_input_files(
        environ["INPUT_DIR"], environ["INPUT_FILE_EXTENSION"], environ["GITHUB_OUTPUT"]
    )
