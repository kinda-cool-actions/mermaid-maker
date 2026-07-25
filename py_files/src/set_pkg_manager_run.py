from subprocess import run
from os import environ


def set_pkg_manager_run(pkg_manager, output_file):
    pkg_manager_run_cmd = ""
    if pkg_manager == "npm":
        pkg_manager_run_cmd = "npx"
    elif pkg_manager == "pnpm":
        pkg_manager_run_cmd = "pnpm"
    elif pkg_manager == "yarn":
        pkg_manager_run_cmd = "yarn dlx"
    elif pkg_manager == "bun":
        pkg_manager_run_cmd = "bunx"
    else:
        run(["exit", "1"])

    with open(output_file, "a") as file:
        print("pkg_manager_run_cmd=" + pkg_manager_run_cmd, file=file)


if __name__ == "__main__":
    set_pkg_manager_run(environ["PKG_MANAGER"], environ["GITHUB_OUTPUT"])
