from os import environ
from subprocess import run


def pkg_manager_teardown(pkg_manager):
    if pkg_manager == "npm":
        print("Nothing to teardown")
    elif pkg_manager == "pnpm":
        run(
            ["pnpm", "config", "set", "--location=project", "strictDepBuilds", "true"],
            check=True,
        )
    elif pkg_manager == "yarn":
        print("Nothing to teardown")
    elif pkg_manager == "bun":
        print("Nothing to teardown")
    else:
        raise ValueError("Inputted pkg_manager is not recognized")


if __name__ == "__main__":
    pkg_manager_teardown(environ["PKG_MANAGER"])
