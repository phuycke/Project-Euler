#!/usr/bin/env python3

# Problem setting
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
of an integer with (1,2, ... , n) where n > 1?
"""

def permutations(inputted, s):

    """Gives all combinations of a certain string that is inputted."""

    if len(s) == len(inputted):
        yield s
    for i in inputted:
        if i in s:
            continue
        s = s+i
        for x in permutations(inputted, s):
            yield x
        s = s[:-1]


def is_prime(n):

    """Checks whether a number is a prime."""

    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

permutationlist = list(permutations('987654321', ''))

for i in range(len(permutationlist)):
    permutationlist[i] = int(permutationlist[i])

