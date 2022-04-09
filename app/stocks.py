

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv

from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data


load_dotenv()

df = fetch_stocks_data

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
