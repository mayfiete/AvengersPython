# create a class to encapsulate the database connection and query execution
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import seaborn as sns
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
comic_counts = df.pivot_table(index='name', aggfunc='count')

# Set the color palette
sns.set_palette("muted")

# create a bar chart image of the data
ax = comic_counts.plot(
    kind='bar', title='Number of Comics per Character', legend=False)

# Add labels to the x-axis and y-axis
ax.set_xlabel('Character')
ax.set_ylabel('Number of Comics')

# Add a grid
ax.grid(axis='y')

# Rotate the x-axis labels
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('comic_counts.png')

# close the cursor and connection to so the server can allocate
# bandwidth to other requests
conn.close()
