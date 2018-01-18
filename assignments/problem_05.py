#!/usr/bin/env python3

# Problem setting
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# evenly divisible = having no remainder
    # https://math.stackexchange.com/questions/58555/what-is-meant-by-evenly-divisible

def evenlyDivided(upperbound):
    """Finds the largest number that is evenly divisible by all numbers from 1 up to the upperbound."""

    satisfied = False
    start = 1
    checked = 0
    while not satisfied:
        for number in range(1, upperbound + 1):
            if start % number != 0:
                break
            else:
                checked += 1
        if checked == upperbound:
            satisfied = True
        else:
            checked = 0
            start += 1
    return start

print(evenlyDivided(20))