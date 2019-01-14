# =======================================
# C-1.14
# 编写一个Python函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的互不相同的数。
import random
def def_C_114(data):
    for n in data:
        for m in data:
            if m*n%2 == 1 and m != n:
                print(str(n)+"*"+str(m)+"的乘积为"+str(m*n))

l = [random.randrange(1,200) for k in range(1,random.randrange(2,5))]
print(l)
def_C_114(l)