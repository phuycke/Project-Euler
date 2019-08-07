#!/usr/bin/env python3

# Problem setting
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

   21 22 23 24 25
   20  7  8  9 10
   19  6  1  2 11
   18  5  4  3 12
   17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def diagonals(numSides):

    maxval = (numSides) ** 2
    counter = 0

    values = []

    if numSides == 1:
        return [1]
    else:
        while counter < 4:
            result = maxval - (counter * (numSides - 1))
            values.append(result)
            counter += 1

        return values


def add(listedvals):

    """Returns the added values of all elements within a list."""

    if len(listedvals) == 1:
        return listedvals[0]
    else:
        sommation = 0
        for i in range(len(listedvals)):
            sommation = sommation + listedvals[i]

        return sommation


def sumOfDiagonals(sides):

    """Returns the added values on the diagonals of a sides x sides spiral."""

    allvals = []

    while sides > 0:
        between = diagonals(sides)
        result = add(between)
        allvals.append(result)
        sides -= 2

    return add(allvals)


def main():

    """Main function to get the program going. Asks the user to input the dimensions of the spiral."""

    dimension = int(input("Enter the dimension of the spiral we are looking at: "))
    result = sumOfDiagonals(dimension)
    print('The sum of the numbers on the diagonals in a', dimension, 'by', dimension, 'spiral is', result)


main()
