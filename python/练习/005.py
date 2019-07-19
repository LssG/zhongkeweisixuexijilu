import re
import random

def string2Dict(string):
    string = string.replace('{', "")
    string = string.replace('}', "")
    string = string.replace('"', "")
    arr1 = string.split(",")
    arr2 = []
    for i in range(len(arr1)):
        arr2.append(arr1[i].split(":"))
    re = dict(arr2)
    return re

def parseV(string):
    re = []
    if len(string) > 0:
        re = string.split("&")
    return re

data = {"primary":{"crm_view":"add_time"},"vice":'{"service_conversation":"update_time"}&{"service_xx":"time"}&{"service_vv":"update"}',"relation":"2"}
data["vice"] = parseV(data["vice"])

print(data)

string = "12345\t67890"
print(string.center(13,'a'))
print(string)
print(string.expandtabs(5))
print(string)

def fun(string):
    return string
arr = []
print(f"{id(arr)},{id(fun(arr))}")

def fun2():
    pass
print(fun2())
print(type(fun2()))

string = "一二三"
print(string)
print(string.isalnum())
print(string.isnumeric())
print(string.isdigit())

string = "Aasd AsaDasd"
print(string.istitle())

print(string.upper())
print(string)
print(string.expandtabs(5))
print(string)

string = '{"service_conversation":"update_time","name":"xiaoming"}'
print(type(string2Dict(string)))
print(string)


trans = string.maketrans("a","|")
print(string.translate(trans))

string = "    \t   \n   \t"
print(string.isspace())

string = "发货款的福建卡"
print(string.isalpha())

string = "jkhasiyujljkdfkljfklsdaYguZcvnaiuvuiyaw"
print(string.find("as"))
print(string.rfind("as"))

print(max(string.swapcase()))

def ti2(string):
    return string.replace("枪","*").replace("毒","%")

# arr = [333,222,1]
# for i,j in arr:
#     print(i,j)

x = 1
y = 2
z = 3


# a = int(input("输入数字a："))
# b = int(input("输入数字b："))
# c = "="
# if a>b:
#     c = ">"
# elif a < b:
#     c = "<"
# print (a,c,b)


string = "kjhHKJgfsakjhLKJH"
tmpstring = string.upper()
sum = 0
for i in range(len(string)):
    if string[i] == tmpstring[i]:
        sum += 1
print(sum)
print()

reArr = []
re = 0
while len(reArr) < 6:
    tmp = random.randint(0,9)
    for j in reArr:
        if j == tmp:
            break
    else:
        reArr.append(tmp)
        re = re*10 + tmp
re = str(re)
print(re)
print()

old_list = [1,1,1,3,4]
for i in range(len(old_list)):
    for j in old_list[0:i]:
        if j == old_list[i]:
            old_list[i] = " "
while " " in old_list:
    old_list.remove(" ")
print (old_list)
print()

def fun(listName):
    return listName[2]
arr = [(5,88,2,444,7),(88,22,34,66,8),(44,2,66,7,88)]
arr.sort(key=fun)
print(arr)
print()

# 如：content = input(‘请输入内容:’)  # 如用户输入：5+8+7....(最少输入两个数相加)，然后进行分割再进行计算，将最后的计算结果添加到此字典中(替换None)：
# dic={‘最终计算结果’:None}。

# content = input('请输入内容:')
# arr = content.split("+")
# dic={'最终计算结果':None}
# sum = 0
# for i in arr:
#     sum += int(i)
# dic['最终计算结果'] = sum
# print(f"最终计算结果:{dic['最终计算结果']}")
#
# print("a"<"b")

arr = [1,2,3,4,56]
for i in arr:
    i = 2
print(arr)

string = "0123456789"
print(string.rfind("23", 0, 4))

string = "开始附带将发挥空间这拉斯"
print(max(string))
print(min(string))