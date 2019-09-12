#List comprehensions
# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]

upper_cased_fruits = [fruit.upper() for fruit in fruits]



# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to 
# produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.


# fruits_with_more_than_two_vowels = []
# vowels = ['a','e','i','o','u']
# counter = 0
# for fruit in fruits:
#     for vowel in vowels:
#         num_vowels = vowels.count()
#     counter +=1
#     print(num_vowels)

# fruits_with_more_than_two_vowels = [fruit for fruit in aeiou.fruits() if count(fruit)> 2]




# 5. Make a list that contains each fruit with more than 5 characters :-)
fruits_w_more_than_5_characters = []
for fruit in fruits:
    if len(fruit) > 5:
        fruits_w_more_than_5_characters.append(fruit)
print(fruits_w_more_than_5_characters)

print([fruit for fruit in fruits if len(fruit) > 5])


# 6. make a list that contains each fruit with exactly 5 characters
fruits_w_exactly_5_characters = []
for fruit in fruits:
    if len(fruit) == 5:
        fruits_w_exactly_5_characters.append(fruit)
print(fruits_w_exactly_5_characters)

print([fruit for fruit in fruits if len(fruit) == 5])



#7. Make a list that contains fruits that have less than 5 characters
fruits_w_less_than_5_characters = []
for fruit in fruits:
    if len(fruit) < 5:
        fruits_w_less_than_5_characters.append(fruit)
print(fruits_w_less_than_5_characters)

print([fruit for fruit in fruits if len(fruit) > 5])


# 8. Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
# characters_per_fruit = []
# for fruit in fruits:
#     count(fruit)
# characters_per_fruit.append(fruit)



# 9. Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = []
