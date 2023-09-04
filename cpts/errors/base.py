class CPTSBaseError(Exception):
    """A base (excepted) error, that when raised is caught by the CLI."""

    def __init__(self, title: str, description: str | None = None) -> None:
        self.title = title
        self.description = description
