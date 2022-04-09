
import os
import json
from dotenv import load_dotenv
import requests


load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

def fetch_crypto_data(symbol):
    symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return(parsed_response)

def fetch_unemployment_data(symbol):
    symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    df = read_csv(url)
    return df

def fetch_unemployment_data():
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response
