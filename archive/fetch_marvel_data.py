

import requests
import json
import hashlib
import datetime
from random import randint
import pyodbc
from MarvelClass import Marvel

# Define API endpoint and authentication keys
# optimization: use environment variables
API_ENDPOINT = "https://gateway.marvel.com:443/v1/public/characters"
public_key = "dda446b2e1c24ad15b95764453ea581f"
private_key = "981b3c906e07a0d1f4acf631bf103087b13099c6"

x = Marvel(public_key, private_key)

timestamp = '{:%Y%m%d%H%M%S}'.format(
    datetime.datetime.now())  # generate a timestamp
hash_input = timestamp + private_key + public_key
hashed_String = hashlib.md5(hash_input.encode(
    'utf-8')).hexdigest()  # generate md5 hash

hashed_String = md5_Hash()
hash_input = md5_Hash()
hash_key = {
    'ts': datetime.datetime.now().timestamp(),
    'apikey': public_key,
    'hash': hashed_String
}

# Hash the keys using SHA-256
# public_key_hashed = hashlib.sha256(public_key.encode()).hexdigest()
# private_key_hashed = hashlib.sha256(private_key.encode()).hexdigest()

# Define output file path and format
OUTPUT_FILE = "/path/to/output/file.txt"
OUTPUT_FORMAT = "{key}:{value}\n"

# Define API parameters and headers
params = {"name": "Wolverine"}
headers = {"Authorization": f"ApiKey {public_key}"}

# Hash the keys using SHA-256


# Make API request and get response
response = requests.get(API_ENDPOINT, params=params, headers=headers)

x = API_ENDPOINT + "?name=Wolverine&apikey=" + \
    public_key + "&hash=" + str(hash)

print(x)

# Check if request was successful
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
else:
    # Parse JSON response
    data = json.loads(response.text)

    # Write data to output file
    with open(OUTPUT_FILE, "w") as f:
        for key, value in data.items():
            f.write(OUTPUT_FORMAT.format(key=key, value=value))
