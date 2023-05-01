# pands-project

-------
This repository serves as a resource for the final project for the ATU university's HDip in Computing in Data Analytics course's Programming and Scripting module. The project's primary objective focuses on the study and examination of the Fisher's Iris Data set.

## Table of Contents

* [Fisher's Iris Data set information](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-information)
  * [Fisher's Iris Data set History](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-history)
* [Data set code and Analysis](https://github.com/C-3sc0/pands-project#data-set-code-and-analysis)
  * [Fisher's Iris Data set file](https://github.com/C-3sc0/pands-project#fishers-iris-data-set-file)
  * [Data Dimension](https://github.com/C-3sc0/pands-project#data-dimension)
  * [Importing the data](https://github.com/C-3sc0/pands-project#importing-the-data)
  * [Iris Data Insight Extraction](https://github.com/C-3sc0/pands-project#iris-data-insight-extraction)
* [Exploring Differences in Sepal and Petal Attributes](https://github.com/C-3sc0/pands-project#exploring-differences-in-sepal-and-petal-attributes)
* [Iris Data Visualization](https://github.com/C-3sc0/pands-project#iris-data-visualization)
* [libraries and modules](https://github.com/C-3sc0/pands-project#libraries-and-modules)
  * [Countplot](https://github.com/C-3sc0/pands-project#countplot)
  * [Histogram](https://github.com/C-3sc0/pands-project#histogram)
  * [Scatterplot](https://github.com/C-3sc0/pands-project#scatterplot)
  * [Pairplot](https://github.com/C-3sc0/pands-project#pairplot)
  * [Violinplot](https://github.com/C-3sc0/pands-project#violin-plot)
* [Conclusion](https://github.com/C-3sc0/pands-project#conclusion)
  
## Fisher's Iris Data set information

### Fisher's Iris Data set History

The *Iris* *flower* *data*, also known as *Fisher's* *Iris* *data* *set* was introduced by British biologist and statistician Sir Ronald Aylmer Fisher in his 1936 article titled "[*The* *Use* *of* *Multiple* *Measurements* *in* *Taxonomic* *Problems*](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)". It is important to mention that the data used in aforementioned article were not collect directly by Fisher himself but by Dr. Edgar Anderson, who collected it in the Gaspé Peninsula region of Canada.
The article Fisher formulated and assessed a linear function that distinguishes between Iris species based on the morphology of their flowers.[^1]

Iris flowers can be distinguished in **three** species: ```Iris Setosa```, ```Iris Virginica``` & ```Iris Versicolor``` as shown in the image below[^2]:

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

The ``` csv_url ``` is a variable that store the Iris Data set available from the [UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris) in csv format. Here, ``` pandas ``` has been used to import the data set. Alternately, the Iris Data set can be downloaded and saved it locally as CSV file. It can then be read the data of the CSV file by by specifying his file path.

```python
iris = pd.read_csv(csv_url, names = attribute_names)
```

The above line of code is used to read a CSV file containing the Iris flower data set and store it in a pandas DataFrame object called `iris`. The `pandas` library makes it simple to import tabular data into a DataFrame[^5] object. By reading data into a DataFrame with the `pandas` library, we can rapidly conduct data analysis and manipulation using the pandas library's extensive set of functions and methods.
One of the problems with the UCI Machine Learning Repository's data set is that the attribute information is not included in the main file. However, this information can be found in a separate file located in the **[Data set Description](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)** section.

<details>
<summary>Data set Description</summary>

```python
7. Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica
```

</details>

In order to address this problem, I opted to create a list consisting of the attribute names and store it in a variable called `attribute_names`.  Then, I passed this variable as an argument to the ``` name = ``` parameter in the current script:

<details>
<summary>Iris attribute's names</summary>

```
#Define the names of the columns in the dataset
attribute_names = ['Sepal_Length (cm)','Sepal_Width (cm)','Petal_Length (cm)','Petal_Width (cm)','Class']
```

</details>

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
print(f" The index of the Data Set is:\n", iris.index, "\n")
print(f"The Iris Data Set has {iris.ndim} dimensions\n")
print(f"The Iris data set has {iris.shape[0]} rows and {iris.shape[1]} columns\n")
print(f"The number of missing value in the Data set is: \n {iris.isnull().sum()}\n")
print(f"Information about the Iris Data Set:\n")
print(iris.info(),"\n")
```

* The ```index``` attribute indicates the automatically generated index of the Data Frame upon reading the CSV file. in This case the output will be:

``` 
The index of the Data Set is:
RangeIndex(start=0, stop=150, step=1)
```

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

```
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

### Exploring Differences in Sepal and Petal Attributes

The Iris dataset can be categorized into three distinct subsets depending on the class assigned to each observation. One way to filter rows from the Iris DataFrame is by using Boolean Indexing, which selects rows that meet certain conditions[^17]. For instance:

<details>
<summary>subset groups</summary>

```python
#Create 3 new DataFrame for the Iris Class Attribute for further analysis
setosa = iris[iris.Class == "Iris-setosa"]
versicolor = iris[iris.Class == "Iris-versicolor"]
virginica = iris[iris.Class == "Iris-virginica"]
```

</details>

The ```.Class``` attribute in the given code signifies the specific column on which the filtering will be applied. Here for example, the expression ```== 'Iris-setosa'``` serves to filter the dataset and extract only those rows where the Class column has the value "Iris-setosa".
This division can be helpful because it allows us to perform separate analysis on each subset. Since each subset represents a different species of Iris, this division is useful in comparing and contrasting the different attributes of each species. By performing separate analysis on each subset, we can gain a better understanding of the unique characteristics of each species and how they differ from one another.
The describe method can be used to obtain summary statistics for each class of iris flower in the data set:

<details>
<summary>input</summary>

```python
print(f"\nThe summary statistic for Iris Setosa class are:\n {setosa.describe()}")
print(f"\nThe summary statistic for Iris Versicolor class are:\n {versicolor.describe()}")
print(f"\nThe summary statistic for Iris Virginica class are:\n {virginica.describe()}\n")
```

</details>

```
The summary statistic for Iris Setosa class are:
        Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)
count           50.00000         50.000000          50.000000          50.00000
mean             5.00600          3.418000           1.464000           0.24400
std              0.35249          0.381024           0.173511           0.10721
min              4.30000          2.300000           1.000000           0.10000
25%              4.80000          3.125000           1.400000           0.20000
50%              5.00000          3.400000           1.500000           0.20000
75%              5.20000          3.675000           1.575000           0.30000
max              5.80000          4.400000           1.900000           0.60000

The summary statistic for Iris Versicolor class are:
        Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)
count          50.000000         50.000000          50.000000         50.000000
mean            5.936000          2.770000           4.260000          1.326000
std             0.516171          0.313798           0.469911          0.197753
min             4.900000          2.000000           3.000000          1.000000
25%             5.600000          2.525000           4.000000          1.200000
50%             5.900000          2.800000           4.350000          1.300000
75%             6.300000          3.000000           4.600000          1.500000
max             7.000000          3.400000           5.100000          1.800000

The summary statistic for Iris Virginica class are:
        Sepal_Length (cm)  Sepal_Width (cm)  Petal_Length (cm)  Petal_Width (cm)
count           50.00000         50.000000          50.000000          50.00000
mean             6.58800          2.974000           5.552000           2.02600
std              0.63588          0.322497           0.551895           0.27465
min              4.90000          2.200000           4.500000           1.40000
25%              6.22500          2.800000           5.100000           1.80000
50%              6.50000          3.000000           5.550000           2.00000
75%              6.90000          3.175000           5.875000           2.30000
max              7.90000          3.800000           6.900000           2.50000
```

The statistical analysis of the Iris dataset at the class level indicates that there are notable differences between the three species, with Iris Setosa showing distinct characteristics compared to Versicolor and Virginica. For instance, the average petal length of Iris Setosa is significantly smaller (1.46 cm) than that of Versicolor (4.26 cm) and Virginica (5.552 cm). Additionally, the petal width of Setosa is considerably smaller than the other two species. Interestingly, Setosa also exhibits smaller sepal length measurements on average, while its sepal width is larger than that of Versicolor and Virginica. This is also reflected in the minimum and maximum measurements of the three species. Overall, the analysis suggests that the differences between Iris Setosa and the other two species are more pronounced than the differences between Versicolor and Virginica.

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

- ```pandas```: It offers high-performance and user-friendly data analysis tools, specifically designed for working with data in a tabular format.  It enables working with structured data that contains a set of ordered columns, where each column can have a different data type. This makes it highly suitable for analyzing the Iris dataset, which consists of several numerical columns and one categorical column[^18].
- ```numpy```: It provides support for large, multi-dimensional arrays and matrices of numerical data, which are commonly used in machine learning[^19].
- ```matplotlib```: It provides support for large, multi-dimensional arrays and matrices of numerical data[^20].
- ```seaborn```: It is based on matplotlib and provides a high-level interface for creating more complex and informative statistical graphics[^21].

### Countplot

Utilizing plots to visualize the Iris dataset is an effective method to examine the data and obtain valuable understanding regarding the correlations between various features present in the dataset.

By utilizing the ```countplot()``` function, we can obtain a more comprehensive understanding of the parameters of the iris dataset[^22]. 

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

### Histogram

Next, we will analyze the five attributes of the Iris dataset using histograms. To create a histogram for each numerical column in the DataFrame, we will use the ```.plot.hist()``` method[^23] from the pandas library. This method groups the values of all given Series in the DataFrame into bins and draws all bins in one histogram per column[^24].

The resulting histograms will show the distribution of each of the measurement attributes across the Iris dataset.

![Histogram](https://github.com/C-3sc0/pands-project/blob/main/plots/Iris-data-set-histogram.png?raw=true)

The histograms generated by the ```iris.hist()``` function give a general overview of the distribution of each variable in the iris dataset. However, they do not allow for a more detailed analysis of the distribution of multiple variables in the dataset. In contrast, the **Seaborn's histplot** method provides a more advanced solution for creating histograms of multiple distributions, enabling us to better explore and analyze the dataset. By using ```histplot()```, we can not only visualize the distribution of each variable for different classes of flowers, but also compare the distributions between different classes[^25][^26].

<details>
<summary>.histplot()</summary>

```python
#create a 2x2 gris histplot to compare the 4 attributes:
fig, ax = plt.subplots(2,2, figsize=(10,6))
sns.histplot(data=iris, x="Sepal_Length (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax= ax[0,0])
sns.histplot(data=iris, x="Sepal_Width (cm)", hue="Class", kde=False, linewidth=0,bins=25, element="step", ax= ax[0,1])
sns.histplot(data=iris, x="Petal_Length (cm)", hue="Class", kde=False, linewidth=0,bins=25, element="step", ax= ax[1,0])
sns.histplot(data=iris, x="Petal_Width (cm)", hue="Class", kde=False, linewidth=0, bins=25, element="step", ax= ax[1,1])
fig.suptitle("Comparision of Sepal & Petal attributes between the 3 Iris flowers", size=20)
plt.savefig("histograms-for-comparison-of-the-4-attribute.png")
plt.show()
```

</details>

![SepalL](https://github.com/C-3sc0/pands-project/blob/main/plots/histograms-for-comparison-of-the-4-attribute.png?raw=true)


The above graphs provide us with some valuable insights about the Iris dataset. If, for example, we take into consideraton the Petal attribute, We can observe that there is an overlap between the Petal Length and Width of iris versicolor and virginica, while iris setosa appears to be distinct from the other two species. Interestingly, the distribution of Petal Length for each species is quite different. We can see that setosa has a shape that is closest to a normal distribution, with the highest peak, while the distributions for versicolor and virginica are more spread out. This information can help us distinguish between the three species more accurately[^27]. The sepal histograms show a distinct scenario where there is a notable amount of overlap among all three species for both sepal length and width, as evident from the above graphs[^28].

### Scatterplot

A scatter plot is a type of plot that displays values for two variables as a set of individual points. It is useful for visualizing the relationship between two variables, and can help identify patterns or trends in the data. With the function ```scatterplot()``` the data is plotted along two axes, x & y, with one variable on the x-axis and the other variable on the y-axis. Each point in the plot represents a single observation[^29]:

<details>
<summary>.scatterplot()</summary>

```python
sns.scatterplot(y=iris["Sepal_Width (cm)"], x=iris["Sepal_Length (cm)"], hue= iris["Class"], s=50)
plt.title("Comparison of Sepal Sizes Across Iris Species")
plt.show()
```

</details>

The scatter plots above describe the relationship between Sepal/Petal Lenght (on the x axis) and Sepal/Petal Width (on the y axis). Every data point represents an individual flower and its position is determined by its lenght x width.

![Sepal](https://github.com/C-3sc0/pands-project/blob/main/plots/Iris-Sepal-attribute-scatterplot.png?raw=true)

The initial scatter plot shows that **flowers with longer sepals tend to have narrower widths**, and vice versa. Interestingly, Iris setosa has the smallest sepals but higher width, while Iris versicolor and Iris virginica have similar sizes, but with slightly different shapes for both the length and width.

![Petal](https://github.com/C-3sc0/pands-project/blob/main/plots/Iris-Petal-attribute-scatterplot.png?raw=true)

On the other hand, the second scatter plot presents a different scenario. In this case, **flower classes with longer petals tend to have wider widths**, and vice versa. Each class of iris flower has a unique pattern[^30]:

- Iris Setosa has the smallest petal length and width.
- Iris Virginica has the largest petal length and width.

### Pairplot

The pairplot is used to explore the pairwise relationships between multiple variables in a dataset. The pairplot function generates a grid of plots where each variable in the dataset is plotted against all the other variables, creating a matrix of scatter plots. The variables are shared on the y-axis across a single row and on the x-axis across a single column. The diagonal of the plot matrix shows the distribution of the variable in that column as a univariate plot[^31]. 

<details>
<summary>.pairplot()</summary>

```python
sns.pairplot(iris, hue= "Class")
plt.show()
```

</details>

![pairplot](https://github.com/C-3sc0/pands-project/blob/main/plots/Iris-data-set-pairplot.png?raw=true)

By analyzing the pairplot for the iris dataset, we can observe that Sepal/Petal length and width are positively correlated, which means that as sepal/Petal length increases, sepal/petal width also tends to increase. The Setosa class is clearly separated from the other two classes in all scatterplots, indicating that it has distinct characteristics from Versicolor and Virginica. Versicolor and Virginica are more similar to each other, but can still be distinguished by the combination of sepal and petal measurements.

 

### Violin plot

A violin plot is a graphical representation that allows us to visualize the distribution of one or more numeric variables for different groups. Each "violin" represents a group or a variable, and the shape of the violin represents the density estimate of the variable. The width of the violin at a particular point represents the estimated density of observations in that range. The plot is symmetric, with the density estimate mirrored and flipped to create the image of a violin. This visualization technique is useful for comparing the ranking and distribution of multiple groups. Violin plots can also display the kernel density estimate (KDE) of the data, which provides a smooth estimate of the probability density function. The KDE helps in visualizing the shape of the distribution more accurately[^32].

<details>
<summary>.violinplot()</summary>

```python
fig, ax = plt.subplots(2,2, figsize=(16,9))
font = {"family" : "Lucida Handwriting", "color" : "Blue", "size" : 15}
sns.violinplot( x= iris["Class"], y= iris["Sepal_Length (cm)"], data= iris,  ax= ax[0,0])
sns.violinplot( x= iris["Class"], y= iris["Sepal_Width (cm)"], data= iris, ax= ax[0,1])
sns.violinplot( x= iris["Class"], y= iris["Petal_Length (cm)"], data= iris,  ax= ax[1,0])
sns.violinplot( x= iris["Class"], y= iris["Petal_Width (cm)"], data= iris,  ax= ax[1,1])
fig.suptitle("Violinplot of Iris Sepal & Petal attributes", size=20, fontdict=font)
plt.show()
```

</details>

![Violinplot](https://github.com/C-3sc0/pands-project/blob/main/plots/Violinlot-of-Iris-Data-Set.png?raw=true)

The above code generates a 2x2 grid of violin plots for the iris dataset, where each plot displays the distribution of the sepal length, sepal width, petal length, and petal width attributes for each of the three iris Class.The width of each violin represents the density of the data points at each value of the attribute, with wider sections indicating more points in that range. The thin horizontal line inside each violin indicates the median value, while the vertical lines extending from the violin show the range of the data. from the ```violinplot()``` we have a better visual of the ditribution of the 3 Iris class: Iris Setosa tends to have the shortest Sepal/Petal lenght and Petal width and the widest Sepal width compared to the other 2 class. Sepal length and width ditributions is similar fo both Iris Versicolor and Virginica. However, based on the violin plots for petal length and width, we can see that Iris Virginica tends to have slightly longer and wider petals compared to Iris Versicolor.

### Conclusion

In conclusion, this project has demonstrated the importance of visualizing and understanding data in order to gain insights and make informed decisions. The Iris dataset is a classic example of a dataset that has been used extensively in the field of machine learning and is still relevant today. Through the pairwise grid of scatter plots, it is clear that the Iris Setosa stands out as being different from the other two species. Additionally, the standard deviations and averages of petal and sepal measurements also highlight the differences between the Iris Setosa and the other two species. These findings can be useful in further analysis and modeling of the dataset, and provide a foundation for future research in the field of machine learning.

[^1]: The Iris Dataset — A Little Bit of History and Biology [towardsdatascience](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)
[^2]: Data Science Example - Iris dataset - [lac.inpe.br](http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)
[^3]: About Fisher’s Iris dataset - [angela1c.com](https://www.angela1c.com/projects/iris_project/the-iris-dataset/)
[^4]:INDEX - [rstudio-pubs-static.s3](https://rstudio-pubs-static.s3.amazonaws.com/568691_afb34f2ab2ad4734b63064a2dcf25931.html#Data%20Dimension)
[^5]: In Python, a DataFrame object is a two-dimensional table-like data format supplied by the pandas module. It is made up of rows and columns, with each column containing various types of data (e.g., number, float, string), and each row representing a record or observation - [geeksforgeeks](https://www.geeksforgeeks.org/python-pandas-dataframe/).
[^6]:What do we mean by "dimension" when talking about arrays?" - [StackOverflow](https://stackoverflow.com/questions/8376218/what-do-we-mean-by-dimension-when-talking-about-arrays)
[^7]: What does 'range(y.shape[1])' mean in "for i in range(dataset2.shape[1]):"? - [StackOverflow](https://stackoverflow.com/questions/65949568/what-does-rangey-shape1-mean-in-for-i-in-rangedataset2-shape1#:~:text=shape%5B0%5D%20will%20give%20you,columns%20present%20in%20the%20dataFrame.)
[^8]: pandas: Detect and count missing values (NaN) with isnull(), isna() - [note.nkmk](https://note.nkmk.me/en/python-pandas-nan-judge-count/)
[^9]: Python | Pandas dataframe info() - [geeksforgeeks](https://www.geeksforgeeks.org/python-pandas-dataframe-info/)
[^10]: The number of non-empty values in the Data Set
[^11]: It shows the mean or average values of the coumn
[^12]: It shows the Standard Deviation of the column
[^13]: It shows the smallest value observed in the Data Set for each variable.
[^bignote]: It shows the percentage of values falling below that percentile. The first quartile is the value below which 25% of the data fall; the median is the value below whichc 50% of the data fall and the third quartile is the value below which 75% of the data fall.
[^15]: It shows the Largest value observed in the Data Set for each variable.
[^16]:Pandas DataFrame describe() Method - [W3schools](https://www.w3schools.com/python/pandas/ref_df_describe.asp)
[^17]: Indexing and selecting data - [pandas](http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-index)
[^18]: Pandas Tutorial - [Geeksforgeeks](https://www.geeksforgeeks.org/pandas-tutorial/)
[^19]: NumPy documentation - [numpy](https://numpy.org/doc/stable/)
[^20]:Matplotlib Application Interfaces (APIs) - [matploylib](https://matplotlib.org/stable/users/explain/api_interfaces.html)
[^21]:seaborn: statistical data visualization - [seaborn](https://seaborn.pydata.org/index.html)
[^22]: Seaborn Countplot – Counting Categorical Data in Python - [datagy](https://datagy.io/seaborn-countplot/)
[^23]: pandas.DataFrame.plot.hist - [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)
[^24]: Histograms in Matplotlib - [datacamp](https://www.datacamp.com/tutorial/histograms-matplotlib)
[^25]: seaborn.histplot - [Seaborn](https://seaborn.pydata.org/generated/seaborn.histplot.html)
[^26]: Data Visualization in Python – Iris dataset - [Ummesalmam.com](https://ummesalmam.com/python-for-you/fundamentals-of-python/visualization-in-python-iris-dataset/)
[^27]: Iris data analysis - [RPubs](https://rpubs.com/Karolina_G/848706)
[^28]: Exploratory Data Analysis : Iris Dataset - [Medium.com](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202.1%2C%20then,then%20species%20is%20Iris%20Virginica)
[^29]: Visualizing statistical relationships - [Seaborn](https://seaborn.pydata.org/tutorial/relational.html#relational-tutorial)
[^30]: Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning Classification - [Medium.com](https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d)
[^31]: seaborn.pairplot - [Seaborn](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
[^32]: A Complete Guide to Violin Plots - [Chartio](https://chartio.com/learn/charts/violin-plot-complete-guide/#:~:text=A%20violin%20plot%20depicts%20distributions,plot%2C%20to%20provide%20additional%20information.)