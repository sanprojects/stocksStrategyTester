import sys
sys.path.append('.')
import bot, pandas


class SimpleBot(bot.Bot):
    def onTick(self):
        # buy every 30 days shares for 300$
        if (self.index % 30) == 0:
            self.buy('^GSPC', 300 / self.getPrice('^GSPC').Close)


for date in pandas.date_range(start='2020-03-30', end='2020-10-02'):
    SimpleBot(start=date, end='2020-10-02').run()
