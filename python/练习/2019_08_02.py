from matplotlib import pyplot, rcParams
import random
import numpy as np

np.set_printoptions(suppress=True)

rcParams.update({'font.size': 10, 'font.family': 'SimHei', "axes.unicode_minus": False})

priceData = np.loadtxt("data.csv", delimiter=",", skiprows=3, usecols=7)
numData = np.loadtxt("data.csv", delimiter=",", skiprows=3, usecols=9)
print(priceData)
print(numData)
mData = priceData * numData
print(mData)

# x = 1
# def c(a):
#     x+=1
#     print(x)
# c(x)

x = [1,2,3,4,5]
x.pop(2)
print(x)
x = 0
y = 2
z = 3
print(x>y>z)

arr = np.array([
    [1,2 ,3 , 6,0 ],
    [1,2 ,3 , 3, 3],
    [4, 5,6 ,1 ,2 ]
])
np.sort(arr, axis=0)

a = [1,2,3,4,5,67]
b = a[2:4]
print(a,b)
b = [9,9,9,9,9]
print(a,b)

a = {"a":1,"a2":1,"a4":1,"a5":1,"a6":1}
print(a.keys())
print(a.items())

dic = {
    "name": "小明",
    "age": 18,
    "friends": [
        {
            "name": "小明",
            "age": 19
         }
    ]
}
friends = dic["friends"]
f = {"name": "小亮","age": 100}
friends.append(f)
print (dic["friends"])

# a = np.array([
#     [35,20,26,30,19,16,30],
#     [33,10,16,13,17,15,20],
#     [30,25,26,30,29,26,29]
# ])
#
# pyplot.plot(range(7),a[0])
# pyplot.plot(range(7),a[1])
# pyplot.plot(range(7),a[2])
# pyplot.legend({"第一周","第二周","第三周"},loc="best")
# pyplot.grid(axis="both")
# pyplot.show()

re = np.random.randint(1, 30, size=(4, 4, 4))
np.save("data.s", re)
# print(re.size)
# print(re.itemsize)
