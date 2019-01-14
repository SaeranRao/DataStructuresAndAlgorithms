# =======================================
# C-1.25
# 编写一个Python函数，接收一个表示一个句子的字符串s，然后返回该字符串的删除了所有标点符号的副本。例如，给定字符串“Let's try ,Mike”，这个字符串将返回Lets try Mike
s = []
# print(ord(','))
str = input("请输入一段话:")
for single in str:
    #print(ord(single))
    if ord(single) not in range(33,48):
        s.append(single)
sep = ''
print(sep.join(s))