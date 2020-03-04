#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import numpy      as     np

from   problem_03 import is_prime

#%%


def countPrimes(n : int) -> int:
    """
    Returns the nth prime number

    Parameters
    ----------
    n : int
        Which prime number do we need?

    Returns
    -------
    int
        Returns the nth prime number as an integer.

    """


    prime_list     = np.zeros(n, dtype = int)
    prime_list[:6] = [2, 3, 5, 7, 11, 13]
    number         = prime_list[5] + 2
    indx           = 6
    
    # the actual compilation of primes
    while prime_list[-1] == 0:
        if is_prime(number):
            prime_list[indx] = number
            number += 2
            indx   += 1
        else:
            number += 2

    return prime_list[-1]

#%%
    
res = countPrimes(10001)
print(res)