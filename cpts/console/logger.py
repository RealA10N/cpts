import contextlib
import itertools
import time
from typing import Iterable, NoReturn, Text

import rich
import typer
from rich.align import Align
from rich.console import Group, RenderableType
from rich.live import Live
from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style
from rich.text import Text


class Logger:
    LONG_THRESHOLD = 4

    def __init__(self) -> None:
        self.console = rich.get_console()

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
        self._print(
            self._generate_label(
                title=title,
                desc=desc,
                label_text=":boom: ERROR",
                label_style="on red",
            )
        )

    def warning(self, title: str, desc: str = "") -> None:
        self._print(
            self._generate_label(
                title=title,
                desc=desc,
                label_text=":warning: WARNING",
                label_style="on yellow",
            )
        )

    def success(self, title: str, desc: str = "") -> None:
        self._print(
            self._generate_label(
                title=title,
                desc=desc,
                label_text=":heavy_check_mark: SUCCESS",
                label_style="on green",
            )
        )

    def info(self, title: str, desc: str = "") -> None:
        title = title if not desc else f"{title}: "
        self._print(f"[bright_black][bold]{title}[/bold]{desc}[/]")

    def _print(self, renderable: RenderableType) -> None:
        self.console.print(renderable)

    def _generate_label(
        self,
        label_text: str,
        label_style: str | Style,
        title: str,
        desc: str = "",
    ) -> None:
        label = Text.from_markup(
            f"[{label_style}] {label_text} [/{label_style}] "
        )
        title = title if not desc else f"{title}: "
        return (
            label
            + Text.from_markup(title, style="white bold")
            + Text.from_markup(desc, style="white")
        )

    @contextlib.contextmanager
    def wait(
        self,
        animation: Iterable[str],
        label: str,
        title: str,
    ):
        animation = itertools.cycle(animation)
        dots = itertools.cycle("." * i for i in range(4))

        start = time.time()

        def render():
            renderable = self._generate_label(
                f"{next(animation)} {label}",
                label_style="on bright_blue",
                title=title,
            )

            if time.time() - start > self.LONG_THRESHOLD:
                renderable += Text.from_markup(
                    f" It might take some time{next(dots)}",
                    style="italic bright_black",
                )
            return renderable

        live = Live(
            console=self.console,
            transient=True,
            refresh_per_second=2,
            get_renderable=render,
        )

        live.__enter__()
        try:
            yield
        finally:
            live.__exit__(None, None, None)


_logger = Logger()


def getLogger() -> Logger:
    return _logger


if __name__ == "__main__":
    _logger.info("operation in process", desc="running tests...")
    _logger.success("operation completed", desc="all tests have passed!")
    _logger.warning("operation failed", desc="some tests yielded warnings...")
    _logger.error("operation exited", desc="all tests have failed")
    try:
        _logger.abort("operation exited", desc="all tests have failed")
    except typer.Exit as error:
        exit(error.exit_code)
