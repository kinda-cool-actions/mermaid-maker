from .. import pkg_manager_setup


def test_pnpm_pkg_manager(monkeypatch):
    run_command = []
    monkeypatch.setattr(pkg_manager_setup, "run", lambda arg: run_command.extend(arg))
    pkg_manager_setup.pkg_manager_setup("pnpm")
    assert run_command == [
        "pnpm",
        "config",
        "set",
        "--location=project",
        "strictDepBuilds",
        "false",
    ]
