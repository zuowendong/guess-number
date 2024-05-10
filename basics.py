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

# 条件判断
if 3 > 5:
  print('我在里面')
  print('我也在里面')
elif 5 < 6:
  print('yep')
else :
  print('我在外面')

# 条件表达式
age = 16
print('抱歉，未满18岁禁止访问') if age < 18 else print('欢迎访问')

a = 3
b = 4
small = a if a < b else b
print(small)

score = 66
level = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 80 else
         'B' if 80 <= score < 90 else
         'A' if 90 <= score < 100 else
         'S' if score == 100 else
         print('请输入分数'))
print(level)

# 循环
i = 1
sum = 0
while i <= 1000000:
  sum += i
  i += 1
  if i == 10:
    break
  if i % 2 == 0:
    continue
  print(i)
print(sum)

day = 1
hour = 1
while day <= 7:
  while hour <= 8:
    print('第' + str(day) + '天：' + '今天我一定学习8小时')
    hour += 1
    if hour > 2:
      break
  day += 1
  hour = 1

# for 循环
for each in 'I learned python':
  print(each)

for i in range(1, 10):
  print(i)

# 输出10以内所有素数
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, '=', x, '*', n // x)
      break
  else:
    print(n, '是一个素数')

# 列表
rhyme = [1, 2, 3, 4, 5, '上山打老虎']
print(rhyme)
for each in rhyme:
  print(each)
print(rhyme[1])
print(rhyme[-1])

# 列表切片
print(rhyme[:])
print(rhyme[:3])
print(rhyme[3:])
print(rhyme[0:6:2])
print(rhyme[::2])
print(rhyme[::-2])
print(rhyme[::-1])

nums = [1,2,3,'x']
# 单个尾部插入
nums.append(4)
# 连续尾部插入
nums.extend([5,6,7])
print(nums)

# 切片尾部插入
nums[len(nums):] = [8,9,10]
# 指定位置插入
nums.insert(0,0)
# 指定元素移除
nums.remove(10)
# 指定位置移除
nums.pop(4)
# 全部清空
nums.clear()

print(nums)

# 排序
nums = [3,45,63,56,3,1,34,5,56,4]
nums.sort()
nums.reverse()
nums.sort(reverse=True)
print(nums)

# 查找
nums = [3,45,63,56,3,1,34,5,56,4]
print(nums.count(56))

print(nums.index(56))

# 浅拷贝
nums_copy = nums.copy()
print(nums_copy)

# 列表的加法乘法
s = [1,2,3]
t = [4,5,6]
print(s+t)
print(s*3)

# 嵌套列表
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)

for i in matrix:
  for each in i:
    print(each, end=' ')
  print()

x = [1,2,4]
y = [1,2,4]
print(x is y)

# 创建多维列表
A = [1] * 3
print(A)
for i in range(3):
  A[i] = [2] * 2
print(A)

# 浅拷贝，处理一层列表的引用
x = [1,2,3]
y = x.copy()
x[1] = 'x'
print(x)
print(y)
# 切片浅拷贝
x = [1,2,3]
y = x[:]
x[1] = 'x'
print(x)
print(y)
# copy模块浅拷贝
import copy
x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.copy(x)
x[1][1] = 'x'
print(x)
print(y)

# 多维列表浅拷贝无效
x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()
x[1][1] = 'x'
print(x)
print(y)

# 深拷贝
import copy
x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.deepcopy(x)
x[1][1] = 'x'
print(x)
print(y)

# 将列表中数字乘以2倍
A = [1,2,3,4,5,6]
for i in range(len(A)):
  A[i] = A[i] * 2
print(A)

# 列表推导式
# 语法 [expression for target in iterable]
A = [1,2,3,4,5,6]
A = [i * 2 for i in A]
print(A)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
col2 = [row[1] for row in matrix]
print(col2)
diag = [matrix[i][i] for i in range(len(matrix))]  # i = 0,1,2
# matrix[0][0] matrix[1][1] matrix[2][2]
print(diag)

# 列表推导式创建多维列表
S = [[0]*3 for i in range(3)]
print(S)

# 筛选
even = [i for i in range(10) if i % 2 == 0]
print(even)
odd = [i+1 for i in range(10) if i % 2 == 0]
print(odd)

words = ['Great', 'Find', 'Fantastic', 'Excellent', 'Nice']
f_words = [i for i in words if i[0] == 'F']
print(f_words)

# 二维列表降为一维列表
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flatten = [col for row in matrix for col in row]
print(flatten)

A = [[x,y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(A)

# 元组
# 元组不可变
rhyme = (1,2,3,3,3,3,4,5,'上山打老虎')
print(rhyme)
print(rhyme[-1])
print(rhyme.count(3))
print(rhyme.index(3))
print(rhyme[::-1])

s = (1,2,3,4,5)
a = [each*2 for each in s]
print(a)

print((520,))

# 打包 / 解包
t = ('你好', '再见', '咕的白')
x, y, z = t # 左侧数量和右侧内数量一致
print(x)
print(y)
print(z)

t = ('你好', '再见', '咕的白', '唯美的', '他')
x, y, *z = t
print(x)
print(y)
print(z)

# 字符串方法
x = '12321'
res = '是回文数' if x == x[::-1] else '不是回文数'
print(res)
x = '12345'
res = '是回文数' if x == x[::-1] else '不是回文数'
print(res)

# 字符串大小写转换方法
x = "how are you? I'm fine"
print(x)
# 首字母大写
print(x.capitalize())
# 首字母小写
print(x.casefold())
# 每个单词首字母大写
print(x.title())
# 所有字符大小写反转
print(x.swapcase())
# 所有字符大写
print(x.upper())
# 所有字符小写
print(x.lower())

# 字符串对齐
x = '你好吗？我很好哦'
print(x.center(5))
print(x.center(20, '-'))
print(x.ljust(20))
print(x.rjust(20))

print('520'.zfill(5))
print('-250'.zfill(5))

# 字符串查找方法
x = "上海自来水来自海上"
print(x.count('海',0,5))
print(x.find('海'))
print(x.rfind('海'))

code = """
  print("I love you")
  print("I love you")
"""
new_code = code.expandtabs(4)
print(new_code)

a = "小乖乖，小一一".replace('小乖乖','小宝宝')
print(a)

a = 'HOW ARE YOU'.translate(str.maketrans("ABCDEFG", '1234567'))
print(a)

a = 'HOW ARE YOU'.translate(str.maketrans("ABCDEFG", '1234567', "HOW"))
print(a)

# 字符串判断
a = 'I love you'.startswith('i')
print(a)
a = 'I love you'.startswith('I')
print(a)
a = 'I love you'.endswith('you')
a = 'I love you'.endswith('u')
print(a)

x = '我爱这个世界'
if x.startswith(('你','我','他')):
  print('总有人爱着这个世界')

x = 'how are you'
print(x.istitle())
print(x.isupper())
print(x.islower())
print(x.isspace())
print(x.isalpha()) 

print("howareyou".isalpha())
print("  \n".isspace())

print(x.isprintable())
print("how are you\n".isprintable())

# 判断字符为数字
x = '12345'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

x = '2²'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

x = 'Ⅰ Ⅱ Ⅲ'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

x = '一二三'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

x = '壹贰叁'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

# 是否为python保留关键字
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('while'))
print(keyword.iskeyword('const'))

# 字符串截取
x = '        左侧不留空白'.lstrip()
print(x)
x = '右侧不留白         '.rstrip()
print(x)
x = '          左右不留白         '.strip()
print(x)
# 匹配其中出现的字符
x = 'www.baidu.com'.lstrip('blowback.')
print(x)
x = 'www.baidu.com'.removeprefix()
print(x)
x = 'www.baidu.com'.removesuffix()
print(x)

# 拆分&拼接
x = ''