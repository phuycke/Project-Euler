#!/usr/bin/env python3

# Problem setting
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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


def findnumber(lowerbound, upperbound, difference):

    """
    Find all primes for which the difference between the primes is specified.
    All elements are primes, and are permutations of one another.
    """

    start = lowerbound
    results = []

    while start < upperbound:
        if is_prime(start):
            holding = True
            for number in range(1,3):
                tested = start + (difference * number)
                if not is_prime(tested):
                    holding = False
            if holding:
                if start < upperbound and start + difference < upperbound and start + difference*2 < upperbound:
                    results.append([start, start + difference, start + difference*2])
        start += 1

    considered = []

    for j in range(len(results)):

        reference = list(str(results[j][0]))
        reference.sort()

        second = list(str(results[j][1]))
        second.sort()

        third = list(str(results[j][2]))
        third.sort()

        if ''.join(reference) == ''.join(second) == ''.join(third):
            considered.append([results[j][0], results[j][1], results[j][2]])

    return considered


lower = 1000
upper = 10000
diff = 3330

results = findnumber(lower, upper, diff)

print("There are", len(results), "possible solutions to this problem.")
print("These are the primes and their permutations that are also primes.\n"
      "The difference between all the primes is", diff, ".")
for i in range(len(results)):
    print(results[i])
