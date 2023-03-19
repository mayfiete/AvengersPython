
import psycopg2
import csv

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

# Open the flat file
# with open('C:\Interview\Avengers\marvel.csv', 'r') as f:
#     reader = csv.reader(f, delimiter='\t')
#     next(reader)  # Skip the header row
#     for row in reader:
#         # Insert each row into the database
#         # cursor.execute("INSERT INTO character_comic (name, comic) VALUES (%s, %s, %s')", (row[0], row[1], row[2]))
#         cursor.execute(
#             "INSERT INTO character_comic (name, comic) VALUES (%s, %s)", (
#                 row[0], row[1])
#         )

# Open the CSV file and read its contents
with open('C:\Interview\Avengers\marvel.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    # next(reader)  # skip the header row
    rows = [row for row in reader]

# Create a cursor object
cur = conn.cursor()

# Construct the SQL query to insert the data into the database
query = "INSERT INTO character_comic (name, comic) VALUES (%s, %s)"


# Execute the query for each row in the CSV file
for row in rows:
    print(row)
    # print(row[0])
    cur.execute(query, row)
    # print(query, row)

# Commit the changes to the database
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
