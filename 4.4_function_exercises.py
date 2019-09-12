# 1. Define a function named is_two. It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    vowels = ('aeiou')
    if letter.lower() in vowels:
        return True
    else:
        return False

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter):
    vowels = ('aeiou')
    if letter.lower() in vowels:
        return False
    else:
        return True


# Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def accepts_string(word):
    vowels = ('aeiou')
    if word[0] not in vowels:
        return word[0].upper()+word[1:]

# Define a function named calculate_tip. It should accept a tip 
# percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(amount):
    bill_total = 0
    
