#!/usr/bin/env python3

# Problem setting
"""
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with n=0.
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


def checkConsecutivePrimes(a, b):

    """Checks how many consecutive primes are created for the formula, depending on the inputted a & b."""

    counted = 0
    allPrimes = True
    n = 0

    while allPrimes:
        number = n**2 + a*n + b
        if is_prime(number):
            counted += 1
            n += 1
        else:
            allPrimes = False

    return counted


def longestPrimeChain(limit):

    longestchain = 40
    pair = [1, 41]

    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            computed = checkConsecutivePrimes(a, b)
            if computed > longestchain:
                longestchain = computed
                pair = [a, b]

    print("The longest chain of primes contains", longestchain, "primes in total.")
    return pair


print(checkConsecutivePrimes(-79, 1601))
print(longestPrimeChain(1000))
