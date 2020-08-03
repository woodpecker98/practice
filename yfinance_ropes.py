import yfinance as yf  # good for historical research
import pandas as pd

tickerSymbol = input("Ticker Symbol: ")
tickers = ["FB", "TSLA"]
print(yf.download(tickerSymbol, start="2020-07-30", end="2020-08-02"))
