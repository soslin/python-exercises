#Conditional Basics

# a.prompt the user for a day of the week, print out whether the day is Monday or not

provide_day_of_week = input('What is the day of the week? ').capitalize().strip()
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if provide_day_of_week  == 'Monday':
    print('Today is Monday')
else:
    print('Today is not Monday')


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

provide_day_of_week = input('What is the day of the week? ').capitalize().strip()
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
week_end = ['Sunday', "Saturday"]
if provide_day_of_week in week_end:
    print('I love weekends!')
else:
    print('Weekdays mean work')


# c. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more 
# than 40 hours

hours_worked_this_week = int(input("How many hours did you work this week? "))
your_hourly_rate = float(input("What is your hourly rate? "))
overtime = hours_worked_this_week - 40
if overtime > 0:
    print(hours_worked_this_week*your_hourly_rate + (overtime*your_hourly_rate*1.5 - overtime*your_hourly_rate)
else:
    print(hours_worked_this_week*your_hourly_rate)



#2a. Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print (i)
    i +=1


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
while x < 101:
    print(x)
    x += 2

#Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x > -11:
    print(x)
    x -= 5

#Create a while loop that starts at 2, and displays the number squared on each line while 
#the number is less than 1,000,000
x = 2
while x < 1_000_000:
    print(x**2)
    x **=x

#Write a loop that uses print to create the output shown below.
x = 100
while x >0:
    print(x)
    x -= 5

# Write some code that prompts the user for a number, then shows a multiplication table up 
# through 10 for that number.
number_to_input = int(input("Pick a number between 1 and 10: "))
while True:
    if number_to_input.isdigit() == False:
        print('Read the directions and try again')
        break
    if number_to_input <= 0 or number_to_input > 10:
        print('Not a number between 1 and 10. Try again')
        break
    for i in range(1,11):
        print(i, ' x ' number_to_input, ' = ', number_to_input*i)
        
# Create a for loop that uses print to create the output shown below.
for i in range(10):
    print(str(i) * i)

# c. break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
# continue prompting the user if they enter invalid input. (Hint: use the isdigit method on 
# strings to determine this). Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.
    
prompt_odd_number = input('Provide an odd number between 1 and 50: ')
while True:
    if int(prompt_odd_number.isdigit()) == False:
        print('Read the directions and try again')
        continue
    if (int(prompt_odd_number <=0) or int(prompt_odd_number > 50)) and int(prompt_odd_number % 2 == 0):
        print('Not an odd number between 1 and 50. Try again')
        continue
if   


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a numeric type.)

enter_pos_number = input("Enter pos number: ")
while True:
    if int(enter_pos_number.isdigit()) == False or int(enter_pos_number) < 0:
        print('Read the directions and try again')
        continue
for n in range(0, int(enter_pos_number)):
    print(n)

# 3. Fizzbuzz
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1,101):
    if n % 15 == 0:
        print ("Fizzbuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 4. Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

prompt_for_integer = input('Enter an integer: ')
while True:
    if int(prompt_for_integer).isdigit() == False:
        print('Enter an INTEGER!')
    continue
for n in range(int(prompt_for_integer),1,-1)):
        print('Number', " | ", "Square", " | ", 'Cube')
        print('-----', '-----', '-----')
        print(int(prompt_for_integer), " | ", int(prompt_for_integer)**2, " | ", int(prompt_for_integer)**3  )


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue. 
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

number_to_letter_grade = input('Provide a numerical grade to get a letter grade: ')
grade_dict {'A' : '100 - 88',
"B" : "87 - 80",
"C" : "79 - 67",
"D" : "66 - 60",
"F" : "59 - 0"}
while True
if number_to_letter_grade in grade_dict[value]:
    print(grade_dict[key])
continue_prompt = input('Enter "Y" to continue or "N" to end: ').upper()
if continue_prompt != 'Y' or continue_prompt != 'N':
    print('Enter "Y" to continue or "N" to end')
    continue
if continue_prompt == 'Y':
    print('You are continuing.')
if continue_prompt == 'N':
    print('Terminating session.')


