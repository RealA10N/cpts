from typing import NoReturn

import rich
import typer
from rich.align import Align
from rich.console import Group, RenderableType
from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style


class Logger:
    def abort(
        self,
        title: str,
        desc: str = "",
        exit_code: int = 1,
    ) -> NoReturn:
        self._print(
            Padding(
                Group(
                    Panel(
                        f"[bold]{title}:[/bold] {desc}",
                        border_style="red",
                        title=":boom: Error!",
                    ),
                    Align(
                        Padding(
                            f"exited with code {exit_code}",
                            pad=(0, 2, 0, 0),
                            style="italic bright_black",
                        ),
                        align="right",
                    ),
                ),
                pad=1,
            )
        )

        raise typer.Exit(code=exit_code)

    def error(self, title: str, desc: str = "") -> None:
        self._label_print(
            title=title,
            desc=desc,
            label_text=":boom: ERROR",
            label_style="on red",
        )

    def warning(self, title: str, desc: str = "") -> None:
        self._label_print(
            title=title,
            desc=desc,
            label_text=":warning: WARNING",
            label_style="on yellow",
        )

    def success(self, title: str, desc: str = "") -> None:
        self._label_print(
            title=title,
            desc=desc,
            label_text=":heavy_check_mark: SUCCESS",
            label_style="on green",
        )

    def info(self, title: str, desc: str = "") -> None:
        title = title if not desc else f"{title}: "
        self._print(f"[bright_black][bold]{title}[/bold]{desc}[/]")

    def _print(self, text: RenderableType) -> None:
        rich.print(text)

    def _label_print(
        self,
        label_text: str,
        label_style: str | Style,
        title: str,
        desc: str = "",
    ) -> None:
        label = f"[{label_style}] {label_text} [/{label_style}]"
        title = title if not desc else f"{title}: "
        self._print(label + f" [white][bold]{title}[/bold]{desc}[/white]")


logger = Logger()

if __name__ == "__main__":
    logger.info("operation in process", desc="running tests...")
    logger.success("operation completed", desc="all tests have passed!")
    logger.warning("operation failed", desc="some tests yielded warnings...")
    logger.error("operation exited", desc="all tests have failed")
    try:
        logger.abort("operation exited", desc="all tests have failed")
    except typer.Exit as error:
        exit(error.exit_code)
