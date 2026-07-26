from ..src import pkg_manager_teardown


def test_pnpm_pkg_manager(monkeypatch):
    """
    Test with the 'pnpm' option to see if the run command runs the correct args
    """
    run_command = []
    monkeypatch.setattr(
        pkg_manager_teardown, "run", lambda arg, check: run_command.extend(arg)
    )
    pkg_manager_teardown.pkg_manager_teardown("pnpm")
    assert run_command == [
        "pnpm",
        "config",
        "set",
        "--location=project",
        "strictDepBuilds",
        "true",
    ]
