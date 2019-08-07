import numpy
import pandas
import requests
import time

def fun(str):
    re = str
    print(id(re))
    return lambda: re

x = fun("asd")
print(x())
fun("dd")
print(x())

arr = numpy.random.randint(0,10,(2,5))
print(arr)

pd = pandas.DataFrame([[2, 3, 8, 2, 4, 64],
                       [4, 9, 8, 128, 32, 128]])
print(pd, "\n")

print(pd.mode(axis=0))

df = pandas.DataFrame(numpy.random.randint(0, 100, (2, 15,)), index=["a", "b"])
print(df)

data = pandas.read_csv("movie_metadata.csv", encoding="utf-8")
print(data)
print(data.reindex(columns=["movie_title", "duration"]))

def fun2(a,b,c):
    return a+b-c

df = pandas.DataFrame(numpy.random.randint(0, 100, (2, 15,)))
print(df)
print(df.pipe(fun2, 10, 20))

 