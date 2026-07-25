from os import chdir
from os.path import dirname
from pathlib import Path
from subprocess import run


def bundle_py_files(option: str, interactive: bool = False):
    option_lower = option.lower()
    if option_lower in ["yes", "y"]:
        chdir(Path(dirname(__file__)) / ".." / "py_files_to_action_bundler")
        if interactive:
            print("Bundling...")
        run(["pnpm", "bundle_to_action"], check=True)
        if interactive:
            print("Completed!")
    elif option_lower in ["q", "quit"]:
        if interactive:
            print("Quitting...")
    else:
        if interactive:
            print(f"Sorry! But {option} is not a recognized command. Exiting...")


if __name__ == "__main__":
    prompt = input(
        "=" * 120
        + "\n"
        + """Do you want to bundle the python files into the action.yml run commands?
    - Type "yes" or "y" to bundle them.
    - Type "quit" or "q" to quit."""
        + "\n"
        + "=" * 120
        + "\n"
    )

    bundle_py_files(prompt, interactive=True)
