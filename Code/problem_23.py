#!/usr/bin/env python3

# Problem setting
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def divisors(number):

    """Returns the divisors of a number."""

    div = []
    start = 1

    while start <= number ** .5:
        if number % start == 0:
            div.append(start)
            if start != 1:
                div.append(number // start)
        start += 1

    result = set(div)
    return sorted(result)


def abundantNums(limit):

    """Find all abundant numbers below a certain limit."""

    number = 1
    abundant = []

    while number <= limit:
        if sum(divisors(number)) > number:
            abundant.append(number)
        number += 1

    result = set(abundant)
    return sorted(result)


def notAsSum(limit):

    """Returns the sum of all numbers that cannot be written as the sum of two abundant numbers."""

    abundantNumbers = abundantNums(limit)
    notSumOfAbundant = list(range(1, 24))

    number = 24

    while number <= limit:
        satisfied = True
        for j in range(len(abundantNumbers)):
            if (number - abundantNumbers[j]) < 12:
                break
            elif (number - abundantNumbers[j]) in abundantNumbers:
                satisfied = False
                break
        if satisfied:
            notSumOfAbundant.append(number)
        if number % 500 == 0:
            print("Now considering number", number)
        number += 1

    result = set(notSumOfAbundant)
    return sorted(result)


upperlim = 28123
result = notAsSum(upperlim)
print("The sum of all numbers below", upperlim,
      "that cannot be expressed as the sum of two abundant numbers is: %d" % result)
