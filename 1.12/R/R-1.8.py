# =======================================
# R-1.8
# Python允许负整数作为序列的索引值，如一个长度为n的字符串s，当索引值-n<=k<0时，所指的元素为s[k],那么求 一个正整数索引值j >= 0,使得s[j]指向的也是相同的元素
import random
n = int(input("请输入列表长度"))
m = int(input("请输入要显示的元素的索引"))
print(n)
s = []
for single in range(1,n+1):
    s.append(random.randint(1,100))
print(s)
print(s[m],s[m-n])
