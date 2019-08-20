#!/usr/bin/python3

from pprint import pprint
import requests

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=LMT&interval=5min&apikey=GULGPASXGY2VVUP0"
    stockdata = requests.get(mylookup)
    decodedstockdata = stockdata.json()
    

main()

