import pytest

from ..src.set_pkg_manager_run import set_pkg_manager_run
from .utility.output_getter import output_getter


def test_set_pkg_manager_run(fs):
    fs.create_file("output.txt")
    set_pkg_manager_run("npm", "output.txt")
    assert "npx" == output_getter("output.txt")["pkg_manager_run_cmd"]

    fs.create_file("output1.txt")
    set_pkg_manager_run("pnpm", "output1.txt")
    assert "pnpm" == output_getter("output1.txt")["pkg_manager_run_cmd"]

    fs.create_file("output2.txt")
    set_pkg_manager_run("yarn", "output2.txt")
    assert "yarn dlx" == output_getter("output2.txt")["pkg_manager_run_cmd"]

    fs.create_file("output3.txt")
    set_pkg_manager_run("bun", "output3.txt")
    assert "bunx" == output_getter("output3.txt")["pkg_manager_run_cmd"]

    with pytest.raises(ValueError):
        fs.create_file("output_exception.txt")
        set_pkg_manager_run("boom", "output_exception.txt")
