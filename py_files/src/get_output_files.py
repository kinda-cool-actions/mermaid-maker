import json
from os import environ
from os.path import basename
from pathlib import Path


def get_output_files(input_files, output_dir, output_file_extension, output_file):
    output_files = []

    if output_dir == "same":
        for file in input_files:
            output_files.append(
                Path(file).with_suffix(f".{output_file_extension}").as_posix()
            )
    else:
        for file in input_files:
            output_files.append(
                (Path(output_dir) / basename(file))
                .with_suffix(f".{output_file_extension}")
                .as_posix()
            )
        if len(output_files) != len(set(output_files)):
            raise FileExistsError(
                "If you are specifying an output directory, please ensure your input mermaid files have unique names."
            )

    with open(output_file, "a") as file:
        print(f"output_files={json.dumps(output_files)}", file=file)


if __name__ == "__main__":
    get_output_files(
        json.loads(environ["INPUT_FILES"]),
        environ["OUTPUT_DIR"],
        environ["OUTPUT_FILE_EXTENSION"],
        environ["GITHUB_OUTPUT"],
    )
