#!/usr/bin/env python3

# Problem setting
"""
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
3025 − 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumOfSquares(upperbound):
    """Calculates the sum of squares for all number from 1 up to the upperbound."""

    sum = 1
    for number in range(2,upperbound + 1):
        sum = sum + (number ** 2)

    return sum

def squareOfSum(upperbound):
    """Calculates the square of the sum of all numbers from 1 up to the upperbound."""

    sum = 1
    for number in range(2, upperbound + 1):
        sum = sum + number

    return sum ** 2

upperbound = 100

sum_of_squares = sumOfSquares(upperbound)
square_of_sums = squareOfSum(upperbound)

solution = square_of_sums - sum_of_squares

print("The difference between the two is: %d" %(solution))