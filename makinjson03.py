#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "zaphod beeblebrox", "species": "betelgeusian"}, {"name": "arthur dent", "species": "human"}, {"name": "ford prefict", "species": None}]

# in json, this would be an array of objects

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

    myhitchhikers=json.dumps(hitchhikers)
    print(myhitchhikers)
# dump puts into a file, dumps puts it in locally

main()

