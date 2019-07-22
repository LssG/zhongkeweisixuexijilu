guiZe = 22

def makeRole(x):
    re = []
    for i in range(8):
        re.insert(0,x&1)
        x = x >> 1
    return re
def printGame(game,end = "\n"):
    re = ""
    for i in game:
        if i == 1:
            re += "@"
        else:
            re += " "
    print(f"[{re}]",end = end)

def zhuanShuZi(arr):
    re = 0
    for i in arr:
        re = re << 1 | i
    return re

def iteration(game, theRole, mode = True):
    re = []
    length = len(game)
    for i in range(len(game)):
        # index = game[(i-1)%length] << 2
        # print(f"test:{index}")
        # index += game[i%length] << 1
        # print(f"test:{index}")
        # index += game[(i+1)%length]
        # print(f"test:{index}")
        index = game[(i-1)%length] << 2 | game[i%length] << 1 | game[(i+1)%length]
        re.append(theRole[index])
    return re

guiZe = makeRole(guiZe)
# print (guiZe)

gameP = []
size = int(input("size:"))
role = int(input("role:"))
times = int(input("times:"))
# size = 111
# role = 0
role = makeRole(role)
# print (role)
for i in range(size):
    gameP.append(0)
gameP[size//2] = 1
# print(gameP)
# printGame(gameP)
# i = 210
for i in range(1):
    gamePlane = gameP.copy()
    print("--------------------------------------------------")
    # role = makeRole(i)
    print(f"role:{i},{role}")
    printGame(gamePlane)
    for j in range(times):
        gamePlane = iteration(gamePlane, role)
        printGame(gamePlane,end="\n")
        # print (zhuanShuZi(gamePlane))


