#!/usr/bin/env python3

# Problem setting
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def createChampernowne(length):


    decimals = list(range(1, 10))

    for index in range(len(decimals)):
        decimals[index] = str(decimals[index])

    number = 10
    unchecked = True

    while len(decimals) < length + 1 and unchecked:
        listed = list(str(number))
        for i in range(len(listed)):
            checking = len(decimals)
            if checking > length:
                unchecked = False
                break
            else:
                decimals.append(listed[i])
        number += 1

    return decimals


def findValues(inputlist, listed):

    if len(listed) == 0:
        raise IndexError("The list you provided is empty...")
    else:
        values = []
        for j in range(len(listed)):
            index = listed[j]
            values.append(int(inputlist[index - 1]))
        return values


needed = createChampernowne(1000000)
result = findValues(needed, [1, 10, 100, 1000, 10000, 100000, 1000000])
product = result[0]
for i in range(1, len(result)):
    product = product * result[i]

print("The numbers we selected are:")
print(result)
print("The product of these numbers is", product)
