
# use pandas to read the json file
import pandas as pd
import json

# read the json file
df = pd.read_json('C:\AvengersPython\marvel.json')

# view the dataframe
# print(df.head())

# extract results from the json file
results = df['data']['results']  # returns a list of dictionaries
try:
    print(results[0]['name'])
    hero = results[0]['name']  # returns the name of the first dictionary
    heroId = results[0]['id']  # returns the name of the first dictionary
except IndexError:
    print("Index out of range!")
    exit()  # exit the program

# returns the collectionURI of the first dictionary
collectionResource = results[0]['comics']['items']
# print(collectionResource)

iterator = df['data']['limit']  # limit the number of results
print(int(iterator))

# loop through the results and print the name of each resourceURI
for i in range(int(iterator)):
    print(collectionResource[i]['name'])
    # write to csv file
    with open('C:\AvengersPython\marvel.csv', 'w') as f:
        json.dump(hero, f)
        f.write('|')
        json.dump(collectionResource[i]['name'], f)
        f.write('|')
        json.dump(heroId, f)
        # add a new line
        f.write('\n')
