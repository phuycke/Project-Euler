#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import csv

#%%

def list_prod(inputlist : list) -> int:
    """
    Returns the product of all elements in a list

    Parameters
    ----------
    inputlist : list
        The list containing all numbers.

    Returns
    -------
    int
        The product of all integers in the list

    """

    result = inputlist[0]
    for i in range(1, len(inputlist)):
        result *= inputlist[i]
    return result  
    
    
def driver(digit : list, shift : int) -> int:
    """
    Will give the largest possible number obtained by multiplying shift 
    adjacent numbers.

    Parameters
    ----------
    digit : list
        A list containing all the values in the long number.
    shift : int
        The n numbers that we considered when computing the product.

    Returns
    -------
    int
        The largest product that comes out.

    """

    prod = 0
    for i in range(len(digit) - shift):
        num_slice = digit[i:i+shift]
        if list_prod(num_slice) > prod:
            prod = list_prod(num_slice)

    return prod


#%%

nums = []
with open(r"C:\Users\pieter\Downloads\GitHub\phuycke\Project-Euler\Other\help_08.txt", 'r') as f:
    reader = csv.reader(f, dialect = 'excel', delimiter = '\n')
    for row in reader:
        nums.extend(row)
nums = [int(n) for n in list("".join(nums))]


solution  = driver(nums, 13)
print("The solution to this problem is: %d" %(solution))
