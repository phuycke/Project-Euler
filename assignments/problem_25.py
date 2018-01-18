#!/usr/bin/env python3

# Problem setting
"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibo(number):
    """A recursive function that calculates a fibonacci sequence."""

    startList = [0, 1]
    for i in range(number - 1):
        startList.append(startList[-1] + startList[-2])

    return startList[-1]


def minimumFibo(digits):
    """A function that returns the number for which its fibonacci number contains at least n digits."""

    number = 0
    cycling = True
    while cycling:
        fibonaccinumber = fibo(number)
        between = list(str(fibonaccinumber))
        if len(between) < digits:
            number += 1
        else:
            cycling = False

    return number

solution = minimumFibo(1000)
print("The number which has a fibonacci number that consist of 1000 digits is: %d" %(solution))