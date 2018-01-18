#!/usr/bin/env python3

# Problem setting:
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
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


def primeFactorize(number):

    """Factorizes a number into primes."""

    divisor = 2
    divisorList = []

    while number >= 2:
        if number % divisor == 0:
            divisorList.append(divisor)
            number = number // divisor
        elif is_prime(number):
            divisorList.append(number)
            break
        else:
            divisor += 1

    return divisorList


print(primeFactorize(45))
