#!/usr/bin/env python3

# Problem setting
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""


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


def largestPandigitalPrime(digits):

    """Delivers the largest prime that is pandigital."""

    checked = []
    for i in range(1, digits + 1):
        checked.append(str(i))

    inputted = str(''.join(checked))
    checkedlist = list(permutations(inputted, ''))

    largestvalue = 0

    for j in range(len(checkedlist)):
        checkedlist[j] = int(checkedlist[j])
        if is_prime(checkedlist[j]) and checkedlist[j] > largestvalue:
            largestvalue = checkedlist[j]

    return largestvalue


def main():

    """Main function to get the program started."""

    reference = int(input('Enter the maximum amount of digits the prime is allowed to have (between 4 and 9): '))
    if reference >= 10 or reference <= 3:
        raise ValueError("The inputted value must be between 4 and 9 (both included).")

    while True:
        result = largestPandigitalPrime(reference)
        if result == 0:
            reference -= 1
            largestPandigitalPrime(reference)
        else:
            break

    print("The largest pandigital prime with", reference,
          "digits is:", result)


main()
