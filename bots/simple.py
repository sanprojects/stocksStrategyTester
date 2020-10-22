"""Strategy: buy every 30 days 1 share"""
import bot


class SimpleBot(bot.Bot):
    ticker = '^GSPC'  # S&P500

    def onTick(self):  # runs every day
        if (self.index % 30) == 0:
            self.buy(self.ticker, 1)
