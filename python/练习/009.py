from calendar import calendar,month,weekday
import re

print(calendar(2019))
print (month(2019,7))
print (weekday(2019,7,1))

def fun():
    for i in range(10):
        print(f"fun():{i}")
        yield i

g = fun()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

tmp = re.search(r".[az]$","1231412dxaz")
print (tmp)

tmp = re.findall(r"\d+","fasd76a8dsga6875g89a76d9f8a7f")
print (tmp)

tmp = re.match(r"(\d+):(\d+).(\d+) (\D+)","00:10:10 歌词")
print(tmp)
print(tmp.group(1))


