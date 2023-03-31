
import pandas as pd

# read in the dataset from the UCI Machine Learning Repository link
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#adding the varible attribute_names as variable names in the UCI repository are lcated in a separate file
attribute_names = ['Sepal_Length (cm)','Sepal_Width (cm)','Petal_Length (cm)','Petal_Width (cm)','Class']
#with read_csv() we are reading the Iris dataframe and storing it in the iris varibale for further use and manipulation.

iris = pd.read_csv(csv_url, names = attribute_names)

#Look to the statistical data of the iris Data Set 
print(iris.describe())

# Using the value_counts() method on the 'Class' column to show how many different class Iris flower can be found in the Data Set.
print(iris["Class"].value_counts())










