"""Date/calendar helpers shared across levels."""

import calendar
import datetime


def today() -> datetime.date:
    return datetime.date.today()


def today_formatted(fmt: str = "%A, %d %B %Y") -> str:
    return datetime.datetime.now().strftime(fmt)


def days_between(target_date: datetime.date, from_date: datetime.date = None) -> int:
    from_date = from_date or today()
    return (target_date - from_date).days


def print_month_calendar(year: int, month: int) -> None:
    print()
    print(calendar.month(year, month))