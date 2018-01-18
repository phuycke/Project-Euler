#!/usr/bin/env python3

# Problem setting
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv

def processNames(fileName):
    """Read the names from the name files provided by problem 22. Returns the list alphabetically sorted."""

    characterlist = []

    with open(fileName, 'r') as f:
        reader = csv.reader(f, dialect = 'excel', delimiter = ',')
        for row in reader:
            characterlist.append(row)
    characterlist = characterlist[0]

    return sorted(characterlist)

def letterValue(word):
    """Compute the value of a word based on the letters. Add the position in the alphabet together for all letters.
    Using this method, A would have a value of 1, B of two ..."""

    letters = "abcdefghijklmnopqrstuvwxyz"
    letterlist = list(letters)

    values = []
    [values.append(letterlist.index(element)+1) for element in word.lower()]

    return sum(values)

def nameScore(namelist):
    """Compute the entire name score by multiplying the sum of the letter values with the index of the entire
    word in the list. Notice that the list starts at position 1, and not at 0 like usual."""

    value = []
    for word in namelist:
        val = letterValue(word)
        val = val * (namelist.index(word) + 1)
        value.append(val)

    return sum(value)

names = processNames("names_22.txt")
solution = nameScore(names)
print("The sum of the name scores for all the names in the list is: %d" %(solution))