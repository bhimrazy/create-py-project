import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_project(name: str, template: str):
    print("Generating....")
    project_path = os.path.join(BASE_DIR, "stubs", template)
    if name == ".":
        print("Generating project on root directory...")
        shutil.copytree(project_path, name, dirs_exist_ok=True)
    else:
        shutil.copytree(project_path, name)

    end_text = f"""\nCompleted.
    cd into {name} directory
    and then follow the instructions in the README.md file
    """
    print(end_text)
    print("Thank you for using create-py-project.^_^")
    print("Author:@bhimrazy")
