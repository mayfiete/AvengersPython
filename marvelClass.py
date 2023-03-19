
import requests
import hashlib
import datetime
from random import randint
import json
from collections import Counter


class Marvel():

    def __init__(self, public_key, private_key):
        # private_key and public_key are used to generate an md5 hash string
        self.private_key = private_key
        self.public_key = public_key
        self.baseURI = "http://gateway.marvel.com/v1/public"
        # self.hashed_String,self.timestamp = self.md5_Hash()
        self.hashed_String = self.md5_Hash()
        self.hash_input = self.md5_Hash()
        self.url_params = {
            'ts': self.timestamp,
            'apikey': self.public_key,
            'hash': self.hashed_String,
        }

    def fetch_characters(self, name="Wolverine", limit=1000):
        self.baseURI += "/characters?name={}".format(name)
        # print(self.baseURI)
        resp = requests.get(self.baseURI, params=self.url_params)
        return resp.json()

    def fetch_characters_by_id(self, char_id="1009652", limit=1000):
        # limit specifies how  many items to display
        if limit is not None:
            self.url_params['limit'] = limit
        self.char_id = char_id
        # add the item in the param payload
        self.baseURI += "/characters" + "/{}".format(self.char_id)
        resp = requests.get(self.baseURI, params=self.url_params)
        # print(resp.url)
        return resp.json()

    def md5_Hash(self):
        '''
        hash changes everytime this function is called.
        returns hashed string and a timestamp
        '''
        self.timestamp = '{:%Y%m%d%H%M%S}'.format(
            datetime.datetime.now())  # generate a timestamp
        self.hash_input = self.timestamp + self.private_key + self.public_key
        self.hashed_String = hashlib.md5(self.hash_input.encode(
            'utf-8')).hexdigest()  # generate md5 hash
