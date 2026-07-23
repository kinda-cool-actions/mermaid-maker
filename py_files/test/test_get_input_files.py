import pytest
from .. import get_input_files
import json
from .utility.output_getter import output_getter


def create_fake_files(fs, files_lst):
    for file in files_lst:
        fs.create_file(file)


@pytest.fixture
def random_files():
    return [
        "hi.png",
        "rainbow.pdf",
        "dir/beebop.txt",
        "dir/somefile.js",
        "dir/dir1/hi.py",
    ]


def test_all_flat_dir(fs, random_files):
    files = [
        "diagram.mermaid",
        "diagram1.mermaid",
        "diagram2.mermaid",
        "diagram3.mermaid",
    ]

    create_fake_files(fs, files + random_files)
    fs.create_file("output.txt")

    get_input_files.get_input_files("all", "mermaid", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_all_deep_dir(fs, random_files):
    files = ["diagram.mmd", "diagram1.mmd", "dir1/diagram.mmd", "dir1/diagram1.mmd"]
    create_fake_files(fs, files + random_files)
    fs.create_file("output.txt")

    get_input_files.get_input_files("all", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_dir_flat(fs, random_files):
    files = ["dir1/diagram.mmd", "dir1/diagram1.mmd"]
    create_fake_files(fs, files + random_files + ["diagram.mmd", "diagram1.mmd"])
    fs.create_file("output.txt")

    get_input_files.get_input_files("dir1", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_dir_deep(fs, random_files):
    files = ["dir1/diagram.mmd", "dir1/diagram1.mmd", "dir1/bingo/diagram3.mmd"]
    create_fake_files(
        fs, files + random_files + ["diagram.mmd", "diagram1.mmd", "dir2/hi.mmd"]
    )
    fs.create_file("output.txt")

    get_input_files.get_input_files("dir1", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files
