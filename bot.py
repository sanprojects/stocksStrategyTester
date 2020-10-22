import history, logging
import pandas as pd


class Bot:
    def __init__(self, start='2020-01-01', end='2020-10-02', **args):
        self.money = 0
        self.index = 0
        self.date = ''
        self.shares = {}
        self.start = start
        self.end = end
        for k, v in args.items():
            setattr(self, k, v)

    def getPrice(self, ticker):
        return history.getByDate(ticker, self.date)

    def buy(self, ticker, count=1):
        self.shares[ticker] = self.shares.get(ticker, 0) + count
        cost = self.getPrice(ticker).Close * count
        self.money -= cost
        orderType = 'Buy ' if count > 0 else 'Sell'
        print(f'{self.date} {orderType} {round(count,3):4} {ticker} for ${cost:,.2f}')

    def sell(self, ticker, count=1):
        self.buy(ticker, -count)

    def sellAll(self):
        for ticker, count in self.shares.items():
            self.sell(ticker, count)

    def step(self):
        self.index += 1
        try:
            self.onTick()
        except Exception as e:
            logging.error(e, exc_info=True)

    def run(self):
        self.minDate = pd.to_datetime(self.start)
        self.maxDate = pd.to_datetime(self.end)
        for date in pd.date_range(start=self.start, end=self.end):
            self.date = date
            self.step()

        self.onStop()

    def onTick(self):
        pass

    def onStop(self):
        self.printSummary()

    def printSummary(self):
        spentMoney = -self.money
        self.sellAll()
        profitPercent = (self.money / spentMoney * 100) if spentMoney else 0
        days = pd.Timedelta(self.maxDate - self.minDate).days
        days = days if days else 0.000000000001
        profitPerYear = (self.money / days) * 365
        profitPercentPerYear = (profitPercent / days) * 365
        # print(vars())
        print(f'Tested {self.minDate} -> {self.maxDate} ({days} days)')
        print(f'Spent: ${spentMoney:,.2f} profit: ${self.money:,.2f} average profit per year: ${profitPerYear:,.2f} ({profitPercentPerYear:,.2f}%)')
