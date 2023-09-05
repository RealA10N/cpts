from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text


class CPTSBaseError(Exception):
    """A base (excepted) error, that when raised is caught by the CLI."""

    def __init__(
        self, title: str, description: str, exit_code: int = 1
    ) -> None:
        self.title = title
        self.description = description
        self.exit_code = exit_code

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"

    def __rich__(self) -> str:
        return Group(
            Panel(
                f"[bold]{self.title}:[/bold] {self.description}",
                border_style="red",
                title=":boom: Error!",
            ),
            Align(
                Padding(
                    f"exited with code {self.exit_code}",
                    pad=(0, 2, 0, 0),
                    style="italic bright_black",
                ),
                align="right",
            ),
        )
