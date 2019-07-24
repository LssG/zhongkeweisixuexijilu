
class Lyrics:

    headStr = ["ti", "ar", "al", "by"]

    @classmethod
    def parseLyrics(cls,str):
        str = str.replace("[",'')

        re = {}

        l1 = str.split("\n")
        for i in range(len(cls.headStr)):
            l1[i] = l1[i].split("]")
            for j in cls.headStr:
                if l1[i][0].startswith(j):
                    re[j] = l1[i][0].split(":")[1]

        l1[0:len(re)] = []
        for i in l1:
            re[i.split("]")[0]] = i.split("]")[1]
        return re