#!/usr/bin/env python3

# Problem setting
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatzChain(number):
    """Runs a Collatz sequence, and returns the number of loops completed before reaching 1."""

    loops = 1

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        loops += 1

    return loops

def collatzLoop(limit):
    """Loops the Collatz sequence from every value ranging from 1 up to the specified limit. Returns the input
    for which the longest Collatz sequence was generated."""

    longest = 1
    collatznumber = 1

    for i in range(1, limit):
        looped = collatzChain(i)
        if looped > longest:
            longest = looped
            collatznumber = i

    answer = [collatznumber, looped]
    return answer

solution = collatzLoop(1000000)
print("The number", solution[0], "has the longest Collatz sequence for all number under the specified limit.")