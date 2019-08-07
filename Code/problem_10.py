#!/usr/bin/env python3

# Problem setting
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def SieveOfEratosthenes(n):
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

solution = SieveOfEratosthenes(2000000)
sum = sum(solution)
print("The solution to our problem is: %d" %(sum))


