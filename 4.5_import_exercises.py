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

print(list(permutations(["a","b","c", 1,2,3])))
print(len(list(permutations(["a","b","c", 1,2,3]))))


# How many different ways can you combine two of the letters from "abcd"?

from itertools import combinations
print(list(combinations(['a','b','c','d'],2)))
print(len(list(combinations(['a','b','c','d'],2))))


from json import load
users = load(open('profiles.json', "r"))
print(users)

type(users)
type(users[0])
print(users[0]['friends'][1]['name'])



# Total number of users
user_count = 0
for user in users:
    user_count +=1
print(user_count)

user_count = len([user for user in users])
print(user_count)

# Number of active users
user_count = 0
for user in users:
    if user["isActive"] == True:
        user_count +=1
print(user_count)

user_count = len([user for user in users if user ["isActive"] == True])
print(user_count)

# Number of inactive users
user_count = 0
for user in users:
    if user["isActive"] == False:
        user_count +=1
print(user_count)

user_count = len([user for user in users if user ["isActive"] == False])
print(user_count)


# Grand total of balances for all users

user_balance = sum([float(user['balance'][1:].replace(",","")) for user in users])
print(user_balance)

# Average balance per user
user_balance = (sum([float(user['balance'][1:].replace(",","")) for user in users]))/len(users)
print(user_balance)

# User with the lowest balance
user_balance = min([float(user['balance'][1:].replace(",","")) for user in users])
print(user_balance)

# User with the highest balance
user_balance = max([float(user['balance'][1:].replace(",","")) for user in users])
print(user_balance)

# Most common favorite fruit
most_favorite_fruit = max([user['favoriteFruit'] for user in users])
print(most_favorite_fruit)

for user in user:
    fruit = user['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

# Least most common favorite fruit
most_favorite_fruit = min([user['favoriteFruit'] for user in users])
print(most_favorite_fruit)

# Total number of unread messages for all users
total_unread_messages = [''.join(user['greeting']) for user in users if user['greeting'].isdigit()]
print(total_unread_messages)

greetings = [extract_digits(user['greeting']) for user in users]
print(greetings)

