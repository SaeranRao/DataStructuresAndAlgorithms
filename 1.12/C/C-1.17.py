# =======================================
# C-1.17
# 1.5.1节scale函数的实现如下。它能正常工作吗？请给出原因。
# def scal(data,factor):
    # for val in data:
    #     val *= factor
# 答：不能val是一个新的对象，并不影响data的值
import random
def scal(data,factor):
    for val in data:
        val *= factor
l = [random.randrange(100) for k in range(1,6)]
print(l)
scal(l,2)
print(l)