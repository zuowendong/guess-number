""" 用pyhon设计第一个游戏 """

temp = input("猜一猜我心里在想的哪个数字：")
guess = int(temp)

if guess == 8:
    print("牛啊牛啊，你猜对了！")
else:
    print("猜错了，我想的数字是8！")

print("游戏结束~")
