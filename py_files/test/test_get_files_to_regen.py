import json
from pathlib import Path

from ..src.get_files_to_regen import get_files_to_regen
from .utility.fake_file_creator import fake_file_creator
from .utility.output_getter import output_getter

# test plan:
# test when output files exist / dont exist (existence)
# if they exist, they should not be regen
# if they dont exist, regen
# test when output files exist, whether theyy're newer/older than input file (date)
# regen if older
# do not regen if newer


def test_existence_no_output_file(fs, flat_mermaid_files, random_files):
    """
    test when output files do not exists, all input mmd files should be regen
    """
    input_files = flat_mermaid_files
    output_files = []
    for file in input_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())
    fake_file_creator(fs, input_files + random_files)
    fs.create_file("output.txt")

    get_files_to_regen(input_files, output_files, "output.txt")

    parsed_output = output_getter("output.txt")
    assert json.loads(parsed_output["input_files_to_regen"]) == input_files
    assert json.loads(parsed_output["output_files_to_regen"]) == output_files


def test__existence_some_output_file(fs, flat_mermaid_files, random_files):
    """
    test when some output files exist, some input mmd files should be regen
    """
    input_files = flat_mermaid_files
    output_files = []
    for file in input_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())
    fake_file_creator(fs, input_files + random_files + output_files[:2])
    fs.create_file("output.txt")

    get_files_to_regen(input_files, output_files, "output.txt")

    parsed_output = output_getter("output.txt")
    assert json.loads(parsed_output["input_files_to_regen"]) == input_files[2:]
    assert json.loads(parsed_output["output_files_to_regen"]) == output_files[2:]


def test_existence_all_output_file(fs, flat_mermaid_files, random_files):
    """
    test when all output files exist, no input file should be regen
    """
    input_files = flat_mermaid_files
    output_files = []
    for file in input_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())
    fake_file_creator(fs, input_files + random_files + output_files)
    fs.create_file("output.txt")

    get_files_to_regen(input_files, output_files, "output.txt")

    parsed_output = output_getter("output.txt")
    assert json.loads(parsed_output["input_files_to_regen"]) == []
    assert json.loads(parsed_output["output_files_to_regen"]) == []


def test_date_some_output_file(fs, flat_mermaid_files, random_files):
    """
    test when some output files are older, they should be the only ones regen
    """
    input_files = flat_mermaid_files
    output_files = []
    for file in input_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())
    fake_file_creator(
        fs, output_files[:2] + input_files + random_files + output_files[2:]
    )
    fs.create_file("output.txt")

    get_files_to_regen(input_files, output_files, "output.txt")

    parsed_output = output_getter("output.txt")
    assert json.loads(parsed_output["input_files_to_regen"]) == input_files[:2]
    assert json.loads(parsed_output["output_files_to_regen"]) == output_files[:2]


def test_date_all_output_file(fs, flat_mermaid_files, random_files):
    """
    test when all output files are older, they should all be regen
    """
    input_files = flat_mermaid_files
    output_files = []
    for file in input_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())
    fake_file_creator(fs, output_files + input_files + random_files)
    fs.create_file("output.txt")

    get_files_to_regen(input_files, output_files, "output.txt")

    parsed_output = output_getter("output.txt")
    assert json.loads(parsed_output["input_files_to_regen"]) == input_files
    assert json.loads(parsed_output["output_files_to_regen"]) == output_files
