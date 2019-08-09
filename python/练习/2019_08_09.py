import numpy
import pandas
from matplotlib import pyplot,rcParams
import MySQLdb

con = MySQLdb.connect(host="47.92.2.94", user="liuyujing", password="123456", database="chandao", port=3306, db="candao")

def getData(table, cols):
    cursor = con.cursor()
    sql = f"select "
    for tmp in range(len(cols)):
        if tmp > 0:
            sql += ","
        sql += cols[tmp]
    sql += f" from {table}"
    print(sql)
    cursor.execute(sql)
    result = list(cursor.fetchall())
    re = pandas.DataFrame(data=result, columns=cols)
    return re
data = getData("zt_action", ["actor", "action"])
print(data)

groups = data.groupby(["actor", "action"])
print(groups.groups)
groups.agg({})

# print(f"{['asd','fff']}")

con.close()
