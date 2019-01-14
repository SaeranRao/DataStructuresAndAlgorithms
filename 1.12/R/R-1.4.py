# =======================================
# R-1.4
# 编写一个Python函数，用来接受正整数n，返回1～n的平方和。
def square_sum(n):
    total = 0
    for single in range(1,n):
        total += single ** 2
    return total
n = int(input("请输入正整数："))
print(square_sum(n))