def str2Dict(string):
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

str = "12345\t67890"
print(str.center(13,'a'))
print(str)
print(str.expandtabs(5))
print(str)

def fun(str):
    return str
arr = []
print(f"{id(arr)},{id(fun(arr))}")

def fun2():
    pass
print(fun2())
print(type(fun2()))

str = "一二三"
print(str)
print(str.isalnum())
print(str.isnumeric())
print(str.isdigit())

str = "Aasd AsaDasd"
print(str.istitle())

print(str.upper())
print(str)
print(str.expandtabs(5))
print(str)

str = '{"service_conversation":"update_time","name":"xiaoming"}'
print(type(str2Dict(str)))
print(str)

