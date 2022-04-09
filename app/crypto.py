


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests

from app.utils import to_usd
from app.alphavantage_service import fetch_crypto_data

load_dotenv()

parsed_response = fetch_crypto_data()

tsd = parsed_response["Time Series (Digital Currency Daily)"]

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
