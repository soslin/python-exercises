#List comprehensions (first calculated as for loops, then as LCs)

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
characters_per_fruit = []
for fruit in fruits:
    cnt = len(fruit)
    characters_per_fruit.append(cnt)
print(characters_per_fruit)

characters_per_fruit = [len(fruit) for fruit in fruits ]
print(characters_per_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that 
# contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = []
for f in fruits:
    if 'a' in f:
        fruits_with_letter_a.append(f)
print(fruits_with_letter_a)

fruits_with_letter_a = [f for f in fruits if 'a' in f]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
numbers = [-5,-3,-4,-10,1,2,3,4,5,6,7,8,9,10,12,99,-34,101]

list_of_evens = []
for n in numbers:
    if n % 2 == 0:
        list_of_evens.append(n)
print(list_of_evens)

list_of_evens = [n for n in numbers if n % 2 == 0]
print(list_of_evens)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)
print(odd_numbers)

odd_numbers = [n for n in numbers if n % 2 != 0]
print(odd_numbers)


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
pos_nums = []
for n in numbers:
    if n >= 0:
        pos_nums.append(n)
print(pos_nums)

pos_nums = [n for n in numbers if n >= 0]
print(pos_nums)


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
neg_nums = []
for n in numbers:
    if n <= 0:
        neg_nums.append(n)
print(neg_nums)

neg_nums = [n for n in numbers if n <= 0]
print(neg_nums)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list 
# of numbers with 2 or more numerals

list_w_two_or_more_numerals = []
for n in numbers:
    if n > 9 or n <-9:
        list_w_two_or_more_numerals.append(n)
print(list_w_two_or_more_numerals)

list_w_two_or_more_numerals = [n for n in numbers if n > 9 or n < -9]
print(list_w_two_or_more_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list 
# with each element squared. Output is [4, 9, 16, etc...]
number_squared = []
for n in numbers: 
    print(n**2)

number_squared = [n**2 for n in numbers]
print(number_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers 
# that are both odd and negative.

odd_negative_numbers = []
for n in numbers:
    if n < 0 and n % 2!= 0:
        odd_negative_numbers.append(n)
print(odd_negative_numbers)

odd_negative_numbers = [n for n in numbers if n < 0 and n % 2!= 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing 
# each number plus five. 
numbers_plus_5 = []
for n in numbers:
    numbers_plus_5.append(n+5)
print(numbers_plus_5)

numbers_plus_5 = [n+5 for n in numbers]
print(numbers_plus_5)
