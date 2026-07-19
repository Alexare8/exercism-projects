class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self.time = (hour * 60 + minute) % 1440

    def __repr__(self) -> str:
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self) -> str:
        return f'{str(self.hour).rjust(2, '0')}:{str(self.minute).rjust(2, '0')}'

    def __eq__(self, other) -> bool:
        return self.time == other.time

    def __add__(self, minutes: int) -> str:
        self.time = (self.time + minutes) % 1440
        return self.__str__()

    def __sub__(self, minutes: int) -> str:
        self.time = (self.time - minutes) % 1440
        return self.__str__()

    @property
    def minute(self) -> int:
        return self.time % 60
    
    @property
    def hour(self) -> int:
        return self.time // 60