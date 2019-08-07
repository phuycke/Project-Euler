#!/usr/bin/env python3

# Problem setting
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.

For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""


from string import ascii_lowercase
import os


def alphabet_position(text):

    """Returns the numeric position in the alphabet for each letter in the word."""

    text = text.lower()

    characters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
    numbers = [characters[character] for character in text if character in characters]

    solution = []
    [solution.append(int(nums)) for nums in numbers]

    return solution


def add(listedvals):

    """Returns the added values of all elements within a list."""

    if len(listedvals) == 1:
        return listedvals[0]
    else:
        sommation = 0
        for i in range(len(listedvals)):
            sommation = sommation + listedvals[i]

        return sommation


def checkTriangle(number):

    found = False
    n = 1

    if number == 1:
        return True
    else:
        while not found and n != number:
            triangle = .5 * n*(n + 1)
            if triangle == number:
                found = True
            n += 1

        return found


def readlist():

    """
    Reads the words from an external text file. User inputs the home folder of the document, along with the
    document name.
    """

    homedir = str(input("Please copy-paste the path to the word file: "))
    homedir.replace('\\', '/')

    docname = str(input("Please specify the name of document: "))

    os.chdir(homedir)
    file = homedir + "\\" + docname

    with open(file) as f:
        wordlist = []
        for line in f:
            [wordlist.append(x.strip()) for x in line.split(',')]

    for j in range(len(wordlist)):
        wordlist[j] = wordlist[j].replace('"', '')

    return wordlist


def countTriangleWords():

    wordlist = readlist()
    counted = 0

    for j in range(len(wordlist)):
        word = wordlist[j]
        num = alphabet_position(word)
        considered = add(num)
        if checkTriangle(considered):
            counted += 1

    return counted


solution = countTriangleWords()
print("In the inputted word file, there were", solution, "'triangle words'.")
