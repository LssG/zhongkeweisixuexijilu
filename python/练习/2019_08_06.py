import numpy
import pandas
import requests
import time

# s = pandas.Series([])
# print(s)
#
# s = pandas.Series([1, 2, 3, 4], index=["jj", "poi", "gyi", "asd"])
# print(s[0])
#
# arr = numpy.random.randint(0, 100, (4, 5))
# s = pandas.DataFrame(arr)
#
# print(s)
#
# print(s.iloc[0])
#
# print(s.count())

def sortFun(item):
    return item["time"]

def getTime(d):
    t = time.localtime(int(d["time"]))
    return time.strftime("%H:%M:%S", t)

url = "https://www.btctrade.com/api/coindata/currency_price_trend"
args = {"currency": "btc", "unit": "CNY", "type": "day", "language": "zh_cn"}

res = requests.get(url, params=args).json()
data = res["data"]
print(data)
for i in data:
    print(getTime(i), i["net_price"])

data = pandas.DataFrame(data)
print(data)

print(data["net_price"].min())
print(data["net_price"].max())

dic = {"asd":sortFun}
print (dic.sortFun)
