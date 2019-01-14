# =======================================
# R-1.12
# Python的random模块包括一个函数choice(data),可以从一个非空序列返回一个随机元素。Random模块还包含一个更基本的的randomrange函数，参数化类似与内置的range函数，可以在给定范围内返回一个随机数，只是用randrange函数，实现自己的choice函数
import random
def def_c_choice(data):
    return data[random.randrange(0,len(data))]


l = [1,22,56,3,87]
print(def_c_choice(l))
print(random.choice(l))