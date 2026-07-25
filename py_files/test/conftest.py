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
