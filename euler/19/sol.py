"""
Solution to Euler Problem number 19.

For humor, we use Conway's doomsday algorithm:
https://www.timeanddate.com/date/doomsday-weekday.html

This is opposed to the trivial datetime module's approach: 
import datetime
count = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if datetime.date(y, m, 1).weekday() == 6:
            count += 1
print count #171
"""

days = {
    "Sunday": 0,    "Monday": 1,
    "Tuesday": 2,   "Wednesday": 3,
    "Thursday": 4,  "Friday": 5,
    "Saturday": 6
}

first_of_month_to_closest_doomsday = {
    3: 6,   4: 3,   5: 8,   6: 5,
    7: 10,  8: 7,   9: 4,   10: 9,
    11: 6,  12: 11
}

def doomsday(year):
    step_1 = int(str(year)[-2:]) / 12
    step_2 = int(str(year)[-2:]) % 12
    step_3 = step_2 / 4
    if year < 2000:
        step_4 = days['Wednesday']  # for 1900 - 1999
    else:
        step_4 = days['Tuesday']    # for 2000 - 2099
    return sum([step_1, step_2, step_3, step_4]) % 7

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def day_of_week(month, day, year):
    dday = doomsday(year)
    if month == 1:
        offset = 31 + 27 + isLeapYear(year)
    elif month == 2:
        offset = 27 + isLeapYear(year)
    else:
        offset = first_of_month_to_closest_doomsday[month]
    return (dday - offset + day - 1) % 7


def counts_months_starting_on(day_name):
    count = 0
    for y in range(1901, 2000 + 1):
        for m in range(1, 12 + 1):
            if days[day_name] == day_of_week(m, 1, y):
                count += 1
    return count

print counts_months_starting_on("Sunday")
