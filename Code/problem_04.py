#!/usr/bin/env python3

# Problem setting
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindromeChecker(integer):
    """Checks whether a certain number is a palindrome."""

    checked = str(integer)
    reverseChecked = checked[::-1]
    equal = True
    index = 0
    while equal and index < len(checked):
        if checked[index] != reverseChecked[index]:
            equal = False
        index += 1
    return equal

def palindromeSeeker(digits):
    """Finds the product of all n digit numbers, and returns the largest product of the two that is a palindrome."""

    maxNumber = 121
    products = [11, 11]
    for prod_one in range(10 ** digits):
        for prod_two in range(10 ** digits):
            product = prod_one * prod_two
            if palindromeChecker(product) and product > maxNumber:
                maxNumber = product
                products = [prod_one, prod_two]

    print(products)
    return maxNumber

print(palindromeSeeker(3))


