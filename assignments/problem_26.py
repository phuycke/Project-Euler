#!/usr/bin/env python3

# Problem setting
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def periodlength(number):

    """Define the period length of the decimal expansion of a fraction."""

    denominator = number
    searching = True
    power = 1

    avoiding = [2, 4, 5, 8, 10]

    for j in range(len(avoiding)):
        if number % avoiding[j] == 0:
            return 0

    while searching:
        if ((10 ** power) - 1) % denominator == 0:
            return power
        else:
            power += 1


def largestCycle(limit):

    """Find the number which has the largest returning cycle by dividing 1 through a certain number."""

    cycle = 6
    number = 7

    for nums in range(2, limit + 1):
        if periodlength(nums) > cycle:
            cycle = periodlength(nums)
            number = nums

    return [number, cycle]


result = largestCycle(1000)
print("The number", result[0], "has a cycle length of", result[1])
