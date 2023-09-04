# encoding
import typer

app = typer.Typer(
    name="cpts",
    rich_markup_mode="markdown",
    help="""**Competitive Programming Testing Suite**: A modern approach for
    developing, testing and evaluating competitive programming problems and
    submissions 🧑‍💻⚡""",
)


@app.command()
def init():
    """Initialize a docker isolated environment.

    This environment will be used for baking and testing on your local machine.
    If available, an official CPTS Docker image will be pulled and installed
    locally. Otherwise, an image will be built and installed locally.
    *A docker daemon is required.*"""


@app.command()
def bake():
    """Bake a problem package, making it ready for production use.

    Each problem package should be baked before it can be executed and evaluated
    against user submissions. In the process, all test generators are executed,
    tests are validated and the bundled submissions are evaluated.
    *Read the docs for more information about the full baking process.*"""


def main():
    app(prog_name="cpts")


if __name__ == "__main__":
    main()
