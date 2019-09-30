# Use the iris database to answer the following quesitons:


# Which features would be best used to predict species?

import pandas as pd
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
df = pd.read_sql('SELECT * FROM measurements', url)
print(df)


import seaborn as sns
import matplotlib.pyplot as plt

# What does the distribution of petal lengths look like?
sns.distplot(df.petal_length)


# Is there a correlation between petal length and petal width?
sns.relplot(x = "petal_length", y = "petal_width", data = df)


# Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(x = "sepal_length", y = "sepal_width", data = df)


# Which features would be best used to predict species?
sns.pairplot(df)
df.corr()


# use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?

anscombe = sns.load_dataset('anscombe')
anscombe.head() # see all the data.head()
anscombe.dtypes

anscombe.info()

anscombe[['x', 'y']].agg(['min', 'max', 'median', 'mean', 'std', 'var'])
anscombe.groupby('dataset').describe()

#Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

sns.relplot(x = "x", y = "y", data = anscombe, col = 'dataset')

# Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.
from pydataset import data
insect_sprays = data('InsectSprays')
data("InsectSprays", show_doc = True) #show documentation

insect_sprays #show all data
insect_sprays.groupby('spray').describe() # show all data grouped by spray


plt.figure(figsize = (12,10))
sns.boxplot(data = insect_sprays, y = 'count', x = 'spray')
plt.title('Effectiveness of insect sprays')


# Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:

swiss = data('swiss')
data("swiss", show_doc = True)
swiss.describe()
swiss.head(15)

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. 
swiss['is_catholic'] = np.where(swiss['Catholic'] > 66, True, False)
swiss.head(10)


# Does whether or not a province is Catholic influence fertility?
swiss.corr() #r = .605, yes, but lack of education is even higher

sns.relplot(x = "Catholic", y = "Fertility", data = swiss)

plt.figure(figsize = (12,10))
sns.boxplot(data = swiss, y = 'Fertility', x = 'is_catholic')


# What measure correlates most strongly with fertility? - education (negatively correlated)
sns.relplot(x = "Education", y = "Fertility", data = swiss)



#Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

def git_db_url():
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    return url
url=git_db_url()
chipotle = pd.read_sql('SELECT * FROM orders', url)
chipotle.head(0)

chipotle['item_price'] = chipotle['item_price'].replace('[\$,)]', '', regex = True).astype(float)

four_most_popular_items = chipotle.groupby('item_name').agg({'quantity': 'count', 'item_price': 'sum'}).sort_values('quantity', ascending = False).head(4)
print(four_most_popular_items)





