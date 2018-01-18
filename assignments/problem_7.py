#!/usr/bin/env python3

# Problem setting
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def isPrime(integer):
    """Returns True  if the number is a prime, returns False otherwise."""

    is_prime = True
    start = 2
    if integer == 2:
        return True
    else:
        while is_prime and start < integer:
            if integer % start == 0:
                is_prime = False
            else:
                start += 1
    return is_prime

def countPrimes(quantity):
    """Records all primes in a list until the list has a length of n. Then returns the reversed prime number list."""

    primeList = [2,3,5,7,11,13]
    number = primeList[-1] + 2
    while len(primeList) != quantity:
        if isPrime(number):
            primeList.append(number)
            number += 2
        else:
            number += 2

    print(len(primeList))
    return primeList[::-1]

print(countPrimes(10001))