# python数据分析
## 基础概念
为什么要学习数据分析
> 有岗位需求  
> 是python数据科学的基础  
> 是机器学习课程的基础

是什么
> 数据分析是用适当的方法对收集来的大量数据进行分析，帮助人们作出判断，以便采取适当行动。

数据分析的流程
> 提出问题  
> 准备数据  
> 分析数据  
> 获得结论  
> 成果可视化，或对结果进行进一步的分析

## matplotlib
用于图形化数据
### 使用步骤
1. 准备数据
2. 设置要绘制的内容
3. 显示要绘制的内容
### 基本要点
基础语法
```
from matplotlib import pyplot

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
pyplot.plot(x, y)
pyplot.show()
```
设置线的样式
>语法
```
pyplot.plot(x,[1,2,3,4,5],"3")
```
>样式
>> '-' 实线样式  
'--' 短横线样式  
'-.' 点划线样式  
':' 虚线样式  
'.' 点标记  
',' 像素标记  
'o' 圆标记  
'v' 倒三角标记  
'^' 正三角标记  
'<' 左三角标记  
'>' 右三角标记  
'1' 下箭头标记  
'2' 上箭头标记  
'3' 左箭头标记  
'4' 右箭头标记  
's' 正方形标记  
'p' 五边形标记  
'*' 星形标记  
'h' 六边形标记 1  
'H' 六边形标记 2  
'+' 加号标记  
'x' X 标记  
'D' 菱形标记  
'd' 窄菱形标记  
'|' 竖直线标记  
'_' 水平线标记

>设置颜色
语法
```
pyplot.plot(x,[1,2,3,4,5],"--",color='c')
```
>类型
>> 'b' 蓝色  
'g' 绿色  
'r' 红色  
'c' 青色  
'm' 品红色  
'y' 黄色  
'k' 黑色  
'w' 白色  

设置线的透明度
```
pyplot.plot(x,[1,2,3,4,5],"--",color='c',linewidth=5)
```

设置图表的标题
```
  pyplot.title("haha")
```
设置X\Y轴的标题
```
pyplot.xlabel("X轴", color="m")
```
设置图片大小
```
pyplot.figure(figsize=(20, 80), dpi=80)
```
>1. num:这个参数是一个可选参数，即可以给参数也可以不给参数。可以将该num理解为窗口的属性id,即该窗口的身份标识。
>如果不提供该参数，则创建窗口的时候该参数会自增，如果提供的话则该窗口会以该num为Id存在。
>2. figsize:可选参数。整数元组，默认是无。
提供整数元组则会以该元组为长宽，若不提供，默认为 rc fiuguer.figsize
例如（4，4）即以长4英寸 宽4英寸的大小创建一个窗口
>3. dpi：可选参数，整数。表示该窗口的分辨率，如果没有提供则默认为 figure.dpi

重新设置x轴刻度
```
pyplot.xticks(x)
```
保存图片
```
pyplot.savefig("./img.png")
```
查看系统支持的资体
```
print(font_manager.findSystemFonts())
```
设置中文字体
```
font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simfang.ttf")
pyplot.xlabel("时间", fontproperties=font) 
pyplot.ylabel("温度", fontproperties=font)
```
在同一张表里 有多条数据
```
font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simfang.ttf") 
x = range(0, 4) y = [55, 58, 22, 66]  
xTitle = ["1号", "2号", "3号", "4号"] 
pyplot.xticks(x, xTitle, fontproperties=font,color="m") 
pyplot.plot(x, y) 
# 在同一张表里  有多条数据 
y = [20, 40, 60, 50] 
pyplot.plot(x, y) 
pyplot.show()
```
设置同一个图中回值两个表
```
subplot
x = [1,2,4,5,7] 
pyplot.subplot(2,1,1) 
pyplot.plot(x,[1,2,3,4,5],"--",color='c',linewidth=5,alpha=0.5) 
pyplot.title("haha") 
pyplot.subplot(2,1,2) 
pyplot.plot(x,[1,2,3,4,5],"--",color='c',linewidth=5,alpha=0.5) 
pyplot.title("haha") 
pyplot.show()
```
设置全局中文和负号
```
pyplot.rcParams['font.sans-serif']=['SimHei']
pyplot.rcParams['axes.unicode_minus']=False
from matplotlib import rcParams 
rcParams.update({'font.size': 10, 'font.family': 'SimHei'，“axes.unicode_minus”：False})
```
设置图例:legend  
```
pyplot.legend({"12号","13号"},loc="lower right",edgecolor="m",shadow=True,fancybox=False,facecolor="red",borderpad=5,labelspacing=2,handlelength=3,handleheight=5,handletextpad=3,borderaxespad=2,title="hhh")
```
语法
> loc:图例所有figure位置  
> >  ‘best'  
> >  ‘upper right'  
> >  ‘upper left'  
> >  ‘lower left'  
> >  ‘lower right'  
> >  ‘right'  
> >  ‘center left'  
> >  ‘center right'  
> >  ‘lower center'  
> >  ‘upper center'  
> >  ‘center'    
> 
> prop:字体参数  
> fontsize:字体大小  
> > 整型  
> > 浮点型  
> > {‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’, ‘x-large’, ‘xx-large’}  
> 
> numpoints：为线条图图例条目创建的标记点数  
> scatterpoints：为散点图图例条目创建的标记点数  
> scatteryoffsets：为散点图图例条目创建的标记的垂直偏移量  
> frameon：控制是否应在图例周围绘制框架  
> fancybox：控制是否应在构成图例背景的FancyBboxPatch周围启用圆边  
> shadow：控制是否在图例后面画一个阴影  
> framealpha：控制图例框架的 Alpha 透明度  
> edgecolor：边框颜色  
> facecolor：Frame facecolor. frameon不能设置为False  
> borderpad：图例边框的内边距  
> labelspacing：图例条目之间的垂直间距  
> handletextpad：图例句柄和文本之间的间距  
> handlelength：图例句柄的长度  
> handleheight：图例句柄的高度  
> borderaxespad：轴与图例边框之间的距离  
> title：图例的标题  

添加网格：grid
> axis : 取值为‘both’， ‘x’，‘y’。就是想绘制哪个方向的网格线  
> alpha:透明度  
> color:设置网格线的颜色。或者用c来代替color  
> linestyle : 也可以用ls来代替linestyle  
> linewidth : 设置网格线的宽度  

### 绘图的种类
折线图
> 以折线的上升或下降来表示统计数量的增减变化的统计图  
> 特点:能够显示数据的变化趋势，反映事物的变化情况。(变化)
  
散点图 scatter(x,y)
> 用两组数据构成多个坐标点，考察坐标点的分布,判断两变量之间是否存在某种关联或总结坐标点的分布模式。  
> 特点:判断变量之间是否存在数量关联趋势,展示离群点(分布规律)  
> 参数  
>> x，y：array_like，shape（n，）  
>> s：标量或array_like，shape（n，），可选  
>>> 大小以点数^ 2。默认是`rcParams ['lines.markersize'] ** 2`。  
>> 
>> c：颜色，顺序或颜色顺序，可选，默认：'b'  
>>> `c`可以是单个颜色格式的字符串，也可以是一系列颜色  
>>
>> marker：散点的样式，可选，默认值：'o'  
>> alpha：标量，可选，默认值：无  
>>> alpha混合值，介于0（透明）和1（不透明）之间  
>>
>> linewidths：标量或array_like，可选，默认值：无  
>>> 如果无，则默认为（lines.linewidth，）。  
>> linewidth 是对线条的宽度设置，绘图时候像素点大小是不变的  
>> s 是设置表示图形的尺寸  
>> 
>> edgecolors ：颜色或颜色顺序，可选，默认值：无  
>> 示例
```
sc=pyplot.scatter(x, y,s=50,marker="o",c=y,edgecolors=["red","m","g","b"],alpha=0.5) pyplot.colorbar(sc)
```

设置颜色条
```
sc=pyplot.scatter(x, y,s=30,marker="o",c=y) pyplot.colorbar(sc)
```
条形图 bar()  
> 排列在工作表的列或行中的数据可以绘制到条形图中。
> 特点:绘制连离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计)
> 参数
>> left：x轴的位置序列，一般采用range函数产生一个序列，但是有时候可以是字符串  
>> height：y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据  
>> alpha：透明度，值越小越透明  
>> width：为柱形图的宽度，一般这是为0.8即可  
>> color或facecolor：柱形图填充的颜色  
>> edgecolor：图形边缘颜色  
>> label：解释每个图像代表的含义  
>
> 示例
> ```
> pyplot.bar(date,a,color="m",edgecolor="b",label="xx") pyplot.legend(loc='upper left')
> ```

直方图 hist()
> 由一系列高度不等的纵向条纹或线段表示数据分布的情况。   
> 一般用横轴表示数据范围，纵轴表示分布情况。  
> 特点:绘制连续性的数据,展示一组或者多组数据的分布状况(统计)  
> 参数  
> > x : 这个参数是指定每个bin(箱子)分布的数据,对应x轴  
> > bins : 这个参数指定bin(箱子)的个数,也就是总共有几条条状图  
> > color : 这个指定条状图的颜色  
> > edgecolor: 直方图边框颜色  
> > alpha: 透明度  
> > histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’  
> 
> 示例  
> ```
> pyplot.hist(a,bins=len(a),histtype="barstacked",edgecolor="m") pyplot.show()
> ```

饼图 pie()
> 参数  
> > x：为一个存放各部分占比的向量  
> > explode：list, 每一部分离开中心点的距离 ,元素数目与x相同且一一对应  
> > labels：list, 设置各类的标签，元素一一对应  
> > colors：list, 设置为各部分染色列表，元素一一对应  
> > startangle：起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起  
> > shadow：显示阴影，默认为False，即不显示阴影  
> > labeldistance：labels标签位置，相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧  
> > radius：控制饼图半径，默认值为1  
> > autopct : None,字符串，函数,百分比标签，可选,pct其实就是percent的缩写  
> 
> 示例  
> ```
> labels=["Python","Java","C","JavaScript"]  
> sizes=[40,20,10,30]  
> colors='yellowgreen','gold','lightskyblue','lightcoral'  
> explode=[0.1,0,0,0]  
> pyplot.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%.1f%%',shadow=True,startangle=50,
>           labeldistance=1.1,radius=0.7) 
> pyplot.show()
> ```

## Numpy
最基础的数据分析库
###介绍
用于处理数值类型的数据  
NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库  
一个在Python中做科学计算的基础库，重在数值计算，也是大部分PYTHON科学计算库的基础库，多用于在大型、多维数组上执行数值运算  
NumPy 是一个运行速度非常快的数学库，主要用于数组计算  
一个强大的N维数组对象 ndarray  
广播功能函数  
整合 C/C++/Fortran 代码的工具  
线性代数、傅里叶变换、随机数生成等功能  
NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用  
### 使用
#### 数组
数组的创建  
> 创建数组的方式  
> ```
> arr1 = numpy.array([1,2,3,5,7,8,10])
> arr2 = numpy.array(range(0,20,3))  
> ```

> 查看数据类型
> > 数组.dtype  

> 创建指定类型的数组  
> ```
> arr3 = numpy.array([0,1,1,0],dtype=bool)  
> arr4 = numpy.array([0.55,1.9,1,0],dtype=float)  
> ```

> 查看数组类名
> > type()  
> 
> 创建全零数组
> > zeros（行，列的元组，类型）
> > ```
> > arr = np.zeros((3, 3),"int")
> > ```
> 
> 创建全1数组
> > ones(行列元组，类型)  
> > ```
> > arr = np.ones((4,5),"float")
> > ```
> 
> 随机生成数组
> > 随机生成零一下小数的多维数组
> > ```
> > arr = np.random.rand(3,5)
> > ```
> > 让每一次随机的数组相同seed（类似编号）
> > ```
> > np.random.seed(1) 
> > arr = np.random.rand(3,5) 
> > print(arr) 
> > np.random.seed(1) 
> > arr = np.random.rand(3,5) 
> > print(arr)
> > ```
> > 随机整数np.random.randint(范围,size=(行,列))
> > ```
> > arr = np.random.randint(10,size=(3,5))
> > ``` 


数组的属性
> dtype 数组类型  
> size 数组的长度，即数组中的元素个数  
> shape 数组的形状  
> > 查看shape  
> > ```
> > arr4.shape
> > ```
> > 修改reshape(行，列)返回新的数组，修改前后的数组元素个数要一致  
> > 转为一维数组  
> > ```
> > arr5.flatten()
> > ```
> 
> itemsize 每个元素占用的字节数  
> ```
> arr = np.array([[3, 6, 8], [4, 9, 7], [5, 9, 4]],dtype="int32") 
> print(arr.dtype) 
> print(arr.itemsize) #=>4
> ```
> ndim数组的维数  
> nbytes数组中所有数组占用的字节数 实际数组所占空间会稍大一些  

切片与索引
> 即访问数组的方式  
> 字段访问  
> 基本切片  
> > 获取某个范围 从第几个元素到第几个 ```arr[2:7]```  
> > 获取某个范围 每隔几个选一个 ```arr2 = arr[2:7:2]```  
> 
> 行列
> > 获取所有行的哪一列 ndarray[:,列数]  
> > 获取某一行的第几个元素[行,列]  
> 
> 高级索引
> > 缺省索引  
> > ```
> > a = np.arange(0, 100, 10) 
> > b = a[:5] 
> > c = a[a >= 50] 
> > print(b) # >>>[ 0 10 20 30 40] 
> > print(c) # >>>[50 60 70 80 90]
> > ```
> > 布尔索引
> > > 通过布尔运算（如：比较运算符）来获取符合指定条件的元素的数组  
> > 
> > 花式索引
> > > 花式索引是NumPy用来描述使用整型数组作为索引， 根据索引数组的值作为目标数组的某个轴的下标来取值。 使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素；如果目标是二维数组，那么就是对应下标的行  
> > 
> > where函数
> > > where() 函数是另外一个根据条件返回数组中的值下标的元组（下标数组，数组类型）。
> > > ```
> > > a = np.arange(0, 100, 10) 
> > > b = np.where(a < 50) 
> > > c = np.where(a >= 50) 
> > > print(a) 
> > > print(b)--》(array([0, 1, 2, 3, 4], dtype=int64),) 
> > > print(c)--》(array([5, 6, 7, 8, 9], dtype=int64),)
> > > ```

数组和数的计算
> 会自动与数组中的每一个元素进行计算  

数组与数组的计算
> + 让几个数组每行每列互加  
> - 让几个数组每行每列互减  
> *让几个数组每行每列互乘  
> / 让几个数组每行每列互除  
> % 让几个数组每行每列互取余  
> 做判断  

numpy读取数据
> CSV:Comma-Separated Value,逗号分隔值文件 换行和逗号分隔行列的格式化文本,每一行的数据表示一条记录
> 由于csv便于展示,读取和写入,所以很多地方也是用csv的格式存储和传输中小型的数据


## Pada