import typer

from create_py_project.utils import generate_project

app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Tool to create a python projects.
    """


def main():
    project_name = typer.prompt("What's your Project name?")

    templates = {
        "1": "template-vannila",
        "2": "template-fastapi-starter",
        "3": "template-django",
        "4": "template-drf-and-auth",
        "5": "template-ml-and-dl",
    }

    prompt_text = """Choose Project Template:
    1. Vannila Python Project
    2. FastAPI Project
    3. Django Project
    4. Django Project with drf and auth
    5. Ml/DL Project
    """
    template = typer.prompt(prompt_text)

    if template not in templates:
        print("ERROR:Select a valid Number")
        return

    template_name = templates[template]

    generate_project(name=project_name, template=template_name)


if __name__ == "__main__":
    typer.run(main)
