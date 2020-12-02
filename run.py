"""Usage: python run.py bots/simple.py start=2020-01-01 param1=value1 param2=value2"""
import sys, utils


args = utils.utils.getArgs()
bot = utils.utils.loadClass(sys.argv[1])(**args)
bot.run()
