#!/usr/bin/env python3

#%%

# --------------- #
# Problem setting #
# --------------- #

"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
 multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
 can be written as a 1 through 9 pandigital.
 
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

#%%

import numpy as np

#%%

desired        = list(np.arange(1, 10))
needed_product = []

for i in np.arange(1, 10000):
    for j in np.arange(1, 10000):
        if len(list(str(i) + str(j) + str(i * j))) > 9:
            continue
        else:
            # check 1: check if the multipliers contain duplicate numbers
            if len(list(str(i))) != len(set(list(str(i)))) or len(list(str(j))) != len(set(list(str(j)))):
                continue
            # check 2: check if the multipliers do not share numbers
            elif not set(list(str(i))).isdisjoint(list(str(j))):
                continue
            else:
                product = str(i * j)
                # check 3: check for duplicate numbers in the product
                if len(list(product)) != len(set(list(product))):
                    continue
                else: 
                    all_numbers = list(str(i) + str(j) + str(i * j))
                    all_numbers = [int(x) for x in all_numbers]
                    if set(all_numbers) == set(desired):
                        if (i * j) not in needed_product:
                            needed_product.append(i * j)
                            print('Pandigital product: {}'.format(i * j))
                            print('Multiplicand: {0} // Multiplier: {1}\n'.format(i, j))

#%%

print("Sum of the products: ", sum(needed_product))




