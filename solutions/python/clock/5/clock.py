from __future__ import annotations


class Clock:

    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

    def __init__(self, hour: int, minute: int) -> None:
        self.time = (hour * self.MINUTES_PER_HOUR + minute) % self.MINUTES_PER_DAY

    def __repr__(self) -> str:
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other) -> bool:
        return self.time == other.time

    def __add__(self, minutes: int) -> Clock:
        time = (self.time + minutes) % self.MINUTES_PER_DAY
        return Clock(0, time)

    def __sub__(self, minutes: int) -> Clock:
        time = (self.time - minutes) % self.MINUTES_PER_DAY
        return Clock(0, time)

    @property
    def minute(self) -> int:
        return self.time % self.MINUTES_PER_HOUR
    
    @property
    def hour(self) -> int:
        return self.time // self.MINUTES_PER_HOUR