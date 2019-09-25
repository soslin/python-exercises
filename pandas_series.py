#Use pandas to create a Series from the following data:
import pandas as pd


# Name the variable that holds the series fruits.
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
"tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", 
"blackberry", "gooseberry", "papaya"]

fruits = pd.Series(fruits)



#Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()



#Run the code necessary to produce only the unique fruit names.
fruits.unique()


#Determine how many times each value occurs in the series.
fruits.value_counts()


#Determine the most frequently occurring fruit name from the series.
frequencies = fruits.value_counts()
frequencies


#Determine the least frequently occurring fruit name from the series.


    #How would I get back all the fruit with the same min value?


#Write the code to get the longest string from the fruits series.
fruits[fruits.str.len().idxmax()]
fruits[fruits.str.len().idxmin()]

#Find the fruit(s) with 5 or more letters in the name.
fruits[fruits.str.len()>4]


#Capitalize all the fruit strings in the series.
fruits.str.capitalize()

#Count the letter "a" in all the fruits (use string vectorization)

def count_of_a(word):
    return len([w for w in word if w == 'a'])
count_of_a('pineapple')
fruits.apply(count_of_a)

fruits.str.count('a')

#Output the number of vowels in each and every fruit.
def count_of_a(word):
    return len([w for w in word if w in 'aeiou'])
count_of_a('pineapple')
fruits.apply(count_of_a)

#Use the .apply method and a lambda function to find the fruit(s) containing two or 
#more "o" letters in the name.

words_with_double_o = fruits[fruits.apply(lambda x: x.count('o') >= 2)]
print(words_with_double_o)

#Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.contains('berry')


#Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.contains('apple')]

#Which fruit has the highest amount of vowels?
fruits.str.apply(count_of_a).idxmax()



#Use pandas to create a Series from the following data:


amounts = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', 
'$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', 
'$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', 
'$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
amounts = pd.Series(amounts)

amounts = amounts.str.replace('$','')
amounts = amounts.str.replace(',','')
amounts

#What is the data type of the series?
type(amounts)

#Use series operations to convert the series to a numeric data type.
pd.to_numeric(amounts)


What is the maximum value? The minimum?
amounts.max()
amounts.min()

amounts.describe

Bin the data into 4 equally sized intervals and show how many values fall into each bin.
Plot a histogram of the data. Be sure to include a title and axis labels.

pd.cut(amounts,4)




# Use pandas to create a Series from the following exam scores:


scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
scores = pd.Series(scores)

#What is the minimum exam score? The max, mean, median?
print(scores.max())
print(scores.mean())
print(scores.median())

#Plot a histogram of the scores.

import matplotlib.pyplot as plt
scores.plot.hist()




#3. Use pandas to create a Series from the following exam scores:
grades = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
grades = pd.Series(grades)

#What is the minimum exam score? The max, mean, median?
print(grades.max())
print(grades.min())
print(grades.mean())
print(grades.median())

#Plot a histogram of the scores.
grades.plot.hist()

Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' 
and 95 should be an 'A'.

def letter_grades(grades):
    for n in grades:
        if n >= 90:
            return 'A'
        elif n >= 80:
            return 'B'
        elif n >= 70:
            return 'C'
        elif n >= 60:
            return 'D'
        else:
            return 'F'
letter_grades(n)







Write the code necessary to implement a curve. I.e. that grade closest to 100 should be 
converted to a 100, and that many points should be given to every other score as well.