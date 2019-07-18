import random

#测试输出函数（方便注释）
def testPrint(str, mend = '\n'):
    # print(str, end = mend);
    pass

#减血函数
def reduceBlood(theRole,val):
    if missRoll(theRole):
        val = 0;
        print(f"{theRole[role[0]]}闪避了攻击！没有受到伤害！")
    else:
        print(f"对{theRole[role[0]]}造成了{val}点伤害!")
    theRole[role[1]] -= val
    if theRole[role[1]] < 0:
        theRole[role[1]] = 0

#概率函数
def roll(probability):
    j = random.random()*100
    return probability > j

#miss函数
def missRoll(theRole):
    re = False
    gaiLv = 0 if theRole[role[3]][5] == 0 else theRole[role[3]][7]
    gaiLv += theRole[role[10]]
    if roll(gaiLv):
        re = True
    return re

#英雄行动
def heroAction(theActor):
    sk1 = True
    tmp = dict(list(theActor)[0])
    print("你的回合，请选择你的行动：")
    print(f"1.攻击\t\t\t", end = "")
    if tmp[role[6]] > 0:
        print(f"  {tmp[role[4]]}（{tmp[role[6]]}回合后可使用）", end = "")
        sk1 = False
    else :
        print(f"2.{tmp[role[4]]}", end = "")
    print()
    while True:
        input1 = int(input())
        if input1 == 1:
            gongJi(theActor[0],theActor[1])
            break
        elif sk1 and input1 == 2:
            skills[tmp[role[4]]](theActor[0],theActor[1])
            break
        print("请输入正确的选项！")
    pass

#怪物行动
def monsterAction(theActor):
    tmp = dict(list(theActor)[0])
    print(f"{tmp[role[0]]}的回合！")
    if tmp[role[6]] == 0:
        if roll(90):
            skills[tmp[role[4]]](theActor[0], theActor[1])
        else:
            gongJi(theActor[0], theActor[1])
    else:
        gongJi(theActor[0], theActor[1])
    pass

#检查双方血量
def check(theActor):
    re = False
    for tmp in theActor:
        re = re or tmp[role[1]] == 0
    return re
    pass

#检查角色状态
def checkState(theActor):
    state = theActor[role[3]]
    re = True
    if state[0] > 0:
        re = False
        print(f"{theActor[role[0]]}处于{state[1]}（{state[0]}回合）状态，无法行动！")
    if state[2] > 0:
        print(f"{theActor[role[0]]}受到{state[4]}点{state[3]}（{state[2]}回合）伤害！")
    if state[5] > 0:
        print(f"{theActor[role[0]]}处于{state[6]}（{state[5]}回合）状态，闪避增加了{state[7]}！")
    return re
    pass

#回合开始函数
def roundStart(theActor):
    tmp = dict(list(theActor)[0])
    heIn = 0 if hero[role[0]] == tmp[role[0]] else 1
    print(f"{theActor[heIn][role[0]]}\t\t\t\t\t\t{theActor[1-heIn][role[0]]}")
    print(f"{theActor[heIn][role[1]]}-----------VS-----------{theActor[1-heIn][role[1]]}")
    if checkState(tmp):
        tmp[role[8]](theActor)

#回合结束函数
def roundEnd(theActor):
    updataStatus(theActor[0])
    # updataStatus(theActor[1])
    theActor.reverse()

#更新角色状态
def updataStatus(theRole):
    if theRole[role[3]][0] > 0:
        theRole[role[3]][0] -= 1
    if theRole[role[3]][2] > 0:
        theRole[role[3]][2] -= 1
    if theRole[role[3]][5] > 0:
        theRole[role[3]][5] -= 1
    if theRole[role[6]] > 0:
        theRole[role[6]] -= 1
    if theRole[role[7]] > 0:
        theRole[role[8]] -= 1

#捡装备
def diaoLuoZhuangBei(theHero,theMoster):
    if not roll(theMoster["diaoLuoLv"]):
        return
    print(f"{theMoster[role[0]]}掉落了装备{theMoster['diaoLuo']}!")
    if len(theHero["zhuangBei"]) > 0:
        print("你当前装备了", end="")
        for tmp in theHero["zhuangBei"]:
            print(tmp[0],end=",")
        print("!")
    else:
        print("你当前没有装备！")
    input1 = int(input("是否拾取装备？（0.是，1.否）"))
    if input1 == 0:
        theHero["zhuangBei"].append(theMoster['diaoLuo'])

#涨经验
def zhangJinYan(theRole):
    theRole["exp"] += 5;
    if theRole["exp"] == theRole[role[11]]*5+5:
        levelUp()

#战斗结束
def battleEnd(theRole):
    winner = theRole[0] if theRole[1] == 0 else theRole[1]
    tmp = theRole[1] if theRole[0] == winner else theRole[0]
    print(f"{winner[role[0]]}击败了{tmp[role[0]]}!")
    return winner

#技能冷却函数
def skillCooling(theRole,skillName):
    if theRole[role[4]] == skillName:
        theRole[role[6]] = coolingTime[skillName]
    else :
        theRole[role[7]] = coolingTime[skillName]

#设置人物状态
def setState(theRole, state, stateName, hold, val = 0):
    theRole[role[3]][state] = hold
    theRole[role[3]][state+1] = stateName
    if state != 0:
        theRole[role[3]][state+2] =val

#冲锋函数
def chongFeng(attacker, Attackee):
    hurtVal = attacker[role[2]]+10
    reduceBlood(Attackee, hurtVal)
    print(f"{attacker[role[0]]}对{Attackee[role[0]]}使用了冲锋！", end = "")
    reduceBlood(Attackee,hurtVal)
    if roll(30):
        setState(Attackee, 0, "倒地", 1)
        print(f"{attacker[role[0]]}释放的冲锋击倒了{Attackee[role[0]]}！持续{Attackee[role[3]][0]}回合！")
    skillCooling(attacker,"冲锋")
    pass
#爆发函数
def baoFa(attacker, Attackee):
    pass
#火球术函数
def huoQiuShu(attacker, Attackee):
    hurtVal = 15
    reduceBlood(Attackee, hurtVal)
    print(f"{attacker[role[0]]}对{Attackee[role[0]]}使用了火球术！", end = "")
    reduceBlood(Attackee,hurtVal)
    if roll(70):
        setState(theRole=Attackee, state=2, stateName="燃烧", val=5, hold=3)
        print(f"{attacker[role[0]]}释放的火球术点燃了{Attackee[role[0]]}！持续{Attackee[role[3]][2]}回合！")
    skillCooling(attacker, "火球术")
    pass
#冰封术函数
def bingFengShu(attacker, Attackee):
    pass
#背刺函数
def beiCi(attacker, Attackee):
    pass
#隐蔽函数
def yinBi(attacker, Attackee):
    setState(attacker, 5, "隐蔽", 2, 20)
    print(f"{attacker[role[0]]}使用技能隐蔽!使自己的闪避增加了20!持续{attacker[role[3]][5]}回合!")
    skillCooling(attacker,"隐蔽")
    pass
#攻击函数
def gongJi(attacker, Attackee):
    hurtVal = getAtk(attacker)
    print(f"{attacker[role[0]]}攻击了{Attackee[role[0]]}！",end = "")
    if roll(attacker[role[9]]):
        hurtVal *= 2
        print(f"{attacker[role[0]]}打出了暴击!效果拔群！",end = "")
    reduceBlood(Attackee, hurtVal)
    pass

#升级函数
def levelUp():
    hero[role[11]] +=1
    hero["exp"] = 0
    print(f"{hero[role[0]]}升级了！攻击+2！闪避+1！当前等级：{hero[role[11]]}！")

#获取角色的攻击力
def getAtk(theRole):
    re = theRole[role[2]]
    for i in theRole["zhuangBei"]:
        re += i[1]
    re += 2*theRole[role[11]]
    return re

def getAvoidance(theRole):
    re = theRole[role[10]]
    for i in theRole["zhuangBei"]:
        re += i[2]
    re += 2 * theRole[role[11]]
    return re

#基础角色数据结构：
# 0.name       名字
# 1.hp         生命值
# 2.atk        攻击力
# 3.state      当前状态      当前状态：值为列表，*[0]为行动状态，0表示可以行动,数字表示还有几回合可以行动
#                                            [1]为行动状态名称，只有在[0]不为0时有效
#                                           *[2]为扣血状态，0表示无状态，非0表示状态还有几回合消失
#                                            [3]为扣血状态名称，只有在[2]不为0时有效
#                                            [4]为扣血血量，只有在[2]不为0时有效
#                                           *[5]为闪避增益状态，0表示无状态，非0表示状态还有几回合消失
#                                            [6]为扣血状态名称，只有在[2]不为0时有效
#                                            [7]为闪避增益数量，只有在[5]不为0时有效
# 4.skill1     技能1
# 5.skill2     技能2
# 6.sk1st      技能1状态
# 7.sk2st      技能2状态     技能状态：值为非负数，0表示可以释放, 非零数为当前回合该技能的冷却时间
# 8.funact     行动函数
# 9.crit       暴击率
#10.avoidance  闪避率
#11.level      等级          每升一级，攻击力增加2，闪避增加1，满级为10级，满级后即通关
#12.exp        经验          人物经验，仅对英雄有效升级经验公式：当前等级*5+5，每杀死一只怪物增加5经验
role = ("name", "hp", "atk", "state", "skill1", "skill2", "sk1st", "sk2st", "funact", "crit",  "avoidance", "level")

hero = {role[0]:"无名氏", role[3]:[0, "", 0, "", 0, 0, "", 0], role[8]:heroAction, role[6]:0, role[7]:0, "zhuangBei":[], role[11]:0, "exp":0}

occupations = [{"occ":"战士", "atk":8, role[1]:200, "skill1":"冲锋", "skill2":"爆发", "crit":30, role[10]:10},
               {"occ":"法师", "atk":5, role[1]:100, "skill1":"火球术", "skill2":"冰封术", "crit":15, role[10]:20},
               {"occ":"盗贼", "atk":13, role[1]:80,  "skill1":"隐蔽", "skill2":"背刺", "crit":20, role[10]:35}]

skills = {"冲锋":chongFeng, "爆发":baoFa, "火球术":huoQiuShu, "冰封术":bingFengShu, "背刺":beiCi, "隐蔽":yinBi, "攻击":gongJi}

weapons = [("皮卡耗子之脚",10,-3),("蒜头王八之头",5,15)]

coolingTime = {"冲锋":2, "爆发":5, "火球术":5, "冰封术":3, "背刺":3, "隐蔽":3, "攻击":0}

monsters = [{role[0]:"皮卡耗子", role[1]:100, role[2]:8, role[3]:[0, "", 0, "", 0, 0, "", 0], role[4]:"攻击", role[5]:"攻击", role[6]:0, role[7]:0, role[8]:monsterAction, role[9]:15, role[10]:10,"diaoLuo":weapons[0], "diaoLuoLv":50, "zhuangBei":[], role[11]:0},
            {role[0]:"蒜头王八", role[1]:200, role[2]:3, role[3]:[0, "", 0, "", 0, 0, "", 0], role[4]:"隐蔽", role[5]:"攻击", role[6]:0, role[7]:0, role[8]:monsterAction, role[9]:10, role[10]:8, "diaoLuo":weapons[0], "diaoLuoLv":50, "zhuangBei":[], role[11]:0}]


# 选择职业
# 设置姓名
# 开始遭遇战

print("职业列表：")
for i in range(len(occupations)):
    print(f"{i}.", end = "\t")
    print(occupations[i]["occ"], end = "\t")
    print(f"hp：%03d"%occupations[i][role[1]],  end = "\t")
    print(f"攻击力：%03d"%occupations[i][role[2]], end="\t\t")
    print(f"技能：{occupations[i][role[4]]}",  end="\n")
# while True:
#     input2 = int(input("请选择职业(输入序号)："))
#     if input2 == 2:
#         print("抱歉，当前无法选择盗贼！")
#         continue
#     break
input2 = int(input("请选择职业(输入序号)："))
hero.update(occupations[input2])
testPrint(hero)
hero[role[0]] = input("请决定您的英雄名：")
testPrint(hero)

#战斗流程：
#   回合开始
#       检查行动方状态，调用对应函数
#   回合行动
#       分为怪物回合与英雄回合，调用对应的回合行动函数
#   回合结束
#       显示双方状态，修改状态
while True:
    print("您的英雄信息如下：")
    print(
        f"名字：{hero[role[0]]}\t职业：{hero['occ']}\t生命值：{hero[role[1]]}\t攻击力：%03d\t技能：{hero[role[4]]}\t等级：{hero[role[11]]}\t经验：{hero['exp']}/%d" %(
        hero[role[2]],hero[role[11]]*5+5))
    theMoster = monsters[random.randint(0,len(monsters)-1)]
    actors = [hero.copy(), theMoster.copy()]
    testPrint(actors[0])
    testPrint(actors[1])
    print(f"你遭遇到了{actors[1][role[0]]}，开始战斗！")
    while not check(actors):
        roundStart(actors)
        roundEnd(actors)
    if battleEnd(actors)[role[0]] != hero[role[0]]:
        break
    zhangJinYan(hero)
    diaoLuoZhuangBei(hero,theMoster)
    input("输入回车继续！")
