

# create a class to encapsulate the database connection
import csv
from db_connx import db_connx

conn = db_connx()
conn.connect()


# Open the CSV file and read its contents
with open('C:/Interview/Avengers/AvengersPython/marvel.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)  # skip the header row
    rows = [row for row in reader]

# Create a cursor object
# cur = conn.cursor()

# Construct the SQL query to insert the data into the database
query = "INSERT INTO character_comic (name, comic) VALUES (%s, %s) ON CONFLICT DO NOTHING;"


# figure out the name, comic insert into character_comic (name, comic) values ('name', 'comic') on conflict do nothing;

# Execute the query for each row in the CSV file
for row in rows:
    name, comic = row
    conn.execute(query, (name, comic))

# Commit the changes to the database
conn.conn.commit()

# Close the cursor and database connection
conn.close()
