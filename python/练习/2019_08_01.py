from matplotlib import pyplot, rcParams
import random
import numpy as np

rcParams.update({'font.size': 10, 'font.family': 'SimHei', "axes.unicode_minus": False})

# labels=["Python","Java","C","JavaScript"]
# sizes=[40,20,10,30]
# colors='yellowgreen','gold','lightskyblue','lightcoral'
# explode=[0.11,0,0,0]
# pyplot.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%.1f%%',shadow=True,startangle=50,labeldistance=1.1,radius=0.7)
# pyplot.show()

# x = []
#
# for i in range(20):
#     x.append(random.randint(20, 70))
# pyplot.hist(x,bins=5)
# pyplot.show()

# a=[131,  98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115,  99, 136, 126, 134,  95, 138, 117, 111,78, 132, 124, 113, 150, 110, 117,  86,  95, 144, 105, 126, 130,126, 130, 126, 116, 123, 106, 112, 138, 123,  86, 101,  99, 136,123, 117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127,105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120, 114,105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134,156, 106, 117, 127, 144, 139, 139, 119, 140,  83, 110, 102,123,107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133,112, 114, 122, 109, 106, 123, 116, 131, 127, 115, 118, 112, 135,115, 146, 137, 116, 103, 144,  83, 123, 111, 110, 111, 100, 154,136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141,120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125, 126,114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137,  92,121, 112, 146,  97, 137, 105,  98, 117, 112,  81,  97, 139, 113,134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110,105, 129, 137, 112, 120, 113, 133, 112,  83,  94, 146, 133, 101,131, 116, 111,  84, 137, 115, 122, 106, 144, 109, 123, 116, 111,111, 133, 150]
#
# pyplot.hist(a, bins=30)
# pyplot.show()

# arr = numpy.array([1, 4, 5])
# print(type(arr))

# arr = numpy.zeros((2, 5))
# print(arr)
#
# arr2 = numpy.zeros((2,3,4))
# print(arr2.shape)
#
# arr3 = numpy.random.randint(0, 30, (11,), dtype="int32")
# print(arr3)
# print(arr3[2::2])

# arr = numpy.array(a)
# re = arr[arr >= 120]
# pyplot.hist(re, 10)
# pyplot.show()

arr = np.array([[3, 6, 8], [4, 9, 7], [5, 9, 4]])
print(arr[1, 0:3])