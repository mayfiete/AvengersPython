
# create a class to encapsulate the database connection
from matplotlib import pyplot as plt
import csv
import pandas as pd
import numpy as np
from DbConnx import DbConnx

conn = DbConnx()
conn.connect()

# Construct the SQL query to insert the data into the database
query = "SELECT name, comic FROM character_comic;"
# Execute the query for each row in the CSV file
conn.execute(query)

# fetch all the rows from the database
rows = conn.fetchall()


# put the rows into pivot table
# Create a pivot table using the pandas pivot_table() function
df = pd.DataFrame(rows, columns=['name', 'comic'])
# count the number of comics for each character
comic_counts = df.groupby('name')['comic'].count()

print(comic_counts)

# create a histogram image of the data
comic_counts.plot(kind='hist', title='Number of Comics per Character')
plt.savefig('comic_counts.png')

# close the cursor and connection to so the server can allocate
# bandwidth to other requests
conn.close()
