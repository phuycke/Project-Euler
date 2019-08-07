#!/usr/bin/env python3

# Problem setting
"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

# The way to generate the next higher permutation were adopted from the following website:
    # https://www.geeksforgeeks.org/lexicographic-permutations-of-string/

def permute(inputted, permutationnumber):
    """This functions permutes an input until the result of the permutation process equals the reverse of the
    inputted string. The permutations process stops after n cycles, and returns the last permutation."""

    try:
        [int(element) for element in inputted]
    except:
        raise ValueError("All elements in your input must be integers.")

    permutations = []
    permutations.append(inputted)

    unsatisfied = True
    while unsatisfied:

        previousPermute = permutations[-1]
        firstCharacter = 0
        for i in range(len(previousPermute)-1,-1,-1):
            if int(previousPermute[i-1]) < int(previousPermute[i]):
                firstCharacter = previousPermute[i-1]
                break

        ceiling = 90000
        subset = list(previousPermute[previousPermute.index(firstCharacter)+1: ])
        if len(subset) == 1:
            ceiling = subset[0]
        elif len(subset) == 0:
            continue
        else:
            for i in range(len(subset) - 1, -1, -1):
                if int(subset[i]) < ceiling and int(subset[i]) > int(firstCharacter):
                    ceiling = int(subset[i])

        transformed_list = list(previousPermute)

        firstCharacter_index = transformed_list.index(str(firstCharacter))
        ceiling_index = transformed_list.index(str(ceiling))

        transformed_list[firstCharacter_index] = ceiling
        transformed_list[ceiling_index] = firstCharacter

        toBePassed = transformed_list[:firstCharacter_index + 1]

        toBeSorted = transformed_list[firstCharacter_index + 1:]
        toBeSorted.sort()
        
        for i in range(len(toBeSorted)):
            toBePassed.append(toBeSorted[i])

        for i in range(len(toBePassed)):
            toBePassed[i] = str(toBePassed[i])

        result = "".join(toBePassed)
        permutations.append(result)

        if len(permutations) == permutationnumber:
            return permutations[-1]

        if result == inputted[::-1]:
            break

    return permutations

solution = permute('0123456789', 1000000)
print("After 1000000 permutations, the inputted string looks like this: %s" %(solution))