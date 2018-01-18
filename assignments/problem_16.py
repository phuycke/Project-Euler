#!/usr/bin/env python3

# Problem setting
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

def powerDigitSum(base, exponent):
    """First calculates base to the exponent, then adds all the individual integers of the resulting number.
    Returns that sum."""

    exponentiation = base ** exponent
    seperateNumbers = list(str(exponentiation))

    i = 0
    sum = 0

    while i < len(seperateNumbers):
        sum = sum + int(seperateNumbers[i])
        i += 1

    return sum

print(powerDigitSum(2, 1000))

