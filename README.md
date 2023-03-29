## pands-project

-------
This repository is used for the final project given during the Programming and scripting module on Higher Diploma in Data Analytics course from ATU university. Topic of the project is research and investigation of Fisher's Iris data set.

## Table of Contents

* Fisher's Iris Data set information
  * Fisher's Iris Data set History
* Data set code and Analysis
  * Fisher's Iris Data set file
  * Data Dimension
  * Importing the data

* References

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

The ``` csv_url ``` is a varible that store the Iris Data set available from the [UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris) in csv format. Here, ``` pandas ``` has been used to import the data set.

```
iris = pd.read_csv(csv_url, names = attribute_names)
```
The above line of code is used to read a CSV file containing the Iris flower dataset and store it in a pandas DataFrame object called ```iris ```. The ```pandas``` library makes it simple to import tabular data into a DataFrame[^5] object. By reading data into a DataFrame with the ```pandas ``` library, we can rapidly conduct data analysis and manipulation using the pandas library's extensive set of functions and methods.
Since the csv file at the UCI Machine Learning Repository does not include the variable attributes information in the same file, the ``` name = ``` parameter is used to list the attribute's names. 
To understand better how DataFrame looks like, the ```.head()``` parameter can be used: 

![Alt text](C:/Users/fratr/Desktop/progetto_pands/head.png)

as per above image, the Data have 5 colums: [0] is the idex number, [1:4] are the quantitative variables, [5] is the class variable. While the ```.head()``` parameter shows oly the first 5 rows, if we want to see the data starting from the bottom, the ```.tail()``` parameter needs to be used:

![Alt text](C:/Users/fratr/Desktop/progetto_pands/tail.png)




### References
[^1]: [towardsdatascience](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5) - The Iris Dataset — A Little Bit of History and Biology
[^2]: http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
[^3]: [angela1c.com](https://www.angela1c.com/projects/iris_project/the-iris-dataset/) - About Fisher’s Iris dataset
[^4]:[rstudio-pubs-static.s3](https://rstudio-pubs-static.s3.amazonaws.com/568691_afb34f2ab2ad4734b63064a2dcf25931.html#Data%20Dimension)
[^5]: In Python, a DataFrame object is a two-dimensional table-like data format supplied by the pandas module. It is made up of rows and columns, with each column containing various types of data (e.g., number, float, string), and each row representing a record or observation - [geeksforgeeks](https://www.geeksforgeeks.org/python-pandas-dataframe/).