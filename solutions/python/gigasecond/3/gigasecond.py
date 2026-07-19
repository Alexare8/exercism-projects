from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds = 1_000_000_000)

def add(moment: datetime) -> datetime:
    """Returns a time 1 Gigasecond after the input."""
    return moment + GIGASECOND
