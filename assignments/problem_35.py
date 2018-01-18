#!/usr/bin/env python3

# Problem setting
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

def sieve(limit):

    """The sieve of Eratosthenes, which defines all primes below a certain number."""

    boolean = [True]*(limit - 1)
    numberlist = list(range(2, limit+1))

    start = 2

    while start ** 2 <= limit:
        for i in range(len(numberlist)):
            if numberlist[i] % start == 0 and numberlist[i] != start:
                boolean[i] = False
        start += 1

    primes = []

    for j in range(len(boolean)):
        if boolean[j]:
            primes.append(j + 2)

    return primes

def combinations(number):

    """Creates all possible combinations of a certain number."""

    stringNum = str(number)

    numList = []
    combinations = []

    for number in stringNum:
        numList.append(number)

    for i in range(len(numList)):
        needed = numList[-i:] + numList[:-i]
        new_num = int("".join(needed))
        combinations.append(new_num)

    return combinations


def circular(limit):

    """Check what primes below the limit are circular primes."""

    primelist = sieve(limit)
    circularPrimes = []

    for i in range(len(primelist)):

        percentage = ((i+1) / len(primelist)*100)
        print("Now %.2f of the computation completed." %(percentage))

        between = combinations(primelist[i])
        counted = 1
        checked = True
        while counted != len(between):
            for j in range(len(between)):
                if between[j] not in primelist:
                    checked = False
            counted += 1
        if checked:
            for k in range(len(between)):
                circularPrimes.append(between[k])

    result = set(circularPrimes)
    return len(result)


number = 1000000
result = circular(number)
print("There are", result, "circular primes below %d" % number)
