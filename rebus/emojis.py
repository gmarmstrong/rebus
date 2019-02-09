import requests
import json
import urllib3
import emoji
from emoji import emojize
import sys
import emoji_data_python
import nltk
from nltk import corpus
from nltk.corpus import wordnet

urllib3.disable_warnings()
http = urllib3.PoolManager()

def get_emoji(word):
    return emoji.emojize(":" + word + ":",use_aliases=True)

def to_emoji(word):
    str = get_emoji(word)
    if (str[0] != ':'):
       return str
    homophones = json.loads(http.request('GET', 'https://api.datamuse.com/words?sl=' + word).data.decode('utf-8'))
    i = 0
    while ( i < len(homophones) and homophones[i]["score"] == 100 ):
        str = get_emoji(homophones[i]["word"])
        if(str[0] != ':'):
            return str
        i += 1
    return word