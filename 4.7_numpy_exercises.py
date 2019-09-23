import numpy as np
# vectorization = applying an operation/function to every item in a vector/array (avoid loops)

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

mask = a < 0 
a[mask]

# a<0 gives list T/F, wrap in a[] will show value at numeric index (boolean mask - a filter)
#creates a new list (vectorized)


# 2. How many positive numbers are there?
np.count_nonzero(a) - (a < 0).sum()

# 3. How many even positive numbers are there?
even_numbers = a[a % 2 == 0]
pos_numbers = even_numbers[even_numbers > 0]
print(pos_numbers)

# alternative approach using 2 masks
is_pos_mask = a >0
pos = a[is_pos_mask]
is_even_mask = pos % 2 == 0
pos_evens = pos[is_even_mask]
pos_evens

#4. If you were to add 3 to each data point, how many positive numbers would there be?
num_plus_three = a + 3
pos_plus_three = num_plus_three[num_plus_three > 0]
count_pos_plus_three = np.count_nonzero(pos_plus_three)
print(count_pos_plus_three)

#shorter solution
add_three = a + 3
len(add_three[add_three > 0])

#5. If you squared each number, what would the new mean and standard deviation be?
num_squared = a ** 2
print(num_squared)
print(num_squared.mean())
print(num_squared.std())

# #6. A common statistical operation on a dataset is centering. This means to adjust the data 
# such that the center of the data is at 0. This is done by subtracting the mean from 
# each data point. Center the data set.
print(a.mean())
centered = a - a.mean()
print(centered)

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
z_score = centered/a.std()
print(z_score)

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a/len(a)
print(mean_of_a)


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a *= n
print(product_of_a)


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for n in a ** 2:
    squares_of_a.append(n)
print(squares_of_a)


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for n in a:
    if n % 2 !=0:
        odds_in_a.append(n)
print(odds_in_a)


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b =np.array([
    [3, 4, 5],
    [6, 7, 8]
])
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)

sum_of_b = np.sum(b) # sum will some each column, np.sum will sum the whole matrix
print(sum_of_b)



# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)

min_of_b = np.min(b)
print(min_of_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)

max_of_b = np.max(b)
print(max_of_b)



# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)

mean_of_b = np.mean(b)
print(mean_of_b)



# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(product_of_b)

product_of_b = np.prod(b)
print(product_of_b)



# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(squares_of_b) # prints matrix as a vector

squares_of_b = b ** 2
print(squares_of_b) # remains a matrix when printed


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(odds_in_b)

odds_in_b = b[b % 2 != 0]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# Exercise 9 - print out the shape of the array b.
array_shape = np.shape(b)
print(array_shape)



# Exercise 10 - transpose the array b.
b_transposed = np.transpose(b)
print(b_transposed)


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_reshaped = np.reshape(b,(1,6))
print(b_reshaped)




# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b_reshaped2 = np.reshape(b,(6,1))
print(b_reshaped2)



## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(c.min())
print(c.max())
print(c.sum())
print(c.prod())

# Exercise 2 - Determine the standard deviation of c.
print(c.std())



# Exercise 3 - Determine the variance of c.
print(c.var())


# Exercise 4 - Print out the shape of the array c
print(np.shape(c))


# Exercise 5 - Transpose c and print out transposed result.
c_transposed = np.transpose(c)
print(c_transposed)

# Exercise 6 - Multiply c by the c-Transposed and print the result.
print(c * c_transposed)


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(c + c_transposed)


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.prod(c*c_transposed))

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])
# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))


# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))



# Exercise 4 - Find all the negative numbers in d
print(d[d<0])

# Exercise 5 - Find all the positive numbers in d
print(d[d>0])


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)


# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))


# Exercise 8 - Print out the shape of d.
np.shape(d)


# Exercise 9 - Transpose and then print out the shape of d.
np.transpose(d)


# Exercise 10 - Reshape d into an array of 9 x 2

np.reshape(d,(2,9))