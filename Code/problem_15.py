#!/usr/bin/env python3

# Problem setting
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
def listProduct(inputlist):
    """Returns the product of all elements within the list."""

    if len(inputlist) == 0:
        raise ValueError("The list must contain at least one element.")
    elif len(inputlist) == 1:
        result = inputlist[0]
    else:
        result = inputlist[0]
        for i in range(1, len(inputlist)):
            result = result * inputlist[i]
    return result

def latticepath(n, k):
    """Returns how many different paths you can take to get to point (n,k)."""

    # These calculations are based on these theories:
        # https://en.wikipedia.org/wiki/Lattice_path
        # https://en.wikipedia.org/wiki/Binomial_coefficient

    upper = n + k
    lower = n

    nFactorial = listProduct(list(range(1, upper+1)))
    kFactorial = listProduct(list(range(1, lower+1)))
    nkFactorial = listProduct(list(range(1, (upper - lower)+1)))

    binomCoeff = int((nFactorial / (kFactorial*nkFactorial)))

    return binomCoeff

solution = latticepath(20,20)
print("There are %d ways to get to the other side of a 20x20 maze." %(solution))



