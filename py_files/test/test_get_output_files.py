import json
from os.path import basename
from pathlib import Path

import pytest

from ..src.get_output_files import get_output_files
from .utility.fake_file_creator import fake_file_creator
from .utility.output_getter import output_getter


def test_same_flat(fs, random_files):
    """
    Test with the "same" files options with a flat directory of mermaid files, i.e.
    where all outputted filepaths are placed adjacent to their corresponding mermaid files.
    """
    input_files = [
        "diagram.mermaid",
        "diagram1.mermaid",
        "diagram2.mermaid",
        "diagram3.mermaid",
    ]
    output_files = []

    for file in input_files:
        output_files.append(Path(file).with_suffix(".png").as_posix())

    fake_file_creator(fs, input_files + random_files)
    fs.create_file("output.txt")

    get_output_files(input_files, "same", "png", "output.txt")

    parsed_output = output_getter("output.txt")
    assert "output_files" in parsed_output.keys()
    assert json.loads(parsed_output["output_files"]) == output_files


def test_same_deep(fs, random_files):
    """
    Test with the "all" files options with a deep directory of mermaid files, i.e.
    where all outputted filepaths are placed adject to input filepaths
    """
    input_files = [
        "diagram.mmd",
        "diagram1.mmd",
        "dir1/diagram.mmd",
        "dir1/diagram1.mmd",
    ]
    output_files = []

    for file in input_files:
        output_files.append(Path(file).with_suffix(".svg").as_posix())

    # output files are added here to test that they shouldn't make a difference
    # i.e. we're outputting filepaths without checking for anything
    fake_file_creator(fs, input_files + random_files + output_files)
    fs.create_file("output.txt")

    get_output_files(input_files, "same", "svg", "output.txt")

    parsed_output = output_getter("output.txt")
    assert "output_files" in parsed_output.keys()
    assert json.loads(parsed_output["output_files"]) == output_files


def test_dir_flat(fs, random_files):
    """
    Test with the "dir" files options with a flat directory of mermaid files, i.e.
    we specify that output files must exist in some specified dir
    """

    input_files = [
        "diagram.mermaid",
        "diagram1.mermaid",
        "diagram2.mermaid",
        "diagram3.mermaid",
    ]

    fake_file_creator(fs, input_files + random_files)
    fs.create_file("output.txt")

    output_files = []
    for file in input_files:
        output_files.append((Path("dir1") / Path(file)).with_suffix(".svg").as_posix())

    get_output_files(input_files, "dir1", "svg", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "output_files" in parsed_output.keys()
    assert json.loads(parsed_output["output_files"]) == output_files


def test_dir_deep_exception(fs, random_files):
    """
    Test with the "dir" files options with a deep directory of mermaid files, i.e.
    we specify that output files must exist in some specified dir.

    this test case should generate an exception b/c 2 mermaid files in diff directories
    have the same basename. This is not allowed b/c they will overwrite each other in the
    outputted directory.
    """

    input_files = [
        "diagram.mmd",
        "diagram1.mmd",
        "dir1/diagram.mmd",
        "dir1/diagram1.mmd",
    ]

    fake_file_creator(fs, input_files + random_files)
    fs.create_file("output.txt")

    with pytest.raises(FileExistsError):
        get_output_files(input_files, "dir1", "svg", "output.txt")


def test_dir_deep(fs, random_files):
    """
    Test with the "dir" files options with a flat directory of mermaid files, i.e.
    we specify that output files must exist in some specified dir
    """

    input_files = [
        "diagram.mmd",
        "diagram1.mmd",
        "dir1/diagram2.mmd",
        "dir1/diagram3.mmd",
    ]

    fake_file_creator(fs, input_files + random_files)
    fs.create_file("output.txt")

    output_files = []
    for file in input_files:
        output_files.append(
            (Path("dir1") / basename(Path(file))).with_suffix(".svg").as_posix()
        )

    get_output_files(input_files, "dir1", "svg", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "output_files" in parsed_output.keys()
    assert json.loads(parsed_output["output_files"]) == output_files
