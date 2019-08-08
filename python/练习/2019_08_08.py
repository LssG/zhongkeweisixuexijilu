import numpy
import pandas
from matplotlib import pyplot,rcParams
rcParams.update({'font.size': 10, 'font.family': 'SimHei', "axes.unicode_minus": False})
pandas.set_option('display.max_columns', None)

# df1 = pandas.read_csv("2019_08_08_data1.csv", encoding="GBK")
# df2 = pandas.read_csv("2019_08_08_data2.csv", encoding="GBK")
# df = df1.append(df2)
#
# print(df1, "\n")
# print(df2, "\n")
# print(df, "\n")
#
# print(df.sort_index(), "\n")
#
# print(df1.sort_values(by="age"), "\n")
#
# group = df1.groupby(("class", "name"))
# print(group.get_group(), "\n")
# g1 = group.get_group("1班")
# g2 = group.get_group("2班")
# g3 = group.get_group("3班")
# print(g1["name"], "\n")
#
# g1 = g1.reset_index(drop=True)
#
# g1.plot()
# pyplot.xticks(g1["name"].index, labels=g1["name"])
# pyplot.show()

# data = pandas.read_csv("2019_08_08_data3.csv", encoding="GBK", skiprows=[0, 2]).reindex(columns=["title", "price", "num", "has_showcase"])
# print(data)
#
# groups = data.groupby("has_showcase")
# print(groups.get_group(0).count(0, ))

# data = pandas.read_csv("movie_metadata.csv", encoding="utf-8", )
# print(data.keys())
# # print(data['director_name'])
#
# groups = data.groupby("country")
# print(groups.get_group("China")["movie_title"])
# # print(groups.get_group("China").shape)

data1 = pandas.read_csv("2019_08_08_data1.csv", encoding="GBK")
data2 = pandas.read_csv("2019_08_08_data2.csv", encoding="GBK")

print(data1)
print(data2)
print(data1.merge( data2, on=["class", "name"], how="outer"))
