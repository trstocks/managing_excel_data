
import pandas as pd
from pathlib import Path


input_file = Path.cwd() / 'data' / 'us-500.xlsx'
df = pd.read_excel(input_file)
# Print the results of the last_name column. This will show the beginning and the end, but will print '...' to represent
# that more data exists in between.
print(df.last_name)

# Sometimes, column names are multiple words with spaces. A better way to grab that information is by doing this:
print(df['email address'])

# This also words with the previous example.
print(df['last_name'])

# Shows unique states, meaning that out of the 500 records/rows, there is information x number of states.
# The result should show 47
print('Number of unique States: ')
print(df['state'].nunique())

# counts the states column data. Should show 500, as there are 500 records.
print('State Data: ')
print(df['state'].count())

# Get the number of records for each state
print(df['state'].value_counts())

# Transform that data to a percentage
print(df['state'].value_counts(normalize=True))


print('Add Country column to data:')
# Add column to data
df['Country'] = 'USA'
# show new column
print(df.head())


