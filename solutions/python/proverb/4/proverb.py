from itertools import pairwise, starmap

LINE_FORM = "For want of a {} the {} was lost."


def proverb(*needs: tuple[str], qualifier: str) -> list[str]:
    """Compose a proverb about the lack of the given list of inputs."""
    return [] if not needs else [*starmap(LINE_FORM.format, pairwise(needs)),
        f"And all for the want of a {qualifier + ' ' if qualifier else ''}{needs[0]}."]
