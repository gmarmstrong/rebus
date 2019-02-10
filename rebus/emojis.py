import json
import urllib3
import emoji
from emoji import emojize

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

def emojify(words):
    arr = words.split()
    string = ""
    for word in arr:
        string += to_emoji(word) + " "
    return string[:int(len(string)-1)]
