import json
from subprocess import run
from os import environ


def mermaid_gen(input_files_to_regen, output_files_to_regen, run_cmd):

    mermaid_env = [
        "env",
        "PUPPETEER_CACHE_DIR=mermaid-maker-chrome-browser",
        "aa-exec",
        "--profile=chrome",
    ]

    # generate mermaid diagram for each changed file
    for i in range(len(input_files_to_regen)):
        mermaid_cmd = [
            "mmdc",
            "-i",
            input_files_to_regen[i],
            "-o",
            output_files_to_regen[i],
            "-b",
            "transparent",
        ]

        run(
            mermaid_env + [run_cmd] + mermaid_cmd,
        )


if __name__ == "__main__":
    mermaid_gen(
        json.loads(environ["INPUT_FILES_TO_REGEN"]),
        json.loads(environ["OUTPUT_FILES_TO_REGEN"]),
        environ["RUN_CMD"],
    )
