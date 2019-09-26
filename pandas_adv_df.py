import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})

#There are several ways to create dataframes, we've already seen how we can create a dataframe from a dictionary:

pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

#The keys in the passed dictionary will be the column names, and the values are the data points that make up each column.


# sidebar: zip files together
a = ['a', 'b', 'c']
b = [1,2,3]
zip(a,b)


# what happens with out column heading data goes across and then down
pd.DataFrame([[1, 2, 3], [4, 5, 6]])

# .T transposes df


#  horizontal data with column headings
data = np.array([[1, 2, 3], [4, 5, 6]])

pd.DataFrame(data, columns=['a', 'b', 'c'])


# The most commonly used function to data from an external text file is read_csv. Two other commonly used functions are read_table, for less structured files that are still tabular, and read_json, for data stored as JSON.

# There are many other read_ functions, but read_csv will be the most commonly used one.

#We can use the read_sql method to create a dataframe based on the results of a SQL query. In order to connect to mysql, we'll install the mysqlclient and pymysql driver packages

# Example: mysql+pymysql://codeup:p@assw0rd@123.123.123.123/some_db

import pandas as pd
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'
df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
print(df)

#It is common to have longer SQL queries that we want to read into python, and an example of how we might break a query into several lines is below:

sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 5
OFFSET 200
'''

pd.read_sql(sql, url)
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})


#The .agg function lets us specify a way to aggregate a series of numerical values, and allows chaining.

df.info()
df.describe()
df.reading.agg('min')
df[['reading','math', 'english']].agg(['min', 'max', 'mean', 'median', 'var', 'std'])


#The .groupby method is used to created a grouped object, which we can then apply an aggregation on. For example, if we wanted to know the highest math grade from each classroom

df.groupby('classroom').math.min()

df.groupby('classroom').math.agg(['min','max','median'])


#We can group by multiple columns as well. To demonstrate, we'll create a boolean column named passing_math, then group by the combination of our new feature and the classroom, and calculate the average reading grade and number of individuals in each subgroup

(df
 .assign(passing_math=df.math.apply(lambda n: 'failing' if n < 70 else 'passing'))
 .groupby(['passing_math', 'classroom'])
 .reading # takes out the column headers: math, english and reading 
 .agg(['mean', 'count']))