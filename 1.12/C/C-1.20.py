# =======================================
# C-1.20
# Python的random模块包括一个函数shuffle(data),它可以接收一个元素的列表返回一个随机的重新排列元素，以使得每种可能的序列发生概率相等。random模块还包括一个更基本的函数randint(a,b),它可以返回一个从a到b(包括两个端点)的随机整数，只使用randint函数，实现自己的shuffle函数
import random
l = [random.randint(1,100) for k in range(1,6)]
print(l)
# random.shuffle(l)
s = []
for m in range(0,len(l)):
    n = random.randint(0,len(l) - 1)
    s.append(l[n])
    del l[n]
print(s)