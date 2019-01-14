# =======================================
# R-1.1
# 编写一个Python函数is_multiple(n,m)用来接收两个整数值n和m，如果n是m的倍数，即存在整数i使得n=mi，那么函数返回True否则返回False
def is_multipke(n,m):
    if n % m == 0:
        return True
    else:
        return False
print(is_multipke(9,4))