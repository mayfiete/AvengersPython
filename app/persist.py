

from DbConnx import DbConnx
import csv

conn = DbConnx()
conn.connect()


# Open the CSV file and read its contents
with open('C:/AvengersPython/marvel.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader)  # skip the header row
    rows = [row for row in reader]


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
