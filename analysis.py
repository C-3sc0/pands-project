
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys



# read in the dataset from the UCI Machine Learning Repository link
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Define the names of the columns in the dataset
attribute_names = ['Sepal_Length (cm)','Sepal_Width (cm)','Petal_Length (cm)','Petal_Width (cm)','Class']
# Read in the Iris dataset using the pandas read_csv() method
iris = pd.read_csv(csv_url, names = attribute_names)

#directing print output to a txt file:https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
sys.stdout = open ("Analysis-summary.txt", "w")
print(f"Information about the Iris Data Set:\n")
print(iris.info(),"\n")
print("Overview of the Iris Data set:\n")
print(iris, "\n")
print("The first 10 rows of the Iris Data set:\n", iris.head(10), "\n")
print("The last 10 rows of the Iris data set:\n", iris.tail(10), "\n")
# Using the value_counts() method on the 'Class' column to show how many different class Iris flower can be found in the Data Set.
print("The Iris plants and their occurances are: \n")
print(iris["Class"].value_counts(), "\n")
print(f" The index of the Data Set is:\n", iris.index, "\n")
print(f"The Iris Data Set has {iris.ndim} dimensions\n")
print(f"The Iris data set has {iris.shape[0]} rows and {iris.shape[1]} columns\n")
print(f"The number of missing value in the Data set is: \n {iris.isnull().sum()}\n")
print(f"The statistical summary of the dataset is: \n\n{iris.describe()}\n")
sys.stdout.close()

#visualizing the class distribution of the iris data set into a countplot
sns.countplot(data=iris, x="Class", saturation= 0.5)
plt.title("Class Count")
plt.show()

#creating a histogram for all the Iris Data set attributes
iris.hist(alpha=0.5, bins=25, figsize=(10,6))
plt.suptitle("Histograms of Iris Dataset Features")
#plt.savefig("Iris-data-set-histogram")
plt.show()

#create a distplot for all the 4 attributes:
setosa = iris[iris.Class == "Iris-setosa"]
versicolor = iris[iris.Class == "Iris-versicolor"]
virginica = iris[iris.Class == "Iris-virginica"]

plt.figure(figsize=(8,6))
sns.distplot(setosa["Sepal_Length (cm)"],  kde = False, label = "Iris setosa")
sns.distplot(versicolor["Sepal_Length (cm)"],  kde = False, label = "Iris versicolor")
sns.distplot(virginica["Sepal_Length (cm)"],  kde = False, label = "Iris virginica")
plt.title("Sepal length in cm", size = 12)
plt.ylabel("Frequency", size = 9)
plt.legend()
#plt.savefig("Sepal-Length-distplot.png")
plt.show()

plt.figure(figsize=(8,6))
sns.distplot(setosa["Sepal_Width (cm)"],  kde = False, label = "Iris setosa")
sns.distplot(versicolor["Sepal_Width (cm)"],  kde = False, label = "Iris versicolor")
sns.distplot(virginica["Sepal_Width (cm)"],  kde = False, label = "Iris virginica")
plt.title("Sepal Width in cm", size = 12)
plt.ylabel("Frequency", size = 9)
plt.legend()
#plt.savefig("Sepal-Width-distplot.png")
plt.show()

plt.figure(figsize=(8,6))
sns.distplot(setosa["Petal_Length (cm)"],  kde = False, label = "Iris setosa")
sns.distplot(versicolor["Petal_Length (cm)"], kde = False, label = "Iris versicolor")
sns.distplot(virginica["Petal_Length (cm)"],  kde = False, label = "Iris virginica")
plt.title("Petal length in cm", size = 12)
plt.ylabel("Frequency", size = 9)
plt.legend()
#plt.savefig("Petal-Length-distplot.png")
plt.show()

plt.figure(figsize=(8,6))
sns.distplot(setosa["Petal_Width (cm)"],  kde = False, label = "Iris setosa")
sns.distplot(versicolor["Petal_Width (cm)"],  kde = False, label = "Iris versicolor")
sns.distplot(virginica["Petal_Width (cm)"],  kde = False, label = "Iris virginica")
plt.title("Petal Width in cm", size = 12)
plt.ylabel("Frequency", size = 9)
plt.legend()
#plt.savefig("Petal-Width-distplot.png")
plt.show()














