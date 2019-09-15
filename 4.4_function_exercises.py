# 1. Define a function named is_two. It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise
def is_two(x):
    if x == 2 or x == '2': # alternate return x in [2,'2']
        return True
    else:
        return False
assert(is_two(2)) == True #only prints if false
assert(is_two("2")) == True
assert(is_two(3)) == False


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    vowels = ('aeiou')
    if letter.lower() in vowels:
        return True
    else:
        return False
assert(is_vowel('v')) == False
assert(is_vowel('a')) == True

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter):
    vowels = ('aeiou')
    if letter.lower() in vowels:
        return False
    else:
        return True
print(is_consonant('C'))
print(is_consonant('o'))
print(is_consonant('b'))


# 4.Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def accepts_string(word):
    vowels = ('aeiou')
    if word[0] not in vowels:
        return word[0].upper()+word[1:]
    else:
        return word
print(accepts_string('great'))
print(accepts_string('arabesque'))

# 5. Define a function named calculate_tip. It should accept a tip 
# percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(amount, tip):
    return amount + amount*tip
print(calculate_tip(45,.18))

# 6. Define a function named apply_discount. It should 
# accept a original price, and a discount percentage, and return the price after the discount is applied

def apply_discount(amount, discount):
    return amount - amount*discount
print(apply_discount(3456,.07))    

# 7. Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.

def handle_commas(amount):
    comma_free_amount = float(amount.replace(",",""))
    return comma_free_amount
print(handle_commas('1,232,591'))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
# associated with that number (A-F)
def get_letter_grade(letter):
    grades_dict = {4:"A", 3:"B", 2:"C", 1:"D", 0:"F"}
    grades = grades_dict[letter]
    return grades
print(get_letter_grade(3))

#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(text):
    vowels = ['a','e', 'i', 'o', 'u']
    for v in vowels:
        if v.lower() in text:
            text = text.replace(v,"")
    return text
print(remove_vowels("Mississippi"))

# 10.Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

def normalize_name(text):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYXabcdefghijklmnopqrstuvwxyz'
    numbers = [1,2,3,4,5,6,7,8,9,0]
    normalized_text = text.strip().lower().replace(" ","_"))
    return(normalized_text)
print(normalize_name('1Sean Oslin'))

def normalized_name(text):
    bad_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ',', ')', '.']
    numbers = [1,2,3,4,5,6,7,8,9,0]
    for b in bad_chars:
        if b in text:
            text.replace(b,'')
    return(text)
print(normalized_name('i!e$'))


#11.Write a function named cumsum that accepts a list of numbers and returns a list that 
# is the cumulative sum of the numbers in the list.

def cumsum(*args): #this is wrong, but gets the right answer
    nums_list = []
    sum_nums = 0
    for n in args:
        sum_nums += n
        nums_list.append(sum_nums)
    return nums_list
print(cumsum(1,1,1))

def cumsum(lst): 
    for n in range(1,len(lst)):
        lst[n] = lst[n] +lst[n-1]
    return lst
print(cumsum([1,1,1]))

str? #brings up documentation in command line and 
list('abcde')
"---".join(["a","b","c"])
"".join(["a","b","c"])