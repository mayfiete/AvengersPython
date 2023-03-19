import pandas as pd

# Read the tab-delimited CSV file into a pandas DataFrame
df = pd.read_csv('C:\Interview\Avengers\AvengersPython\marvel.csv', sep='|')

# Create a pivot table using the pandas pivot_table() function
pivot_table = pd.pivot_table(
    df, index='column1', columns='column2', aggfunc='count')

# Print the pivot table
print(pivot_table)
