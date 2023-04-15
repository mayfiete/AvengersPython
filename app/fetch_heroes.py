
import requests
import json
import hashlib
import datetime
import os
from MarvelClass import Marvel

# In real life, you would not store your keys in the code.
# Instead, you would store them in a configuration file or environment variables.

# Define API endpoint and authentication keys
# optimization: use environment variables

public_key = "dda446b2e1c24ad15b95764453ea581f"
private_key = "981b3c906e07a0d1f4acf631bf103087b13099c6"

# Retrieve the public and private keys from environment variables
# public_key = os.environ.get("MARVEL_PUBLIC_KEY")
# private_key = os.environ.get("MARVEL_PRIVATE_KEY")

if not public_key or not private_key:
    raise ValueError(
        "MARVEL_PUBLIC_KEY or MARVEL_PRIVATE_KEY environment variable is not set.")

x = Marvel(public_key, private_key)


# import names from the hero_names.txt file, parse commas and new lines
file_name = 'C:/AvengersPython/app/hero_names.txt'
print(file_name)
with open(file_name) as f:
    # need to loop through the names in the hero_names.txt file
    names = f.read().splitlines()
    for name in names:
        split_name = name.split(',')
        for single_name in split_name:
            row = x.fetch_characters(single_name.strip(), 20)
            print("Comic Character: ", row)
            print(single_name)
            with open('C:/AvengersPython/marvel.json', 'w') as outfile:
                json.dump(row, outfile)
                outfile.write(' ')


# The following code is for testing purposes only

# the following variables can be passed to the os and used by the fetch_heroes function
# export MARVEL_PUBLIC_KEY="dda446b2e1c24ad15b95764453ea581f"
# export MARVEL_PRIVATE_KEY="981b3c906e07a0d1f4acf631bf103087b13099c6"
