#!/usr/bin/env python3

# Problem setting
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def amicableNumbers(limit):
    """Returns a set of amicable numbers below the limit. All duplicates are filtered out, as well as [a,b] couples
    where a == b."""

    number = 1
    amicable = []

    while number < limit:

        divisors_1 = [1]
        for i in range(2, number):
            if number % i == 0:
                divisors_1.append(i)
        sum_1 = sum(divisors_1)

        divisors_2 = [1]
        for j in range(2, sum_1):
            if sum_1 % j == 0:
                divisors_2.append(j)
        sum_2 = sum(divisors_2)

        if number == sum_2 and number != sum_1:
            amicable.append(number)
            amicable.append(sum_1)

        number += 1

    return set(amicable)

between = amicableNumbers(10000)

globalsum = 0
for element in between:
    globalsum = globalsum + element

print("The set of amicable numbers is", between, "and there sum is: %d" %(globalsum))
