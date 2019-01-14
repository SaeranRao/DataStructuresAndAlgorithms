# =======================================
# R-1.2
# 编写一个Python函数is_even(k),用来接收一个整数k，如果整数k是偶数返回True否则返回False，但是函数中不允许使用乘法/除法/或求余操作
def is_even(k):
    return False if (k+1)//2 != (k)//2 else True   
print(is_even(11))