# =======================================
# C-1.23
# 给出一个Python代码片段的例子，编写一个索引可能越界的元素列表。如果索引越界，程序应该捕获该异常并答应以下错误消息："Don't try  buffer overflow attacks in Python!"
import random
l = [random.randrange(1,100) for k in range(1,6)]
print(l)

try:
    n = random.randint(0,10)
    print(l[n])
except:
    print(str(n) + " is out of range.Don't try  buffer overflow attacks in Python!")
