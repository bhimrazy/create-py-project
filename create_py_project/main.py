import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Tool to create a python projects.
    """


@app.command()
def fastapi():
    """
    Create a complete fastapi project.
    """
    typer.echo("Loading Project")


@app.command()
def flask():
    """
    Create a complete flask project.
    """
    typer.echo("Loading Project")


@app.command()
def ml_flask():
    """
    Create a complete flask based ml project.
    """
    typer.echo("Loading Project")
