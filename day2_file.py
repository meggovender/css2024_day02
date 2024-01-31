# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:49:40 2024

@author: megan
"""

import pandas as pd

df = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/iris.csv")

 """
 relative path =  location to where you are now
 absolute path = location on your windows drive
 """
 
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

file = pd.read_csv(url)



file = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/Geospatial Data.txt", sep = ";")

file = pd.read_excel("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/residentdoctors.xlsx")

file = pd.read_json("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/student_data.json")

df = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])

df = pd.read_json("C:/Users/megan/CSS2024_DAY_2/bin.1.json")

df = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/country_data_index.csv", index_col = 0)

resident = pd.read_excel("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/residentdoctors.xlsx")

print(resident.info())
resident["LOWER_AGE"] = resident["AGEDIST"].str.extract("(\d+)-")
resident["UPPER_AGE"] = resident["AGEDIST"].str.extract("-(\d+)")
print(resident.info())

resident["LOWER_AGE"] = resident["LOWER_AGE"].astype(int)



"""
\d - any digit from 0 to 9 
- - what it should look for
"""

"""
Working with dates

30-01-2024 - UK

01-30-2024 - US

"""

df = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/time_series_data.csv", index_col = 0)

print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format = "%d-%m-%Y")
print(df.info())


df['Year'] = df['Date'].dt.year

"""
.str
.extract
.astype
"""

file = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/patient_data_dates.csv", index_col = 0)
file['Date'] = pd.to_datetime(file['Date'], format = "mixed")
file = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/patient_data_dates.csv", index_col = 0, skiprows = [27])
df.drop(index = 26, inplace = True)

print(file.info())

how did he change / to - in dates?

"""
replace NaN with column average
"""

avg_cal = file["Calories"].mean()

file["Calories"]. fillna(avg_cal, inplace = True)


"""
best practices
"""

file.dropna(inplace = True)
file = file.reset_index(drop = True)
file.loc[7, 'Duration'] = 45

print(file)

pd.set_option('display.max_rows', None)

file = pd.read_csv ("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header = None, names = column_names)

column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

file = pd.read_csv ("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header = None, names = column_names)

print(file.columns)

col_names = file.columns

print(col_names)

file["sepal_length_sq"] = file["sepal_length"]**2
file["sepal_length_sq_2"] = file["sepal_length"].apply(lambda x:x**2)

grouped = file.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)

df1 = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/person_split1.csv")
df2 = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index = True)

df1 = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/person_education.csv")
df2 = pd.read_csv("C:/Users/megan/CSS2024_DAY_2/data_02/data_02/person_work.csv")

df_merge_inner = pd.merge(df1, df2, on = "id")
 
"""
 inner join = returns dataframe with only those rows with the same characteristics
 outer join = all
 left join = all first
 right join = all last
 """
 
file["class"] = file["class"].str.replace("Iris-", "")
 
file = file[file['sepal_length']>5]
file = file[file['class'] == "virginica"] 

file.to_csv("cleaned_iris_data.csv")
file.to_csv("Output/cleaned_iris_data.csv")
file.to_excel("Output/cleaned_iris_data.xlsx", index = False, sheet_name = 'Sheet1')
file.to_json("Output/cleaned_iris_data.json", orient = 'records')
