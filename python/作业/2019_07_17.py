import random

#测试输出函数（方便注释）
def testPrint(str, mend = '\n'):
    # print(str, end = mend);
    pass

#减血函数
def reduceBlood(theRole,val):
    theRole[role[1]] -= val
    if theRole[role[1]] < 0:
        theRole[role[1]] = 0

#概率函数
def roll(probability):
    j = random.random()*100
    return probability > j

#英雄行动
def heroAction(theActor):
    tmp = dict(list(theActor)[0])
    print("你的回合，请选择你的行动：")
    print(f"1.攻击\t\t\t2.{tmp[role[4]]}")
    input1 = int(input())
    if input1 == 1:
        gongJi(theActor[0],theActor[1])
    elif input1 == 2:
        skills[tmp[role[4]]](theActor[0],theActor[1])
    pass
#怪物行动
def monsterAction(theActor):
    tmp = dict(list(theActor)[0])
    print(f"{tmp[role[0]]}的回合！")
    gongJi(theActor[0], theActor[1])
    pass

#检查双方血量
def check(theActor):
    re = False
    for tmp in theActor:
        re = re or tmp[role[1]] == 0
    return re
    pass

#回合开始函数
def roundStart(theActor):
    tmp = dict(list(theActor)[0])
    if tmp[role[3]] == 0:
        heIn = 0 if hero == tmp else 1
        print(f"{theActor[heIn][role[0]]}\t\t\t\t\t\t{theActor[1-heIn][role[0]]}")
        print(f"{theActor[heIn][role[1]]}---------VS---------{theActor[1-heIn][role[1]]}")
        tmp[role[8]](theActor)
    updataStatus(tmp)

#回合开始函数
def roundEnd(theActor):
    theActor.reverse()
    updataStatus(theActor[0])
    updataStatus(theActor[1])

#更新角色状态
def updataStatus(theRole):
    if theRole[role[3]] > 0:
        theRole[role[3]] -= 1
    if theRole[role[6]] > 0:
        theRole[role[6]] -= 1
    if theRole[role[7]] > 0:
        theRole[role[8]] -= 1

#战斗结束
def battleEnd(theRole):
    winner = theRole[0] if theRole[1] == 0 else theRole[1]
    tmp = theRole[1] if theRole[0] == winner else theRole[0]
    print(f"{winner[role[0]]}击败了{tmp[role[0]]}!")

#冲锋函数
def chongFeng(attacker, Attackee):
    hurtVal = attacker[role[2]]+10
    reduceBlood(Attackee, hurtVal)
    print(f"{attacker[role[0]]}对{Attackee[role[0]]}使用了冲锋！对{Attackee[role[0]]}造成了{hurtVal}点伤害！")
    pass
#爆发函数
def baoFa(attacker, Attackee):
    pass
#火球术函数
def huoQiuShu(attacker, Attackee):
    pass
#冰封术函数
def bingFengShu(attacker, Attackee):
    pass
#连刺函数
def LianCi(attacker, Attackee):
    pass
#隐蔽函数
def yinBi(attacker, Attackee):
    pass
#攻击函数
def gongJi(attacker, Attackee):
    reduceBlood(Attackee, attacker[role[2]])
    print(f"{attacker[role[0]]}攻击了{Attackee[role[0]]}，对{Attackee[role[0]]}造成了{attacker[role[2]]}点伤害")
    pass

#基础角色数据结构：
#0.name       名字
#1.hp         生命值
#2.atk        攻击力
#3.state      当前状态      当前状态：值为非负数，0表示可以行动,非零数表示无法行动，数字表示还有几回合可以行动
#4.skill1     技能1
#5.skill2     技能2
#6.sk1st      技能1状态
#7.sk2st      技能2状态     技能状态：值为非负数，0表示可以释放, 非零数为当前回合该技能的冷却时间
#8.funact     行动函数
role = ("name", "hp", "atk", "state", "skill1", "skill2", "sk1st", "sk2st", "funact")

hero = {role[0]:"无名氏", role[3]:0, role[8]:heroAction, role[6]:0, role[7]:0}

occupations = [{"occ":"战士", "atk":8, "hp":200, "skill1":"冲锋", "skill2":"爆发"},
               {"occ":"法师", "atk":3, "hp":100, "skill1":"火球术", "skill2":"冰封术"},
               {"occ":"盗贼", "atk":13, "hp":80,  "skill1":"连刺", "skill2":"隐蔽"}]
skills = {"冲锋":chongFeng, "爆发":baoFa, "火球术":huoQiuShu, "冰封术":bingFengShu, "连刺":LianCi, "隐蔽":yinBi, "冲锋":chongFeng, "攻击":gongJi}
monsters = [{role[0]:"皮卡耗子", role[1]:100, role[2]:3, role[3]:0, role[4]:"攻击", role[5]:"攻击", role[6]:0, role[7]:0, role[8]:monsterAction}]

# 选择职业
# 设置姓名
# 开始遭遇战

print("职业列表：")
for i in range(len(occupations)):
    print(f"{i}.", end = "\t")
    print(occupations[i]["occ"], end = "\t")
    print(f"hp：{occupations[i][role[1]]}",  end = "\t")
    print(f"攻击力：%03d", end="\t\t")
    print(f"技能：{occupations[i][role[4]]}",  end="\n")
if int(input("请选择职业(输入序号)：")) != 0:
    print("抱歉，当前只能够选择战士")
hero.update(occupations[0])
testPrint(hero)
hero["name"] = input("请决定您的英雄名：")
testPrint(hero)

print("您的英雄信息如下：")
print(f"名字：{hero[role[0]]}\t职业：{hero['occ']}\t生命值：{hero[role[1]]}\t攻击力：{hero[role[2]]}\t技能：{hero[role[4]]}")

#战斗流程：
#   回合开始
#       检查行动方状态，调用对应函数
#   回合行动
#       分为怪兽回合与英雄回合，调用对应的回合行动函数
#   回合结束
#       显示双方状态，修改状态
theMoster = monsters[random.randint(len(monsters))];
actors = [hero.copy(), theMoster.copy()]
testPrint(actors[0])
testPrint(actors[1])
print(f"你遭遇到了{actors[1]['name']}，开始战斗！")
while True:
    roundStart(actors)
    roundEnd(actors)
    if check(actors):
        break;
battleEnd(actors)
