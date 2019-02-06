import json
import random
import urllib.request
import ast
#import requests



# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"

def download():
    """ This function downloads the json data from the url."""
    jsonurl = urlopen(url)
    text = json.loads(jsonurl.read())
    text = json.dumps(text,separators=(',',':'))
    return (text);
  

def extract_requests(text: str) -> List[Dict[str, Any]]:
    """l
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """


    text2 = ast.literal_eval(text)
    return text2['promises']


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    Titles = []
    for i in promises:
        Titles.append(i['title'])

    return Titles

def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    random.choice(titles)
    return random.choice(titles)
