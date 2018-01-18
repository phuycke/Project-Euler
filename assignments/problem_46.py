#!/usr/bin/env python3

# Problem setting
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""


def SieveOfEratosthenes(n):

    """Returns all prime numbers below a certain limit."""

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes


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


def isSquare(number):

    """Returns True if a certain number is a square. Returns false otherwise."""

    start = 1
    square = False

    if number == 1:
        return True

    while start < number:
        if start ** 2 == number:
            square = True
            break
        start += 1

    return square


def checkGoldbach(number):

    """Returns True if the hypothesis of Goldbach checks out. Returns False otherwise."""

    primesbelow = SieveOfEratosthenes(number)
    index = 0
    found = False

    while index < len(primesbelow):
        firstprime = primesbelow[index]
        result = number - firstprime
        possiblesquare = result // 2
        if isSquare(possiblesquare):
            found = True
            break
        index += 1

    return found


def proveGoldbachWrong():

    """Find the first odd number for which Goldbach's hypothesis doesn't work out."""

    number = 33
    found = False

    while not found:
        if is_prime(number):
            number += 2
        else:
            correct = checkGoldbach(number)
            if correct:
                number += 2
            else:
                found = True

    return number


result = proveGoldbachWrong()
print("The first odd number for which Goldbach's hypothesis doesn't work out is: %d" % result)
