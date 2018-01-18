#!/usr/bin/env python3

# Problem setting
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sumDivisors(number):
    """Find the sum of number below n that are divisible by 3 and 5."""

    sum = 0
    for n in range(number):
        if (n % 3 == 0) or (n % 5 == 0):
            sum = sum + n

    return sum

solution = sumDivisors(1000)
print("The sum equals: %d." %(solution))