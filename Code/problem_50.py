#!/usr/bin/env python3

# Problem setting
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def SieveOfEratosthenes(n):

    """Returns all prime numbers below a certain limit."""

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes


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


def add(listed):

    """Add all elements in a list. Use in function instead of build in function 'sum()'."""

    return sum(listed)


def maxsum(limit):

    """Calculates the maximal sum of primes which also yields a prime number as a result"""

    primes = SieveOfEratosthenes(limit)

    start = 0

    largestrow = 2
    largestsum = 5

    while start < len(primes):
        sum = primes[start]
        test = [True]

        for j in range(start + 1, len(primes)):
            sum = sum + primes[j]
            if sum > limit:
                break
            else:
                if is_prime(sum):
                    test.append(True)
                else:
                    test.append(False)

        true_indices = [(x+(start + 1)) for x in range(len(test)) if test[x]]
        considered = primes[start:max(true_indices)]
        addition = add(considered)

        if len(considered) > largestrow and addition > largestsum:
            largestsum = addition
            largestrow = len(considered)

        start += 1

    return [largestrow, largestsum]


def main():

    """Main function to let the user decide the upper limit."""

    inputted_prime = int(input("Please enter the upper limit for which you want to calculate the largest prime that "
                               "can be represented as the sum of consecutive primes: "))
    result = maxsum(inputted_prime)
    print("The largest prime number under", inputted_prime,
          "that can be written as the sum of consecutive primes is", result[1],
          ", and this prime can be calculated by adding", result[0],
          "consecutive primes.")


main()
