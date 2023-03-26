
import pymongo
import csv

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
db = client["marvel_heroes"]

# Select the collection
collection = db["superheroes"]

# Open the CSV file and read its contents
with open('C:/Interview/Avengers/AvengersPython/marvel.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader)  # skip the header row
    rows = [row for row in reader]


# Insert the data into the collection
# collection.insert_many(rows)
for row in rows:
    name, comic = row
    collection.insert_one({"name": name, "comic": comic})

# Close the connection to the MongoDB server
client.close()
