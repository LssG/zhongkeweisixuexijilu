# 座机电话格式：
#xxxx-xxxxxxx

import re

inStr = input("请输入要判断的电话号码：")
tmp = re.match(r"^\d{4}-\d{7}$",inStr)
print ("是座机号（大概）！" if tmp else "不是座机号（确信）！")