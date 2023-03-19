
import requests
import json
import hashlib
import datetime
# from random import randint
from MarvelClass import Marvel

# Define API endpoint and authentication keys
# optimization: use environment variables

public_key = "dda446b2e1c24ad15b95764453ea581f"
private_key = "981b3c906e07a0d1f4acf631bf103087b13099c6"
x = Marvel(public_key, private_key)

row = x.fetch_characters('Human Torch', 20)
print("Comic Character: ", row)

# write to a file
with open('marvel.json', 'a') as f:
    json.dump(row, f)
