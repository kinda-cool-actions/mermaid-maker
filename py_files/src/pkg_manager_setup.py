from os import environ
from subprocess import run


def pkg_manager_setup(pkg_manager):
    if pkg_manager == "npm":
        print("Nothing to setup")
    elif pkg_manager == "pnpm":
        run(
            ["pnpm", "config", "set", "--location=project", "strictDepBuilds", "false"],
            check=True,
        )
    elif pkg_manager == "yarn":  # noqa: SIM114
        print("Nothing to setup")
    elif pkg_manager == "bun":
        print("Nothing to setup")
    else:
        raise ValueError("Inputted pkg_manager is not recognized")


if __name__ == "__main__":
    pkg_manager_setup(environ["PKG_MANAGER"])
