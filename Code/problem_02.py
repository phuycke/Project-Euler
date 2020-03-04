#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

def fibonacci(limit : int) -> int:
    """
    Returns the sum of the even Fibonacci numbers below limit

    Parameters
    ----------
    limit : int
        The upper limit, we compute fibo numbers while they are < limit

    Returns
    -------
    int
        The final resulting sum

    """    
    
    prev, following = 1, 2
    fibo    = -1
    sumList = 2
    while fibo < limit:
        fibo = prev + following
        if fibo % 2 == 0:
            sumList += fibo
        prev, following = following, fibo

    return sumList

#%%
    
print("The sum of the even fibonacci numbers up to 4.000.000 is: %d." %(fibonacci(4000000)))