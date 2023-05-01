
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def read_data(csv_url, attribute_names):
    #Read in the Iris dataset using the pandas read_csv() method
    iris = pd.read_csv(csv_url, names=attribute_names)
    #Create 3 new DataFrame for the Iris Class Attribute for further analysis
    setosa = iris[iris.Class == "Iris-setosa"]
    versicolor = iris[iris.Class == "Iris-versicolor"]
    virginica = iris[iris.Class == "Iris-virginica"]
    return iris, setosa, versicolor, virginica



#directing print output to a txt file:https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
def text_file(iris):
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
    print(f"\nThe summary statistic for Iris Setosa class are:\n {setosa.describe()}")
    print(f"\nThe summary statistic for Iris Versicolor class are:\n {versicolor.describe()}")
    print(f"\nThe summary statistic for Iris Virginica class are:\n {virginica.describe()}\n")
    sys.stdout.close()

#visualizing the class distribution of the iris data set into a countplot
def plot_class_distribution(iris):
    sns.countplot(data=iris, x="Class", saturation=0.5)
    plt.title("Class Count")
    plt.savefig("Class-Count.png")
    plt.show()

#creating a histogram for all the Iris Data set attributes
def plot_histograms(iris):
    iris.hist(alpha=0.5, bins=25, figsize=(10, 6))
    plt.suptitle("Histograms of Iris Dataset Features")
    plt.savefig("Iris-data-set-histogram")
    plt.show()

#create a 2x2 gris histplot to compare the 4 attributes:
def plot_histplot(iris):
    fig, ax = plt.subplots(2, 2, figsize=(10, 6))
    sns.histplot(data=iris, x="Sepal_Length (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax=ax[0, 0])
    sns.histplot(data=iris, x="Sepal_Width (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax=ax[0, 1])
    sns.histplot(data=iris, x="Petal_Length (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax=ax[1, 0])
    sns.histplot(data=iris, x="Petal_Width (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax=ax[1, 1])
    fig.suptitle("Comparision of Sepal & Petal attributes between the 3 Iris flowers", size=20)
    plt.savefig("histograms-for-comparison-of-the-4-attribute.png")
    plt.show()

#Create a Scatter plot for for Sepal and Petal Attributes:
def sepal_scatter(iris):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(y=iris["Sepal_Width (cm)"], x=iris["Sepal_Length (cm)"], hue=iris["Class"], s=50)
    plt.title("Comparison of Sepal Sizes Across Iris Species")
    plt.savefig("Iris-Sepal-attribute-scatterplot.png")
    plt.show()

def petal_scatter(iris):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(y=iris["Petal_Width (cm)"], x=iris["Petal_Length (cm)"], hue=iris["Class"], s=50)
    plt.title("Comparison of Petal Sizes Across Iris Species")
    plt.savefig("Iris-Petal-attribute-scatterplot.png")
    plt.show()


#Creating a Violinplot:
def violin_plot(iris):
    fig, ax = plt.subplots(2,2, figsize=(16,9))
    font = {"family" : "Lucida Handwriting", "color" : "Blue", "size" : 15}
    sns.violinplot( x= iris["Class"], y= iris["Sepal_Length (cm)"], data= iris,  ax= ax[0,0])
    sns.violinplot( x= iris["Class"], y= iris["Sepal_Width (cm)"], data= iris, ax= ax[0,1])
    sns.violinplot( x= iris["Class"], y= iris["Petal_Length (cm)"], data= iris,  ax= ax[1,0])
    sns.violinplot( x= iris["Class"], y= iris["Petal_Width (cm)"], data= iris,  ax= ax[1,1])
    fig.suptitle("Violinplot of Iris Sepal & Petal attributes", size=20, fontdict=font)
    plt.savefig("Violinlot-of-Iris-Data-Set.png")
    plt.show()

#create a pairplot:
def pair_plot(iris):
    sns.pairplot(iris, hue= "Class")
    plt.savefig("Iris-data-set-pairplot.png")
    plt.show()

#Read in the dataset from the UCI Machine Learning Repository link
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#Define the names of the columns in the dataset
attribute_names = ['Sepal_Length (cm)', 'Sepal_Width (cm)', 'Petal_Length (cm)', 'Petal_Width (cm)', 'Class']
iris, setosa, versicolor, virginica = read_data(csv_url, attribute_names)

text_file(iris)
plot_class_distribution(iris)
plot_histograms(iris)
plot_histplot(iris)
sepal_scatter(iris)
petal_scatter(iris)
violin_plot(iris)
pair_plot(iris)