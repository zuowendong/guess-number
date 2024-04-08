# 说明文档
""" 用python设计第一个游戏 """

import random

counts = 3
answer = random.randint(1, 10)
while counts > 0:
    temp = input("please guess number: ")
    # 转数字
    guess = int(temp)
    if guess == answer:
        print("nice! you are right")
        break
    else:
        print("wrong！")
        if guess < 8:
            print("small")
        else:
            print("larger")
    counts = counts - 1
print("game over~")
