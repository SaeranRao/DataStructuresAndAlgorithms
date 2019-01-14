# =======================================
# C-1.22
# 编写一个Python程序，用来接收长度为n的两个整数型数组a和b并返回数组a和b的点积。也就是返回一个长度为n的数组c，即c[i]=a[i].b[i],for i = 0,...,n-1
import random
n = int(input("请输入数组长度n："))
a = [random.randrange(1,100) for k in range(1,n+1)]
b = [random.randrange(1,100) for k in range(1,n+1)]

c = []
for i in range(0,n):
    c.append(a[i]*b[i])

print(a)
print(b)
print(c)