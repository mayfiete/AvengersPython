
# use pandas to read the json file
import pandas as pd
import json

# read the json file
df = pd.read_json('C:\Interview\Avengers\marvel.json')

# view the dataframe
print(df.head())


# convert the json file to csv
df.to_csv('C:\Interview\Avengers\marvel.csv', index=False)

# extract results from the json file
results = df['data']['results']  # returns a list of dictionaries
name = results[0]['name']  # returns the name of the first dictionary
# returns the collectionURI of the first dictionary
collectionResource = results[0]['comics']['items']

print(name)
# print(results)


iterator = df['data']['limit']  # limit the number of results
print(int(iterator))

# loop through the results and print the name of each resourceURI
for i in range(20):
    print(collectionResource[i]['name'])
