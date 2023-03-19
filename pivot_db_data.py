
# fetch data from the database
from matplotlib import pyplot as plt
import psycopg2
import csv
import pandas as pd

# AWS RDS database configuration
# put these in a config file and import them instead of hardcoding them here
db_host = "marvelgetwell.cs1gposyeo3a.us-east-1.rds.amazonaws.com"
db_name = "postgres"
db_user = "getwell"
db_password = "Voltron*09"
db_port = "5432"

# Connect to the database
conn = psycopg2.connect(host=db_host, database=db_name,
                        user=db_user, password=db_password, port=db_port)

# Create a cursor object
cur = conn.cursor()

# Construct the SQL query to insert the data into the database
query = "SELECT name, comic FROM character_comic;"
cur.execute(query)

# fetch all the rows from the database
rows = cur.fetchall()


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
cur.close()
conn.close()
