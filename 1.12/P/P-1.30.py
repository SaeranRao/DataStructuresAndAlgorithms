# =======================================
# P-1.30
# 编写一个Python程序，输入一个大于2的正整数，求将该数反复被2整除直到商小于2为止的次数
n = 0 # declare a variable to save the number which is input by the user
try:
    n = int(input("请输入一个正整数:"))
    if n < 2:
        print("请输入正整数")
except ValueError as e:
    print("请输入正整数!",e)
times = 1
while n//2 >= 2:
    n //= 2
    times += 1
print("次数为：",times)