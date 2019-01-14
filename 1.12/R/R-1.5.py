# =======================================
# R-1.4
# 编写一个Python函数，用来接受正整数n，返回1～n的平方和。
# R-1.5
# 基于Python的解析语法和内置函数sum，写一个单独的命令来计算R-1.4中的和。
n = int(input("请输入一个整数："))
s = [k*k for k in range(1,n)]
total = sum(s)
print(total)