#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%


def is_palindrome(number : int) -> bool:
    """
    Returns boolean depending on whether a number is a palindrome or not

    Parameters
    ----------
    number : int
        The number to check.

    Returns
    -------
    bool
        True if a palindrome, False if not.

    """
    
    if list(str(number)) == list(str(number))[::-1]:
        return True
    else:
        return False
    

#%%
    
import numpy as np


largest_product = -1
coef1, coef2    = -1, -1

for i in np.arange(999, 99, -1):
    for j in np.arange(999, 99, -1):
        if is_palindrome(i * j) and (i * j) > largest_product:
            largest_product = i * j
            coef1, coef2    = i, j
            
print("Largest product: {}\nResult of {} times {}".format(largest_product, 
                                                          coef1, coef2))
