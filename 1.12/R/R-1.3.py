# =======================================
# R-1.3
# 编写一个Python函数minmax(data)，用来在数的序列中找出最小数和最大数，并以一个长度为2的元组的形式返回。注意：不能通过内置函数min和max来实现
def minmax(data):
    min = 0
    max = 0
    n = 0
    for member in data:
        if member > max:
            max = member
        if member < min:
            min = member
    return min,max
data = (1,-42,3,53,5,6,7)
print(minmax(data))