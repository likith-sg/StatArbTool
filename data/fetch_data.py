from binance.client import Client
import pandas as pd
import os
from config import BINANCE_API_KEY, BINANCE_SECRET

client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_SECRET)

def get_historical_data(symbol, interval='1h', limit=1000):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume", "_", "_", "_", "_", "_", "_"
    ])
    df["close"] = df["close"].astype(float)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df[["timestamp", "close"]] 
