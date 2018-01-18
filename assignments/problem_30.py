#!/usr/bin/env python3

# Problem setting
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_n_powers(power):

    number = 2
    found = []

    while number <= (9*9**power):
        check = str(number)
        digits = []

        for digit in check:
            digits.append(int(digit))

        sum = int(digits[0]) ** power
        for i in range(1, len(digits)):
            sum = sum + int(digits[i])**power

        if int(sum) == number:
            found.append(number)

        number += 1

    sum = 0
    for i in range(len(found)):
        sum = sum + found[i]

    return sum

print(sum_of_n_powers(5))
