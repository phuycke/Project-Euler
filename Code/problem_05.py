#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import numpy      as     np

from   problem_03 import prime_factorize

#%%

# compute the prime factors of all numbers <= 20
prime_factors = []
primes        = []

for i in np.arange(1, 21):
    result = prime_factorize(i)
    prime_factors.append(result)
    primes.extend(result)

# for all primes, find the max occurence count, and multiply these together
prod = 1
for prime in set(primes):
    counted, kept = -1, -1
    for l in prime_factors:
        if l.count(prime) > counted:
            counted = l.count(prime)
            kept    = prime
    for i in range(counted):
        prod *= prime
  
    
#%%
        
print("Smallest number divisble by numbers in [1, 21]: {}".format(prod))