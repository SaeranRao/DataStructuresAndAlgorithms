# =======================================
# R-1.6
# 编写一个Python函数，用来接收正整数n，并返回1～n中所有奇数的平方和
def odd_square_sum(n):
    s = 0
    for k in range(1,n):
        if(k%2 == 1):
            s += k
    return s
print(odd_square_sum(5))

    
