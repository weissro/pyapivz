#!/usr/bin/python3

import pprint
import requests

def main():
    r = requests.get("http://anapioficeandfire.com/api/books")
    pprint.pprint(r.json())# strip off json and display on screen


main()
