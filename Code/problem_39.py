

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
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


def dickson(number):

    r = number
    r_squared = ((r ** 2) // 2)

    divisors = []
    starter = 1

    while starter < (r_squared // 2):
        if r_squared % starter == 0:
            if starter not in divisors:
                divisors.append(starter)
            if r_squared // starter not in divisors:
                divisors.append(r_squared // starter)
        starter += 1

    index = 0
    solutions = []

    while index < len(divisors):

        r = number
        s = divisors[index]
        t = divisors[index + 1]

        x = r + s
        y = r + t
        z = r + s + t

        solutions.append([x, y, z])

        index += 2

    return solutions[::-1]


def add(listedvals):

    """Returns the added values of all elements within a list."""

    if len(listedvals) == 1:
        return listedvals[0]
    else:
        sommation = 0
        for i in range(len(listedvals)):
            sommation = sommation + listedvals[i]

        return sommation


def maximalSolution(limit):

    number = 2
    perimeters = [0] * limit
    scanning = True

    while scanning:
        needed = dickson(number)
        if len(needed) > 0:
            firstelement = add(needed[0])
            if firstelement > limit:
                scanning = False
            else:
                for j in range(len(needed)):
                    sums = add(needed[j])
                    if sums <= limit:
                        perimeters[sums - 1] = perimeters[sums - 1] + 1
        number += 2

    needed = perimeters.index(max(perimeters)) + 1
    return needed


def main():

    """Main function to get everything going. Also, the user is asked to define the upper limit of p."""

    inputted = int(input("Please specify the upper limit for p? (p <= x): "))
    result = maximalSolution(inputted + 1)
    print("The value for which p ≤", inputted, ", and where the number of solutions is maximised is:", result)


main()
