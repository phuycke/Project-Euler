#!/usr/bin/env python3

# Problem setting
"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import calendar

count = 0

def countDays(lowerbound, upperbound, when, weekday):
    """Specify from which year up to which year we are considering, enter the day of the month, and the day we seek.
    The function returns how many times this day falls on that time in the month."""

    count = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for year in range(lowerbound, upperbound + 1):
        for month in range(1, 13):
            day = days[calendar.weekday(year,month,when)]
            if day == weekday:
                count += 1
            if year == upperbound and month == 12:
                break

    return count

print(countDays(1901, 2000, 1, "Sunday"))