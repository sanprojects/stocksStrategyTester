"""Usage: python run.py bots/simple.py start=2020-01-01 param1=value1 param2=value2"""
import inspect, sys, os, pandas


def getArgs():
    result = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            sep = arg.find('=')
            key, value = arg[:sep], arg[sep + 1:]
            result[key] = value
    return result


def loadClass(name):
    path = os.path.abspath(name)
    moduleName = os.path.basename(path).split('.')[0]
    sys.path.insert(1, os.path.dirname(path))
    module = __import__(moduleName)
    classes = inspect.getmembers(module, inspect.isclass)
    return classes[0][1]

args = getArgs()
bot = loadClass(sys.argv[1])(**args)
bot.run()