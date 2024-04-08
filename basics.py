# 变量
x = 3
print(x)

# 赋值
x = y = 10
print(x, y)

# 互换变量值
a = 1
b = 2
a, b = b, a
print(a, b)

# 字符串
print("Let's go")

# 转义字符
print('\"Life is short, Let\'s learn python\"')

print("D:\\three\\two\\one\\now")

print(r"D:\six\five\four\three\two\one\now")

print("床前明月光\n\
疑是地上霜")

poetry = '''
积雨空林烟火迟，蒸藜炊黍饷东菑。
漠漠水田飞白鹭，阴阴夏木啭黄鹂。
山中习静观朝槿，松下清斋折露葵。
野老与人争席罢，海鸥何事更相疑。
'''
print(poetry)

print("今天星期一！\n" * 10)

# 攻击随机数
import random
# 获取随机数种子
x = random.getstate()
# 循环打印5次随机数
counts = 5
while counts > 0:
  print(random.randint(1, 10))
  counts = counts -1
# 重新设置随机数生成器内部状态
random.setstate(x)
# 再次执行，重现之前的随机数
counts = 5
while counts > 0:
  print(random.randint(1, 10))
  counts = counts -1

# 数字类型
x = 6 / 2
print(x)

# 浮点数精度问题
x = 0.1 + 0.2
print(x)

i = 0
while i < 1:
  i = i + 0.1
  print(i)

print(0.3 == 0.1 + 0.2)

# 十进制
import decimal
a  = decimal.Decimal("0.1")
b  = decimal.Decimal("0.2")
c  = decimal.Decimal("0.3")
print(c == a + b)

# 复数（实部 + 虚部）
x = 1 + 2j
print(x.real)
print(x.imag)

# 计算

# 地板除 - 除法向下取整 （取比目标结果小的最大整数）
print(3 // 2)
print(-3 // 2)

# 同时获取地板除 & 余数
print(divmod(-3, 2))

# 布尔值类型
print(bool(100))
print(bool(''))
print(bool(0))

# 逻辑运算符

# 全真才为真，有假即为假
x = 3 < 4 and 4 < 5
print(x)

x = 3 > 4 and 4 < 5
print(x)

x = 3 > 4 and 4 > 5
# False
print(x)

# 全假才为假，有真即为真
x = 3 < 4 or 4 < 5
print(x)
x = 3 > 4 or 4 < 5
print(x)
x = 3 > 4 or 4 > 5
print(x)

# 取反
x = not True
print(x)
x = not False
print(x)
x = not 250
print(x)
x = not 0
print(x)

# 短路逻辑
"""从左往右，只有当第一个操作数的值无法确定逻辑运算的结果时，才对第二个操作数进行求值"""
x = (not 1) or (0 and 1) or (3 and 4) or (5 and 6) or(7 and 8 and 9)
print(x)

# and运算，需要判断左右两侧都为true，才会返值
# 3 为 True, and运算需要再比较右侧的值，右侧4为True, 就将4返回
print(3 and 4)
# 0 为 False, and运算有一个False就结束比较
print(0 and 3)

# or运算，判断左右两侧有一个true，即为True,就返值
# 3 为 True, or运算需要一个true，就将3返回
print(3 or 4)
# 0 为 False, or运算需要都为False才返回， 比较第二个值 4
print(0 or 4)


x = False or 0 or 4 or 6 or 9
print(x)

x = not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
print(x)