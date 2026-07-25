import pytest


@pytest.fixture
def random_files():
    return [
        "hi.png",
        "rainbow.pdf",
        "dir/beebop.txt",
        "dir/somefile.js",
        "dir/dir1/hi.py",
    ]


# two types of mmd suffixes to make sure that the suffix is not a dependency


@pytest.fixture
def flat_mermaid_files():
    return [
        "diagram.mermaid",
        "diagram1.mermaid",
        "diagram2.mermaid",
        "diagram3.mermaid",
    ]


@pytest.fixture
def flat_mmd_files():
    return [
        "diagram.mmd",
        "diagram1.mmd",
        "diagram2.mmd",
        "diagram3.mmd",
    ]


@pytest.fixture
def deep_mmd_files():
    return [
        "diagram.mmd",
        "diagram1.mmd",
        "dir1/diagram.mmd",
        "dir1/diagram1.mmd",
    ]


@pytest.fixture
def deep_unique_mmd_files():
    return [
        "diagram.mmd",
        "diagram1.mmd",
        "dir1/diagram2.mmd",
        "dir1/diagram3.mmd",
    ]
