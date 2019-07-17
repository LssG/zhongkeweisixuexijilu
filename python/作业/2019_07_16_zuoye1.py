#英雄的属性有hp（血量），mp（蓝量），weapon（武器栏）
#武器的属性有dmg（攻击力），attribute（属性）

heros = [{"name":"南宫康健"},{"name":"段文柏"},{"name":"蔺锦薇"}]
hps = {"南宫康健":100,"段文柏":80,"蔺锦薇":150}
mps = {"南宫康健":100,"段文柏":150,"蔺锦薇":50}
weapons = {"南宫康健":"无","段文柏":"无","蔺锦薇":"无"}
weaponNames = ["玄冥抓","苍空地缚伞","自在霸王钟"]
dmgs = {"玄冥抓":10,"苍空地缚伞":3,"自在霸王钟":2}
attributes = {"玄冥抓":"攻速+2","苍空地缚伞":"法强+6","自在霸王钟":"防御+10"}
for i in range(len(heroNames)):
    print("%d\t%s"%(i,heroNames[i]))
heroNo = int(input("请输入编号选择人物："))
i = 0
for i in range(len(weapons)):
    print("%d\t%s"%(i,weaponNames[i]))
weaponNo = int(input("请输入编号选择武器："))
print("你的人物信息如下：")
print("人物名称:\t%s"%heroNames[heroNo])
print("生命值:\t%d"% hps[heroNames[heroNo]])
print("魔法值:\t%d"% mps[heroNames[heroNo]])
print("装备:\t%s"% weaponNames[weaponNo])
print("\t\t攻击力:%d"% dmgs[weaponNames[weaponNo]])
print("\t\t属性:%s"% attributes[weaponNames[weaponNo]])


