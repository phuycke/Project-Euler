#!/usr/bin/env python3

# Problem setting
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(number):
    """Returns the factorial of a certain number."""

    if number == 0:
        return 1
    else:
       return number * factorial(int(number-1))

def sumDigits(number):
    """Splits a number into single digits, returns the sum of those single digits."""

    inBetween = str(number)
    numList = []
    [numList.append(int(element)) for element in inBetween]

    return sum(numList)

between = factorial(10)
solution = sumDigits(between)
print("The solution to this problem is: %d" %(solution))

