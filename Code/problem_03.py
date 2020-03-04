#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%


def is_prime(n : int) -> bool:
    """
    Returns whether a number is a prime or not

    Parameters
    ----------
    n : int
        The number to check for primality.

    Returns
    -------
    bool
        True if number is a prime, False otherwise.

    """

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


def prime_factorize(number : int) -> list:
    """
    Returns a list of all the prime factors of the inputted number

    Parameters
    ----------
    number : int
        The number to factorize.

    Returns
    -------
    list
        Returns a list of the prime factors of the original number.

    """
    
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


#%%

# print(max(prime_factorize(600851475143)))
