import pandas as pd

# Read the tab-delimited CSV file into a pandas DataFrame
df = pd.read_csv('C:\Interview\Avengers\marvel.csv', sep='\t')

# Create a pivot table using the pandas pivot_table() function
pivot_table = pd.pivot_table(
    df, index='column1', columns='column2', aggfunc='sum')

# Print the pivot table
print(pivot_table)
