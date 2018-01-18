#!/usr/bin/env python3

# Problem setting
"""
The number 3797 has an interesting property.

Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7.

Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def truncateleft(number):

    """Delete numbers from right to left."""

    numbers = []

    numbers.append(number)
    inputted = list(str(number))

    for j in range(len(inputted) - 1):
        del inputted[0]
        numbers.append(''.join(inputted))

    for k in range(len(numbers)):
        numbers[k] = int(numbers[k])

    return numbers


def truncateright(number):

    """Delete numbers from left to right."""

    numbers = []

    numbers.append(number)
    inputted = list(str(number))

    for j in range(len(inputted) - 1):
        inputted.pop()
        numbers.append(''.join(inputted))

    for k in range(len(numbers)):
        numbers[k] = int(numbers[k])

    return numbers


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


def truncatablePrimes(lower, upper):

    """A function to find whether a number is prime, and whether is still remains a prime after truncation from
    the right and the left."""

    tested = lower
    checked = []

    while tested < upper:

        test_left = truncateleft(tested)
        left_cleared = 1

        test_right = truncateright(tested)
        right_cleared = 1

        for i in range(len(test_left)):
            if not is_prime(test_left[i]):
                left_cleared = 0
                break
        for j in range(len(test_right)):
            if not is_prime(test_right[j]):
                right_cleared = 0
                break

        if left_cleared == 1 and right_cleared == 1:
            checked.append(tested)

        tested += 1

    return checked


lower = 10
upper = 1000000
result = truncatablePrimes(lower, upper)
print("The numbers we are looking for are:", result,
      ",and the sum of these numbers:", sum(result))
