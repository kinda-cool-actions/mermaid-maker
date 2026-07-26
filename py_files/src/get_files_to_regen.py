import json
from os import environ
from os.path import getmtime
from pathlib import Path


def get_files_to_regen(input_files, output_files, output_file):
    input_files_to_regen = []
    output_files_to_regen = []

    for i in range(len(input_files)):
        output_file_exists = Path(output_files[i]).exists()

        # we want to skip generating mermaid diagrams when:
        # 1. output file exists, AND
        # 2. output file is newer or as new as the input file
        # this is the negation of that
        if not output_file_exists or (
            getmtime(input_files[i]) > getmtime(output_files[i])
        ):
            input_files_to_regen.append(input_files[i])
            output_files_to_regen.append(output_files[i])

    with open(output_file, "a") as file:
        print("input_files_to_regen=" + json.dumps(input_files_to_regen), file=file)
        print("output_files_to_regen=" + json.dumps(output_files_to_regen), file=file)


if __name__ == "__main__":
    get_files_to_regen(
        json.loads(environ["INPUT_FILES"]),
        json.loads(environ["OUTPUT_FILES"]),
        environ["GITHUB_OUTPUT"],
    )
