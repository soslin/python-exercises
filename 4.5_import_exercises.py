# 1. Import and test 3 of the functions from your functions exercise file.

# Your functions exercise are not currently in a file with a 
# name that can be easily imported. Copy your functions exercise 
# file and name the copy functions_exercises.py.

# Import each function in a different way:

# import the module and refer to the function with 
# the . syntax
# use from to import the function directly
# use from and give the function a different name

import function_exercises as f
f.accepts_string('hello')

from function_exercises import calculate_tip
print(calculate_tip(45,.18))

from function_exercises import apply_discount as disc
print (disc(3456,.07))




# How many different ways can you combine the letters from "abc" with the 
# numbers 1, 2, and 3?

from itertools import permutations

def permutations('abc123', r=3):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# How many different ways can you combine two of the letters from "abcd"?


