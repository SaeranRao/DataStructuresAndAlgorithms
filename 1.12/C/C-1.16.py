# =======================================
# C-1.16
# 在1.5.1节scale函数的实现中，循环体内执行的命令data[j] *= factor。我们已经说过这个数字类型是不可变的，操作符 *= 在这种背景下使用是创建了一个新的实例，(而不是现有实例的变化)。那么scale函数是如何实现改变调用者发送的实际参数呢？
# 答，函数传入的是data实参，在函数中通过=更新data中的元素
import random
def scale(data,factor):
    for j in range(len(data)):
        data[j] *= factor
        

l = [random.randrange(100) for k in range(1,6)]

print(l)
scale(l,2)
print(l)