import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

(a < 0).sum()

# 2. How many positive numbers are there?
np.count_nonzero(a) - (a < 0).sum()

# 3. How many even positive numbers are there?
np.count_nonzero(a) - (a < 0).sum() - np.count_nonzero(a % 2 == 0)


If you were to add 3 to each data point, how many positive numbers would there be?

If you squared each number, what would the new mean and standard deviation be?

A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

Calculate the z-score for each data point. Recall that the z-score is given by: