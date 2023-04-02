
import pandas as pd
import numpy as np


# read in the dataset from the UCI Machine Learning Repository link
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Define the names of the columns in the dataset
attribute_names = ['Sepal_Length (cm)','Sepal_Width (cm)','Petal_Length (cm)','Petal_Width (cm)','Class']
# Read in the Iris dataset using the pandas read_csv() method
iris = pd.read_csv(csv_url, names = attribute_names)

# Display the statistical summary of the dataset using the describe() method 
print(f"Statistical summary of the dataset: \n{iris.describe()}")

# Display the index of the Iris Data Set
print(f" The index of the Data Set is: ", iris.index)

# Using the value_counts() method on the 'Class' column to show how many different class Iris flower can be found in the Data Set.
print("The Iris plant are: \n")
print(iris["Class"].value_counts())

# Display the number of dimensions in the dataset using the ndim attribute.
print(f"The Iris Data Set has {iris.ndim} dimensions")

# Display the number of rows and columns in the dataset using the shape attribute
print(f"The Iris data set has {iris.shape[0]} rows and {iris.shape[1]} columns")

# Check for any missing values in the dataset using the isnull() and sum() methods
print(f"the number of missing value in the Data set is: \n{iris.isnull().sum()}")

# Display information about the dataset using the info() method
print(f"Information about the Iris Data Set:")
print(iris.info())





