
import psycopg2
import csv

# AWS RDS database configuration
db_host = "your_rds_instance_endpoint"
db_name = "your_database_name"
db_user = "your_username"
db_password = "your_password"
db_port = "5432"

# Connect to the database
conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)
cursor = conn.cursor()

# Open the flat file
with open('your_flat_file.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for row in reader:
        # Insert each row into the database
        cursor.execute("INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))

# Commit the changes to the database and close the connection
conn.commit()
cursor.close()
conn.close()