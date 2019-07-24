import time
import threading

class Date:
    @classmethod
    def toHHMMSS(cls,timeTup):
        return "%02d:%02d:%02d"%(timeTup[3],timeTup[4],timeTup[5])

ts = time.time()
print (ts)

timeTup = time.localtime(ts)
print(timeTup)
print(type(timeTup))

print ("%02d:%02d:%02d"%(timeTup[3],timeTup[4],timeTup[5]))
Date.toHHMMSS(timeTup)

def doSomething():
    print (Date.toHHMMSS(time.localtime(time.time())))

timer = threading.Timer(0.01,doSomething)
timer.start()

def clock():
    print(Date.toHHMMSS(time.localtime(time.time())))
    timer = threading.Timer(1,clock)
    timer.start()

# clock()

def naoZhong(timeStr):
    sec = 0
    ptext = ""
    text = ["小时","分钟","秒"]
    tmp = timeStr.split(":")
    for j,i in enumerate(tmp):
        i = int(i)
        sec += sec * 60 + i
        if i > 0:
            ptext += str(i)+text[j]
    if ptext:
        print(f"{ptext}后叫你起床！")
    else:
        print("马上起床！")
    def qiChuang():
        print("起床了！")
    timer = threading.Timer(sec,qiChuang)
    timer.start()

naoZhong("00:10:00")