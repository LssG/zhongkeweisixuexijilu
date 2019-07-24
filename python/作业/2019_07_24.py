import Lyrics
import threading

str = """[ti:知足]
[ar:五月天(07 最知足版)]
[al:离开地球表面 Jump！]
[by:海阔天空]
[00:26.59]怎么去拥有 一道彩虹
[00:32.81]怎么去拥抱 一夏天的风
[00:39.11]天上的星星笑地上的人
[00:45.28]总是不能懂不能觉得足够
[00:51.78]
[00:54.85]如果我爱上 你的笑容
[01:01.00]要怎么收藏 要怎么拥有
[01:07.25]如果你快乐 不是为我
[01:13.49]会不会放手其实才是拥有
[01:18.90]当一阵风吹来风筝飞上天空
[01:25.54]为了你而祈祷 而祝福而感动
[01:31.55]终于你身影消失在 人海尽头
[01:38.32]才发现 笑着哭 最痛
[01:44.84]
[01:48.33]那天你和我 那个山丘
[01:54.45]那样的唱着 那一年的歌
[02:00.54]那样的回忆 那么足够
[02:07.17]足够我天天都品尝着寂寞
[02:13.67]
[02:37.56]当一阵风吹来风筝飞上天空
[02:44.09]为了你而祈祷 而祝福而感动
[02:50.06]终于你身影消失在 人海尽头
[02:57.13]才发现 笑着哭 最痛
[03:02.55]当一阵风吹来风筝飞上天空
[03:09.10]为了你而祈祷 而祝福而感动
[03:15.24]终于你身影消失在 人海尽头
[03:22.18]才发现 笑着哭 最痛
[03:32.12]如果我爱上 你的笑容
[03:38.46]要怎么收藏 要怎么拥有
[03:44.97]如果你快乐再不是为我
[03:51.13]会不会放手其实才是拥有
[03:57.31]知足的快乐叫我忍受心痛
[04:03.79]知足的快乐叫我忍受心痛
[04:16.64]~~End~~"""

def praseTime(str):
    str = str.split(":")
    re = int(str[0]) * 60 + float(str[1])
    return re

# print (dir(Lyrics.Lyrics))

lyricsData = Lyrics.Lyrics.parseLyrics(str)

info = {}
lyricses = []

for i in lyricsData:
    if i[0:2].isnumeric():
        lyricses.append({
            "time":i,
            "str":lyricsData[i]
        })
    else:
        info[i] = lyricsData[i]

# timeSecBefore = praseTime(lyricses[0]["time"])
# print(timeSecBefore)

# printList = []
# for i in info:
#     for j in Lyrics.Lyrics.headStr:
#         if i == j:

print (f"正在播放：{info['ti']}")
print (f"歌手：{info['ar']}")
print (f"专辑：{info['al']}")
print (f"原曲：{info['by']}")
print ("--------------------------")

index = 0
secNow = 0

def __show():
    global index
    global secNow
    tmp = lyricses[index]
    print(f"{tmp['time']}\t\t{tmp['str']}")
    if index < len(lyricses)-1:
        threading.Timer(praseTime(lyricses[index+1]["time"])-praseTime(tmp["time"]),__show).start()
    index += 1

def show():
    global index
    global secNow
    tmp = lyricses[index]
    threading.Timer(praseTime(tmp["time"]),__show).start()

show()


