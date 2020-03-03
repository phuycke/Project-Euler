#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

def fibonacci(limit):
    """Find all fibonacci numbers below a certain limit, and sum those that are evenly divisible by two."""

    startList     = [1,2]
    criticalValue = 0
    sumList       = [2]
    while criticalValue < limit:
        fibonacciValue = startList[-2] + startList[-1]
        if fibonacciValue % 2 ==0:
            sumList.append(fibonacciValue)
        startList.append(fibonacciValue)
        criticalValue = fibonacciValue

    return sum(sumList)

#%%
    
print("The sum of the even fibonacci numbers up to 4.000.000 is: %d." %(fibonacci(4000000)))