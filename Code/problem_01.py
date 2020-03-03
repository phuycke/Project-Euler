#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%


def sumDivisors(limit : int) -> int:
    """
    Find the sum of all number below the limit which are divisible by 3 or 5

    Parameters
    ----------
    limit : int
        The upper limit for our function.

    Returns
    -------
    sum : int
        The sum of numbers below limit that are divisible by 3 or 5.

    """

    return sum(set(list(range(0, limit, 3)) + list(range(0, limit, 5))))


#%%
    
print("The sum equals: %d." %(sumDivisors(limit = 1000)))