from ..src import get_input_files
import json
from .utility.output_getter import output_getter
from .utility.fake_file_creator import fake_file_creator


def test_all_flat_dir(fs, random_files):
    """
    Test with the "all" files options with a flat directory of mermaid files, i.e.
    where all diagrams are in the containing directory
    """
    files = [
        "diagram.mermaid",
        "diagram1.mermaid",
        "diagram2.mermaid",
        "diagram3.mermaid",
    ]

    fake_file_creator(fs, files + random_files)
    fs.create_file("output.txt")

    get_input_files.get_input_files("all", "mermaid", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_all_deep_dir(fs, random_files):
    """
    Test with the "all" files options with a deep directory of mermaid files, i.e.
    where diagrams are spread out across current directory and subdirectories
    """

    files = ["diagram.mmd", "diagram1.mmd", "dir1/diagram.mmd", "dir1/diagram1.mmd"]
    fake_file_creator(fs, files + random_files)
    fs.create_file("output.txt")

    get_input_files.get_input_files("all", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_dir_flat(fs, random_files):
    """
    Test with the "dir" files options with a flat directory of mermaid files.
    """

    files = ["dir1/diagram.mmd", "dir1/diagram1.mmd"]
    fake_file_creator(fs, files + random_files + ["diagram.mmd", "diagram1.mmd"])
    fs.create_file("output.txt")

    get_input_files.get_input_files("dir1", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files


def test_dir_deep(fs, random_files):
    """
    Test with the "dir" files options with a deep directory of mermaid files.
    """
    files = ["dir1/diagram.mmd", "dir1/diagram1.mmd", "dir1/bingo/diagram3.mmd"]
    fake_file_creator(
        fs, files + random_files + ["diagram.mmd", "diagram1.mmd", "dir2/hi.mmd"]
    )
    fs.create_file("output.txt")

    get_input_files.get_input_files("dir1", "mmd", "output.txt")

    parsed_output = output_getter("output.txt")
    assert len(parsed_output) == 1
    assert "input_files" in parsed_output.keys()
    assert json.loads(parsed_output["input_files"]) == files
