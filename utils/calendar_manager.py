import calendar
import json
from datetime import datetime

FILE_NAME = "goals.json"


def load_goals():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_goals(goals):
    with open(FILE_NAME, "w") as file:
        json.dump(goals, file, indent=4)


def show_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print(calendar.month(year, month))


def today():
    print(datetime.now().strftime("%A %d %B %Y"))