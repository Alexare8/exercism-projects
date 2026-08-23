import calendar
import datetime as dt

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


def start_of_first_workday(year: int, month: int) -> dt.datetime:
    date = dt.date(year=year, month=month, day=1)
    while date.weekday() > 4:
        date += dt.timedelta(days=1)
    return dt.datetime.combine(date, dt.time(hour=8))


def start_of_last_workday(year: int, month: int) -> dt.datetime:
    days_in_month = calendar.monthrange(year, month)[1]
    date = dt.date(year=year, month=month, day=days_in_month)
    while date.weekday() > 4:
        date -= dt.timedelta(days=1)
    return dt.datetime.combine(date, dt.time(hour=8))


def delivery_date(start: str, description: str) -> str:
    start_dt = dt.datetime.strptime(start, DATE_FORMAT)

    if description == "NOW":
        due_dt = start_dt + dt.timedelta(hours=2)

    elif description == "ASAP":
        if start_dt.time() < dt.time(hour=13):
            due_dt = start_dt.replace(hour=17, minute=0)
        else:
            due_dt = start_dt.replace(hour=13, minute=0) + dt.timedelta(days=1)

    elif description == "EOW":
        weekday = start_dt.date().weekday()
        if weekday < 3:  # Mon=0, Tue=1, Wed=2
            days_ahead = 4 - weekday
            due_time = dt.time(hour=17)
        elif weekday < 5:  # Thu=3, Fri=4
            days_ahead = 6 - weekday
            due_time = dt.time(hour=20)
        else:
            raise ValueError("Invalid Description")

        due_date = start_dt.date() + dt.timedelta(days=days_ahead)
        due_dt = dt.datetime.combine(due_date, due_time)

    elif description.endswith("M"):  # Matches format "<N>M"
        month = int(description[:-1])
        if start_dt.date().month < month:
            due_dt = start_of_first_workday(start_dt.year, month)
        else:
            due_dt = start_of_first_workday(start_dt.year + 1, month)

    elif description.startswith("Q"):  # Matches format "Q<N>"
        quarter = int(description[1])
        if start_dt.month <= quarter * 3:
            due_dt = start_of_last_workday(start_dt.year, quarter * 3)
        else:
            due_dt = start_of_last_workday(start_dt.year + 1, quarter * 3)

    else:
        raise ValueError("Invalid Description")

    return due_dt.strftime(DATE_FORMAT)
