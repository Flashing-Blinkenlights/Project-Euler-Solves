# problem: from 1st Jan 1900 to 31 Dec 2000, how many times was the first day of the month a Sunday?
# observation: there are 12 months a year and 100 years to check, so 1200 months that need to be checked

from datetime import date, timedelta
from calendar import monthrange

START = date(1901, 1, 1)
END = date(2000, 12, 31)

current_date = START
sundays = 0

while current_date <= END:
    weekday, days = monthrange(current_date.year, current_date.month)
    print(current_date.isoformat(), weekday, days)
    if weekday == 6:
        sundays += 1
    current_date += timedelta(days=days)

print(sundays)
