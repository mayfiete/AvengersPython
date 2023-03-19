
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
cursor = conn.cursor()

# Open the flat file
with open('C:\Interview\Avengers\marvel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Insert each row into the database
        # cursor.execute("INSERT INTO character_comic (name, comic) VALUES (%'s, %s, %s')", (row[0], row[1], row[2]))
        cursor.execute(
            "INSERT INTO character_comic (name, comic) VALUES ('Wolverine', 'Test')"
        )  # this works


# Commit the changes to the database and close the connection
conn.commit()
cursor.close()
conn.close()
