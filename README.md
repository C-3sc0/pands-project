# pands-project

-------
This repository is used for the final project given during the Programming and scripting module on Higher Diploma in Data Analytics course from ATU university. Topic of the project is research and investigation of Fisher's Iris data set.

## Table of Contents

* [Fisher's Iris Data set information](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-information)
  * [Fisher's Iris Data set History](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-history)
* [Data set code and Analysis](https://github.com/C-3sc0/pands-project#data-set-code-and-analysis)
  * [Fisher's Iris Data set file](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-file)
  * [Data Dimension](https://github.com/C-3sc0/pands-project#data-dimension)
  * [Importing the data](https://github.com/C-3sc0/pands-project#importing-the-data)
  * [Iris Data Insight Extraction](https://github.com/C-3sc0/pands-project#iris-data-insight-extraction)
* [Iris Data Visualization](https://github.com/C-3sc0/pands-project#iris-data-visualization)
  * [libraries and modules]

* [References](https://github.com/C-3sc0/pands-project#references)

## Fisher's Iris Data set information

### Fisher's Iris Data set History

The *Iris* *flower* *data*, also known as *Fisher's* *Iris* *data* *set* was introduced by British biologist and statistician Sir Ronald Aylmer Fisher in his 1936 article titled "[*The* *Use* *of* *Multiple* *Measurements* *in* *Taxonomic* *Problems*](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)". It is important to mention that the data used in aforementioned article were not collect directly by Fisher himself but by Dr. Edgar Anderson, who collected it in the Gaspé Peninsula region of Canada.
The article Fisher formulated and assessed a linear function that distinguishes between Iris species based on the morphology of their flowers.[^1]

Iris flowers can be distinguished in **three** species:*Iris* *Setosa*, *Iris* *Virginica* & *Iris* *Versicolor* as shown in the image below[^2]:

![Iris flower spcecies](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

## Data set code and Analysis

### Fisher's Iris Data set file

The Iris data set, commonly used in the pattern recognition and machine learning field, consist of 50 samples for the 3 classes of iris flowers. Where one class of plants can be separated from the other two classes through a linear boundary, while the other two classes cannot be separated from each other using a linear boundary[^3].

### Data Dimension

The Iris Data set constist of 150 instances, each having five attribue:

 1. *Sepal* *length* in cm
 2. *Sepal* *width* in cm
 3. *Petal* *length* in cm
 4. *Petal* *width* in cm
 5. *Class*

The first 4 attributes are considered quantitative variables, whereas the last one is cosidered categorical variable representing the species of the flower. This variable can take on three possible values: *Setosa*, *Virginica* and *Versicolour* [^4].

### Importing the data

The ``` csv_url ``` is a variable that store the Iris Data set available from the [UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris) in csv format. Here, ``` pandas ``` has been used to import the data set.

```python
iris = pd.read_csv(csv_url, names = attribute_names)
```

The above line of code is used to read a CSV file containing the Iris flower dataset and store it in a pandas DataFrame object called `iris`. The `pandas` library makes it simple to import tabular data into a DataFrame[^5] object. By reading data into a DataFrame with the `pandas` library, we can rapidly conduct data analysis and manipulation using the pandas library's extensive set of functions and methods.
Since the csv file at the UCI Machine Learning Repository does not include the variable attributes information in the same file, the ``` name = ``` parameter is used to list the attribute's names.

## Iris Data Insight Extraction

This Section aims to provide an overview of the Fisher's Iris Data set by presenting several statistics that can help to understand better the data.
Let's start to take a look at the appearance of the Iris DataFrame. In order to do so, two function can be taken into consideration: ```head()``` & ```tail()```.

* The function ```head()``` retrieves a specified number of rows from the beginning of a dataset, if no number is specified, the default value of 5 rows will be displayed.

```python
      Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)     Class
0                5.1               3.5                1.4               0.2  Iris-setosa
1                4.9               3.0                1.4               0.2  Iris-setosa
2                4.7               3.2                1.3               0.2  Iris-setosa
3                4.6               3.1                1.5               0.2  Iris-setosa
4                5.0               3.6                1.4               0.2  Iris-setosa
```

* The function ```tail()``` retrieves a specified number of rows from the bottom of a dataset, and also in this case the default value of 5 rows will be displayed if no number is specified:

```python
      Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)     Class
145                6.7               3.0                5.2               2.3  Iris-virginica
146                6.3               2.5                5.0               1.9  Iris-virginica
147                6.5               3.0                5.2               2.0  Iris-virginica
148                6.2               3.4                5.4               2.3  Iris-virginica
149                5.9               3.0                5.1               1.8  Iris-virginica

```

The structure presented above shows that the Data Set is comprised of an index No. and 5 different columns: the first 4 columns represent the quantitative variables, while the last column indicates the class variable.
Moreover, by using the ```value_counts``` method, it is possible to determine whether the Data Ser is evenly distributed or not, meaning if each class contains an equal number of entries:

```python
print("The Iris plant are: \n")
print(iris["Class"].value_counts())
```

The output of the above code, generates a table that display the occurrence of distinct values:

```python
The Iris plant are:
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: Class, dtype: int64

```

Based on the above information, It is apparent that all the Iris classes show the same number of entries, indicating a balanced Data Set.
Additional attributes such as, index, ndim, shape, isnull etc., can be taken into consideration to gain a more comprehensive understanding of the iris data set, as showed in the below code:

```python
print(f" The index of the Data Set is: ", iris.index)
print(f"The Iris Data Set has {iris.ndim} dimensions")
print(f"The Iris data set has {iris.shape[0]} rows and {iris.shape[1]} columns")
print(f"the number of missing value in the Data set is: \n{iris.isnull().sum()}")
print(f"Information about the Iris Data Set:")
print(iris.info())
```

* The ```index``` attribute indicates the automatically generated index of the Data Frame upon reading the CSV file. in This case the output will be:

```The index of the Data Set is:  RangeIndex(start=0, stop=150, step=1)```

* The `ndim` attirbute shows the number of axes dimension of the Iris Data Set[^6]. The output will be:

```The Iris Data Set has 2 dimensions```

* The ```shape``` attribute will return the number of rows and columns present in the Data set, In particular shape[0] is used to obtain the total number of row, while shape[1] will return the total number of columns present in the Data Set[^7]:

```The Iris data set has 150 rows and 5 columns```

* The ```isnull()``` attribute check for any missing values that were imported as null value into the Data Set, and it provides a Boolean value of either **True** or **False** for each observation. The ```isnull().sum()``` attribute will count the number of missing values in each row & column and it returns new information with the sum of null values in each column of the original Data Set. the sum method calculate `True = 1` and `False = 0`[^8]:

```python
the number of missing value in the Data set is:
Sepal_Length (cm)    0
Sepal_Width (cm)     0
Petal_Length (cm)    0
Petal_Width (cm)     0
Class                0
dtype: int64
```

The above output shows that the Iris Data set is a compact Data Set that does not contain any missing value.

* The ```info()``` attribute displays a concise summary of the Data set, incluing information on the index type and column data types, non-values, and memory usage[^9]:

```python
Information about the Iris Data Set:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   Sepal_Length (cm)  150 non-null    float64
 1   Sepal_Width (cm)   150 non-null    float64
 2   Petal_Length (cm)  150 non-null    float64
 3   Petal_Width (cm)   150 non-null    float64
 4   Class              150 non-null    object
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None
```

As per above output, we can immediately see that the Data Set has 150 rows and 5 columns. It also tells us the number of non-null values in each column, the dtype of each column and the memory usage of the Data Set.

Common mathematical and statistical methods are available for pandas objects. These methods typically generate a single value, such as count[^10], mean[^11], standard deviation[^12], minimum[^13], percentiles[^bignote] (25%, 50%, 75%), maximum[^15]. To obtain multiple summary statistics at once, the describe() method can be used[^16]:

```print(f"Statistical summary of the dataset: \n{iris.describe()}")```

```python
Statistical summary of the dataset: 
          Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean          5.843333          3.054000           3.758667          1.198667
std           0.828066          0.433594           1.764420          0.763161
min           4.300000          2.000000           1.000000          0.100000
25%           5.100000          2.800000           1.600000          0.300000
50%           5.800000          3.000000           4.350000          1.300000
75%           6.400000          3.300000           5.100000          1.800000
max           7.900000          4.400000           6.900000          2.500000
```

Summary statistics for the iris Data Set:

* The mean of the Sepal Length is 5.8 cm. The mean of the Sepal Length is greater then the mean of the other three measurements.

* The highest standard deviation can be found in the Petal Length (1.76 cm), while the smallest can be found in the Sepal Width (0.43 cm).

* the range of min and max value is:
  * Sepal Length: 4.3 cm to 7.9 cm
  * Sepal Width: 2.0 cm to 4.4 cm
  * Petal Length: 1.0 cm to 6.9 cm
  * Petal Width: 0.1 cm to 2.5 cm

* The percentiles give an idea about the distribution of the data:
  For example, 50% of the observations have Sepal Length between 5.1 cm and 6.4 cm.

### Iris Data Visualization

#### Libraries and Modules

<details>
<summary>Libraries</summary>

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

</details>

To analyze the Iris Data set with Python, we need to import several Python libraries, each with its specific purpose:

- ```pandas```: It offers high-performance and user-friendly data analysis tools, specifically designed for working with data in a tabular format.  It enables working with structured data that contains a set of ordered columns, where each column can have a different data type. This makes it highly suitable for analyzing the Iris dataset, which consists of several numerical columns and one categorical column[^17].
- ```numpy```: It provides support for large, multi-dimensional arrays and matrices of numerical data, which are commonly used in machine learning[^18].
- ```matplotlib```: It provides support for large, multi-dimensional arrays and matrices of numerical data[^19].
- ```seaborn```: It is based on matplotlib and provides a high-level interface for creating more complex and informative statistical graphics[^20].

Utilizing plots to visualize the Iris dataset is an effective method to examine the data and obtain valuable understanding regarding the correlations between various features present in the dataset.

By utilizing the ```countplot()``` function, we can obtain a more comprehensive understanding of the parameters of the iris dataset[^21]. 

<details>
<summary>Class</summary>

```python
sns.countplot(data=iris, x="Class", saturation= 0.5)
plt.show()
```

</details>

The function generates a countplot that visualizes the distribution of the categorical variable "Class" in the dataset. As a result, the countplot showcases the frequency of each type of iris flower (setosa, versicolor, and virginica) on the y-axis and the count of each class on the x-axis. This graphical representation can offer valuable insights into the distribution of the target variable in the dataset:

![Class](https://github.com/C-3sc0/pands-project/blob/main/plots/Class-Count.png?raw=true)

The countplot provides a visual confirmation of our previous observation that the Iris dataset is well-balanced. This is evident from the plot as it shows an equal count of 50 rows for all three classes.

Next, we will analyze the five attributes of the Iris dataset using histograms. To create a histogram for each numerical column in the DataFrame, we will use the ```.plot.hist()``` method[^22] from the pandas library. This method groups the values of all given Series in the DataFrame into bins and draws all bins in one histogram per column[^23].

The resulting histograms will show the distribution of each of the measurement attributes across the Iris dataset.

![Histogram](https://github.com/C-3sc0/pands-project/blob/main/plots/Iris-data-set-histogram.png?raw=true)

The histograms generated by the ```iris.hist()``` function give a general overview of the distribution of each variable in the iris dataset. However, they do not allow for a more detailed analysis of the distribution of multiple variables in the dataset. In contrast, the **Seaborn's distplot** method provides a more advanced solution for creating histograms of multiple distributions, enabling us to better explore and analyze the dataset. By using ```distplot()```, we can not only visualize the distribution of each variable for different classes of flowers, but also compare the distributions between different classes[^24][^25].

<details>
<summary>.distplot()</summary>

```python
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
```

</details>

The above code filters the original Iris dataset by separating it into three new datasets, each containing only the rows corresponding to one of the three species of Iris flowers: Setosa, Versicolor, and Virginica. This is done because we want to compare the distributions of sepal lengths between the three species separately.

![SepalL](https://github.com/C-3sc0/pands-project/blob/main/plots/Sepal-Length-distplot.png?raw=true)

![SepalW](https://github.com/C-3sc0/pands-project/blob/main/plots/Sepal-Width-distplot.png?raw=true)

![PetalL](https://github.com/C-3sc0/pands-project/blob/main/plots/Petal-Length-distplot.png?raw=true)

![PetalW](https://github.com/C-3sc0/pands-project/blob/main/plots/Petal-Width-distplot.png?raw=true)

The above graphs provide us with some valuable insights about the Iris dataset. If, for example, we take into consideraton the Petal attribute, We can observe that there is an overlap between the Petal Length and Width of iris versicolor and virginica, while iris setosa appears to be distinct from the other two species. Interestingly, the distribution of Petal Length for each species is quite different. We can see that setosa has a shape that is closest to a normal distribution, with the highest peak, while the distributions for versicolor and virginica are more spread out. This information can help us distinguish between the three species more accurately[^26].







### References

[^1]: [towardsdatascience](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5) - The Iris Dataset — A Little Bit of History and Biology
[^2]: http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
[^3]: [angela1c.com](https://www.angela1c.com/projects/iris_project/the-iris-dataset/) - About Fisher’s Iris dataset
[^4]:[rstudio-pubs-static.s3](https://rstudio-pubs-static.s3.amazonaws.com/568691_afb34f2ab2ad4734b63064a2dcf25931.html#Data%20Dimension)
[^5]: In Python, a DataFrame object is a two-dimensional table-like data format supplied by the pandas module. It is made up of rows and columns, with each column containing various types of data (e.g., number, float, string), and each row representing a record or observation - [geeksforgeeks](https://www.geeksforgeeks.org/python-pandas-dataframe/).
[^6]:[StackOverflow](https://stackoverflow.com/questions/8376218/what-do-we-mean-by-dimension-when-talking-about-arrays)
[^7]: [StackOverflow](https://stackoverflow.com/questions/65949568/what-does-rangey-shape1-mean-in-for-i-in-rangedataset2-shape1#:~:text=shape%5B0%5D%20will%20give%20you,columns%20present%20in%20the%20dataFrame.)
[^8]: [note.nkmk](https://note.nkmk.me/en/python-pandas-nan-judge-count/)
[^9]: [geeksforgeeks](https://www.geeksforgeeks.org/python-pandas-dataframe-info/)
[^10]: The number of non-empty values in the Data Set
[^11]: It shows the mean or average values of the coumn
[^12]: It shows the Standard Deviation of the column
[^13]: It shows the smallest value observed in the Data Set for each variable.
[^bignote]: It shows the percentage of values falling below that percentile. The first quartile is the value below which 25% of the data fall; the median is the value below whichc 50% of the data fall and the third quartile is the value below which 75% of the data fall.
[^15]: It shows the Largest value observed in the Data Set for each variable.
[^16]:[W3schools](https://www.w3schools.com/python/pandas/ref_df_describe.asp)
[^17]: [Geeksforgeeks](https://www.geeksforgeeks.org/pandas-tutorial/)
[^18]: [numpy](https://numpy.org/doc/stable/)
[^19]: [matploylib](https://matplotlib.org/stable/users/explain/api_interfaces.html)
[^20]: [seaborn](https://seaborn.pydata.org/index.html)
[^21]:[datagy](https://datagy.io/seaborn-countplot/)
[^22]: [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)
[^23]: [datacamp](https://www.datacamp.com/tutorial/histograms-matplotlib)
[^24]: [cmdlinetips](https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/)
[^25]: [Stack Overflow](https://stackoverflow.com/questions/60046243/how-to-make-a-distplot-for-each-column-in-a-pandas-dataframe)
[^26]: [RPubs](https://rpubs.com/Karolina_G/848706)