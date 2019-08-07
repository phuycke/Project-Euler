#!/usr/bin/env python3

# Problem setting
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(number):
    """Calculate the factorial of a number."""

    if number == 0:
        return 1
    else:
       return number * factorial(int(number-1))

def factorions(lowerbound, upperbound):
    """Find the numbers for which the sum of the factorials of the single digits equals the number itself."""

    number = 0
    found = []

    while number <= upperbound:
        check = str(number)
        digits = []

        for digit in check:
            digits.append(int(digit))

        sum = factorial(int(digits[0]))
        for i in range(1, len(digits)):
            sum = sum + factorial((digits[i]))


        if (int(sum) == number) and (number > lowerbound):
            found.append(number)

        number += 1

    return found

print(factorions(2, 1000000))
