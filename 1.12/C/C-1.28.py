# =======================================
# C-1.28
# 在n维空间定义一个向量v = (v1,v2,...vn)的p范数，如下所示：（略过）,对于p=2的特殊情况，这就成了传统的欧几里得范数，表示向量的长度。例如，一个二维向量坐标为(4,3)的欧几里得范数为(4的平方+2的平方)的根号2次方等于（16+9）的开2次方等于根号25等于5。编写norm函数，即norm(v,p),返回向量v的p范数的值，norm(v)，返回向量v的欧几里得范数。你可以假定v是一个数字列表。 
import random
def nor(v):
    p = 2
    totals = 0
    for single in v:
        totals += single ** 2
    return (totals ** (1/2))

v = [random.randrange(1,100) for i in range(1,random.randrange(1,6))]
# v = [3,4]
print(v)
print(nor(v))