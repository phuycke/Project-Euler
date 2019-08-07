#!/usr/bin/env python3

#%%

# --------------- #
# Problem setting #
# --------------- #

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the 
numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""

#%%

from fractions import Fraction

#%%

def disjoint(num1, num2):
  
    a = list(str(num1))                         # make it a list
    b = list(str(num2))                         # make it a list

    common = list(set(a).intersection(b))       # check common elements
    
    if len(common) == 0:
        return True, 0                          # if no commons: return 
    else:    
        a.remove(common[0])
        b.remove(common[0])
        
        if int(b[0]) == 0:
            return True, 0                      # if commons but b == 0, return
        else:
            return False, int(a[0]) / int(b[0]) # return
    
#%%
            
nominator   = 1
denominator = 1

for i in range(10, 100):
    for j in range(10, 100):
        if (i % 10 == 0) and (j % 10 == 0):
            pass         # ignore the trivial cases, like 30/50
        elif i > j:
            continue     # ignore the cases where a / b > 1
        elif i == j:
            pass
        else:
            nothing_shared, fraction = disjoint(i, j)
            if nothing_shared:
                pass     # ignore if there is no common element
            else:
                if fraction == (i / j):
                    print("Digit cancelling fraction: {0}/{1}".format(i, j))
                    nominator   = nominator * i
                    denominator = denominator * j

# print the end fraction, and simplify it
end_frac = Fraction('{0}/{1}'.format(nominator, denominator))
print("\nFinal fraction (simplified): {}".format(end_frac))
print("Denominator: {}".format(end_frac.denominator))
