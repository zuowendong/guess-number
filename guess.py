""" 用pyhon设计第一个游戏 """

counts = 3

while counts > 0:
    temp = input("猜一猜我心里在想的哪个数字：")
    guess = int(temp)

    if guess == 8:
        print("牛啊牛啊，你猜对了！")
        break
    else:
        print("猜错了！")
        if guess < 8:
            print("小啦")
        else:
            print("大啦")
    counts = counts - 1

print("游戏结束~")
