#!/usr/bin/env python3

# Problem setting
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


def is_prime(n):

    """Checks whether a number is a prime."""

    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def factorize(number):

    """Decomposes numbers into smaller prime numbers."""

    prime = 2
    factors = []
    not_prime = True

    while not_prime:
        if is_prime(number):
            factors.append(number)
            not_prime = False
        else:
            if number % prime == 0:
                number = number // prime
                factors.append(prime)
            else:
                while True:
                    prime += 1
                    if is_prime(prime):
                        break

    counting = []

    for j in range(len(factors)):
        counted = factors.count(factors[j])
        needed = factors[j] ** counted
        if needed not in counting:
            counting.append(needed)

    return counting


def sharenone(list1, list2):

    if len(list1) != len(list2):
        raise ValueError("The lists have to be of the same length.")

    list1.sort()
    list2.sort()

    distinct = True

    for j in range(len(list1)):
        if list1[j] == list2[j]:
            distinct = False
            break

    return distinct


def distinctprimes(digits):

    # if the set of the addition of two list equals the addition of the two list, then the lists are distinct
    # this could be far more efficient, but it is the end of the day, and this also works, be it less efficient

    first = 644
    second = 645
    third = 646
    fourth = 647

    first_result = 0
    second_result = 0
    third_result = 0
    fourth_result = 0

    not_found = True
    while not_found:
        if not is_prime(first) and not is_prime(second) and not is_prime(third) and not is_prime(fourth):
            firstFactors = factorize(first)
            secondFactors = factorize(second)
            thirdFactors = factorize(third)
            fourthFactors = factorize(fourth)
            if len(firstFactors) == digits and len(secondFactors) == digits and \
                    len(thirdFactors) == digits and len(fourthFactors) == digits:
                if sharenone(firstFactors, secondFactors) and sharenone(thirdFactors, fourthFactors) \
                        and sharenone(secondFactors, thirdFactors):
                    first_result = first
                    second_result = second
                    third_result = third
                    fourth_result = fourth
                    not_found = False
        first += 1
        second += 1
        third += 1
        fourth += 1

    return [first_result, second_result, third_result, fourth_result]


print(distinctprimes(4))
