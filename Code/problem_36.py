#!/usr/bin/env python3

# Problem setting
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def convertToBase(number, base):

    """Converts a number to a certain base."""

    baselist = []

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        while number > 1:
            baselist.append(number % base)
            number = number // base
            if number == 1:
                baselist.append(1)
                break

        result = baselist[::-1]
        base = ''.join(str(number) for number in result)

        return base


def palindrome(inputted):

    """Returns whether an input is a palindrome or not. Works with digits and strings."""

    converted = str(''.join(inputted))

    if converted == converted[::-1]:
        return True
    else:
        return False

def palindromesUpTo(limit, base):

    """Calculates the sum of all palindromic number under a certain limit."""

    palindromic = [1]
    number = 2

    while number < limit:

        binary = convertToBase(number, base)
        list_binar = list(binary)

        if list_binar[0] == '0' or list_binar[-1] == '0':
            pass
        else:
            num = str(number)
            if palindrome(list(num)) and palindrome(binary):
                palindromic.append(number)

        number += 1

    return palindromic


result = sum(palindromesUpTo(1000000, 2))
print("The solution to this problem is", result)
