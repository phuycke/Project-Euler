#!/usr/bin/env python3

# Problem setting
"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""


def numberToPower(limit):

    number = 1
    sum = 0

    while number <= limit:
        sum = sum + (number ** number)
        number += 1

    result = list(str(sum))
    needed = result[-10::]

    print(sum)
    return int(''.join(needed))


print(numberToPower(1000))

