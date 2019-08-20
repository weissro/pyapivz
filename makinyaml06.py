#!/usr/bin/python3

import yaml


def main():
    hitchhikers = [{"name": "zaphod beeblebrox", "species": "betelgeusian"}, {"name": "arthur dent", "species": "human"}, {"name": "ford prefict", "species": None}]

    mystr = yaml.dump(hitchhikers)
    print(mystr)

main()

