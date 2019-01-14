# =======================================
# C-1.15
# 编写一个Python函数，用来接收一个整数序列，并判断是否所有数字都互不相同（即它们是不同的）
import random
def def_C_115(data):
    for n in range(0,len(data)):
        # print(data[n])
        # print(data[n + 1:])
        if data[n] not in data[n + 1:]:
            # print(data)
            return True
    return False

l = [random.randrange(1,10) for k in range(1,6)]
print(l)
print(def_C_115(l))