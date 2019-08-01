import re
import requests

URL = "https://m.qxs.la"
URLend = "/157739/12220123/"
file = open("武炼巅峰.txt", "w+", encoding="utf-8")
index = 1

for i in range(200):
    res = requests.get(URL+URLend)

    html = res.text

    wenben = re.search(r"<div class=\"n-title\">(.*?)</div>", html, re.S).groups(1)[0]

    zhengze = r"<div class=\"n-chapter\" id=\"content\">(.*?)</div>"

    wenben += re.search(zhengze, html, re.S).groups(1)[0]
    wenben = wenben.replace("\r\n\r\n", "\r\n")
    wenben = wenben.replace("<br/>", "\n")
    wenben = wenben.replace("\t", "\n")

    # print(wenben)
    file.write(wenben)

    URLend = re.search(r"<div class=\"n-prenext\">.*(?:<a href=\")(.*?)\">下一页", html, re.S).groups(1)[0]

    print(f"{index} ok")
    index += 1

file.close()
# print(URLend)

