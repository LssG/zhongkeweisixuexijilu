from matplotlib import pyplot, rcParams
import pandas
import numpy
import requests
rcParams.update({'font.size': 10, 'font.family': 'SimHei', "axes.unicode_minus": False})

# testarr = ["aaa", "fff", "ddd"]
# test = pandas.DataFrame({"name": testarr, "val": 1})
# test = test.append(pandas.DataFrame([{"name": testarr, "val": 1}]))
# print(test)

data = pandas.read_csv("movie_metadata.csv", encoding="GBK")#.reindex(index=numpy.arange(0, 100))
# print(data)

data = data.reindex(columns=["genres", "movie_facebook_likes"])
# print(data.ftypes)
# print(type(data["movie_facebook_likes"][0]))

redata = pandas.DataFrame()


def splitData(datas):
    global redata
    tmpstrs = datas["genres"].split("|")
    tmpdf = pandas.DataFrame({"genres": tmpstrs, "movie_facebook_likes": ([datas["movie_facebook_likes"]]*len(tmpstrs))})
    # print(tmpdf.ftypes)
    # print(tmpstrs)
    # print(tmpdf)
    redata = redata.append(tmpdf)
    # print(redata.ftypes)
    # print(type(datas["movie_facebook_likes"]))

data.apply(splitData, axis=1)
# print(redata.ftypes)
print("redata ok")
# print(redata)

redata = redata.reset_index(drop=True)

regroups = redata.groupby("genres")
# print(regroups.groups)

re = regroups.agg({"movie_facebook_likes": ["mean", "count", ]})["movie_facebook_likes"]
print(re)

# print(re.index)
pyplot.figure(figsize=(8, 8), dpi=100)
pyplot.subplot(2, 1, 1)
pyplot.grid()
pyplot.title("平均like数")
pyplot.plot(re['mean'])
pyplot.xticks(rotation='vertical')
pyplot.gcf()
pyplot.subplot(2, 1, 2)
pyplot.grid()
pyplot.title("电影总数")
pyplot.plot(re['count'])
pyplot.xticks(rotation='vertical')
pyplot.savefig("2019_08_08.jpg", dpi=100)
pyplot.show()

print("done")
