# =======================================
# C-1.24
# 编写一个Python函数，计算所给字符串中元音字母的个数
list_vowel = list('aeiou')
print(list_vowel)
input_str = input("请输入需要计算的字符串：")
totals = 0
for i in input_str:
    if i in list_vowel:
        totals += 1
print("字符串中的元音字母个数为"+str(totals))