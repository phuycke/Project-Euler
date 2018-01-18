#!/usr/bin/env python3

# Problem setting
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
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


def checkProperty(inputted):

    transform = list(inputted)

    one = int(''.join(transform[1:4]))
    two = int(''.join(transform[2:5]))
    three = int(''.join(transform[3:6]))
    four = int(''.join(transform[4:7]))
    five = int(''.join(transform[5:8]))
    six = int(''.join(transform[6:9]))
    seven = int(''.join(transform[7:10]))

    if one % 2 == 0 and two % 3 == 0 and three % 5 == 0 and \
            four % 7 == 0 and five % 11 == 0 and six % 13 == 0 and seven % 17 == 0:
        return True
    else:
        return False


def findnumbers(digits):

    checked = []
    for i in range(0, digits + 1):
        checked.append(str(i))

    inputted = str(''.join(checked))
    checkedlist = list(permutations(inputted, ''))

    results = []

    for i in range(len(checkedlist)):
        if checkProperty(checkedlist[i]):
            results.append(int(checkedlist[i]))

    return results


def main():

    """Main function to get started. User specifies the largest number that can be found in the digit string."""

    digits = int(input("Define the largest number you want to have in your digit string (with input <= 9): "))
    needed = findnumbers(digits)
    sumofall = sum(needed)

    print("All the numbers that comply to the specified rule:")
    print(needed)
    print("The sum of all these numbers:", sumofall)


main()
