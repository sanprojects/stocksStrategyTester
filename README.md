# Python stocks strategy tester
Bots framework for stocks strategy testing. History automatically downloads from yahoo finance.  

## Install requirements

```shell
./manager.sh install
```

## Simple bot example
Strategy: buy every 30 days 1 share. See [bots/simple.py](bots/simple.py)   
```python
import bot


class SimpleBot(bot.Bot):
    ticker = '^GSPC'  # S&P500

    def onTick(self):  # runs every day
        if (self.index % 30) == 0:
            self.buy(self.ticker, 1)

```
Run bot
```shell
python3 run.py bots/simple.py start=2020-01-01 end=2020-09-30
```
Output:
```
2020-01-30 00:00:00 Buy     1 ^GSPC for $3,283.66
2020-02-29 00:00:00 Buy     1 ^GSPC for $2,954.22
2020-03-30 00:00:00 Buy     1 ^GSPC for $2,626.65
2020-04-29 00:00:00 Buy     1 ^GSPC for $2,939.51
2020-05-29 00:00:00 Buy     1 ^GSPC for $3,044.31
2020-06-28 00:00:00 Buy     1 ^GSPC for $3,009.05
2020-07-28 00:00:00 Buy     1 ^GSPC for $3,218.44
2020-08-27 00:00:00 Buy     1 ^GSPC for $3,484.55
2020-09-26 00:00:00 Buy     1 ^GSPC for $3,298.46
2020-09-30 00:00:00 Sell   -9 ^GSPC for $-30,267.00
Tested 2020-01-01 00:00:00 -> 2020-09-30 00:00:00 (273 days)
Spent: $27,858.85 profit: $2,408.15 average profit per year: $3,219.69 (11.56%)
```



