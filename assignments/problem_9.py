#!/usr/bin/env python3

# Problem setting
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagoreanTriplets(upperbound):
    """Search a pythagorean triple for which a + b + c equals the inputted  number."""

    a = upperbound - 2
    b = upperbound - 1
    c = upperbound

    result = [0, 0, 0]

    for i in range(1,c+1):
        for j in range(1,b+1):
            for k in range(1,a+1):
                if (k + i + j > upperbound) or (k**2) + (j**2) != (i**2):
                    continue
                elif (k**2) + (j**2) == (i**2) and (k + j + i == upperbound):
                    result = [k, j, i]
                    break
                else:
                    pass

    return result

needed = pythagoreanTriplets(1000)

solution = needed[0] * needed[1] * needed[2]
print("The solution to this problem is:", solution, "as", needed, "is the Pythagorean triplet we sought.")
