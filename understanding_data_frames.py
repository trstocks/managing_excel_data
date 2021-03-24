# Importing libraries you'll need
# pandas is how you'll be managing data. the program will be referring to pandas as 'pd'.
# use print() function to show the results in a command prompt/terminal window

import pandas as pd
# pathlib is used to tell the program where the files are located.
from pathlib import Path
# English: from the current directory, go to the data folder and use 'us-500.xlsx' file to use as the data input file
input_file = Path.cwd() / 'data' / 'us-500.xlsx'
# English:  use pandas read_excel function to get/read the data from the file.
df = pd.read_excel(input_file)
# English: Print the top 5 rows to the screen
print(df.head())
# English: Print the bottom 5 rows to the screen
print(df.tail())

# English: Print the columns to the screen.
print(df.columns)
# function provides the number of rows and columns for the data you're working with.
df.shape()

# provides important for understanding when you need to manipulate the data. The DType, or data type column is
# often important to review why data may not correctly display, such as dates.
df.info()

# Quick summary of all the numeric columns
# performs basic math, like count, min, max of numerical data
df.describe()
