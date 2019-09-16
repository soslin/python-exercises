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
print(f.accepts_string('hello'))

from function_exercises import calculate_tip
print(calculate_tip(45,.18))

from function_exercises import apply_discount as disc
print (disc(3456,.07))




# How many different ways can you combine the letters from "abc" with the 
# numbers 1, 2, and 3?

from itertools import permutations
print(list(permutations(['a','b','c',1,2,3])))
print(len(list(permutations(['a','b','c',1,2,3]))))


# How many different ways can you combine two of the letters from "abcd"?

from itertools import combinations
print(list(combinations(['a','b','c','d'],2)))
print(len(list(combinations(['a','b','c','d'],2))))


from json import load
users = load(open('profiles.json', "r"))
print(users)

# Total number of users
user_count = 0
for user in users:
    user_count +=1
print(user_count)


# Number of active users
user_count = 0
for user in users:
    if user["isActive"] == True:
        user_count +=1
print(user_count)


# Number of inactive users
user_count = 0
for user in users:
    if user["isActive"] == False:
        user_count +=1
print(user_count)

# Grand total of balances for all users
user_balance = 0
for user in users:
    user_balance = float(user['balance'][1:].replace(",",""))

print(user_balance)




# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users
