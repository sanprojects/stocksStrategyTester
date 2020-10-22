import yfinance, httpHelper
import pandas as pd

httpHelper.enableLogger()
httpHelper.enableCache()

pd.options.mode.chained_assignment = None  # default='warn'
cache = {}

def get(ticker='AAPL', period='100y', start=None, end=None, fromCache=True):
    if fromCache and ticker in cache:
        return cache.get(ticker)

    company = yfinance.Ticker(ticker)
    cache[ticker] = company.history(period=period, start=start, end=end)
    return cache[ticker]


def getByDate(ticker, date):
    try:
        df = get(ticker)
        return df.iloc[df.index.get_loc(date, method='pad')]
    except KeyError:
        return


def getDateIndex(history, date):
    return history.index.get_loc(date)