from matplotlib import pyplot,font_manager
import random

x = range(11, 22)
y = []
for i in x:
    y.append(random.randint(0,3))
font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\硬笔行书130106.ttf")
pyplot.title("从10岁到现在每年养宠物的数量",fontproperties=font)
pyplot.plot(x,y)
pyplot.xlabel("岁数",fontproperties=font)
pyplot.ylabel("宠物数量",fontproperties=font)
pyplot.show()

x = range(1, 8)
y = []
for i in x:
    y.append(random.randint(0,30))
font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\硬笔行书130106.ttf")
pyplot.title("当年每月与女友或男友的约会次数",fontproperties=font)
pyplot.plot(x,y)
pyplot.xlabel("月份",fontproperties=font)
pyplot.ylabel("约会次数",fontproperties=font)
pyplot.show()


x = range(1, 8)
y = []
for i in x:
    y.append(random.randint(0,30))
font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\硬笔行书130106.ttf")
pyplot.title("你与朋友当年约会次数的对比",fontproperties=font)
pyplot.plot(x,y)
y = []
for i in x:
    y.append(random.randint(0,30))
pyplot.plot(x, y)
pyplot.xlabel("月份",fontproperties=font)
pyplot.ylabel("约会次数",fontproperties=font)
pyplot.show()

