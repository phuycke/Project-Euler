#!/usr/bin/env python3

# Problem setting
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

def number2text(integer):
    """Returns the written form of an inputted integer. The number can be inputted in integer form."""

    numbers_1_20_char = ["one", "two", "three", "four", "five",
                         "six", "seven", "eight", "nine", "ten",
                         "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                         "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

    numbers_21_99_int = list(range(20, 100, 10))
    numbers_21_99_char = ["twenty", "thirty", "forty", "fifty",
                          "sixty", "seventy", "eighty", "ninety"]

    numbers_100_999_int = list(range(100,1000,100))
    numbers_100_999_char = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred",
                            "six hundred", "seven hundred", "eight hundred", "nine hundred"]

    number_1000_int = 1000
    number_1000_char = "one thousand"

    if integer <= 0:
        raise ValueError("The number must be higher than 0, and smaller than 1001")
    elif 1 <= integer <= 19:
        word = numbers_1_20_char[integer - 1]
    elif 20 <= integer <= 99:
        if integer in numbers_21_99_int:
            word = numbers_21_99_char[int(integer/10) - 2]
        else:
            inBetween = list(str(integer))
            lastword = numbers_1_20_char[int(inBetween[1]) - 1]
            firstword = numbers_21_99_char[int(int(inBetween[0])) - 2]
            word = "".join([firstword, lastword])
    elif 100 <= integer <= 999:
        if integer in numbers_100_999_int:
            word = numbers_100_999_char[int(integer/100) - 1]
        else:
            inBetween = list(str(integer))
            firstword = numbers_100_999_char[int(integer / 100) - 1]
            if int(inBetween[2]) == 0:
                if int(inBetween[1]) == 1:
                    word = "".join([firstword, "and", "ten"])
                else:
                    secondword = numbers_21_99_char[int(int(inBetween[1])) - 2]
                    word = "".join([firstword, "and", secondword])
            else:
                number = (int(inBetween[1])*10) + int(inBetween[2])
                if 1 <= number <= 20:
                    secondword = numbers_1_20_char[number - 1]
                    word = "".join([firstword, "and", secondword])
                else:
                    secondword = numbers_21_99_char[int(int(inBetween[1])) - 2]
                    thirdword = numbers_1_20_char[int(int(inBetween[2])) - 1]
                    word = "".join([firstword, "and", secondword, thirdword])
    elif integer == number_1000_int:
        word = number_1000_char

    return word

def countLetters(inputtedString):
    """Returns the amount of letters in a certain string, only counts letters, no spaces or other characters."""

    counted = 0
    inBetween = list(inputtedString)
    i = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while i < len(inBetween):
        if inBetween[i] in alphabet:
            counted += 1
        i += 1

    return counted

def numberCounts(limit):
    """Counts how many letters there are in a certain word, and sums the total amount of letters needed to print
    all the considered numbers in words."""

    sum = 0
    for number in range(1,limit+1):
        word = number2text(number)
        amount = countLetters(word)
        sum = sum + amount
    return sum

solution = numberCounts(1000)
print("The print all the numbers in text, a total of %d letters is needed." %(solution))
