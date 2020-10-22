"""Strategy: Buy when price fallen"""
import bot, history


class BuyFallenBot(bot.Bot):
    ticker = 'AAPL'
    threshold = 2.0  # %
    lastPrice = lastMa = 0

    def __init__(self, **args):
        super().__init__(**args)
        df = history.get(self.ticker)  # get history dataframe
        df['ma'] = df['Close'].rolling(window=50).mean()  # add moving average 50 for trend detection

    def onTick(self):
        price = self.getPrice(self.ticker).Close
        ma = self.getPrice(self.ticker).ma
        priceDiff = (self.lastPrice - price) / price * 100

        if (ma > self.lastMa # ma grown - it mean upward trend
                and priceDiff > self.threshold): # price down to threshold %
            # print(self.date, self.lastPrice, '->', price, diffInPercent, self.getPrice(self.ticker).ma)
            self.buy(self.ticker, 1)

        self.lastPrice = price
        self.lastMa = ma
