import datetime

def calendar_module(month: int, day: int, year: int) -> str:

    date = datetime.date(year, month, day)
    return date.strftime("%A").upper()