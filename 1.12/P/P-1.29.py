# =======================================
# P-1.29
# 编写一个Python程序，输出有字母'c','a','t','d','o','g'组成的所有可能的字符串（每个字母只能用一次）
def combination(current_s,single_s,letters):
    if single_s in current_s:
        return
    current_s += single_s
    if len(current_s) == len(letters):
        print(current_s)
        return
    last_letters = []
    #计算剩余可选字母
    for n in range(0,len(letters)):
        if letters[n] != single_s:
            last_letters.append(letters[n])
    # print("last",last_letters)
    for data in last_letters:
        combination(current_s,data,letters)
# letters = list('catdog')
letters = list('catdog')
for data in letters:
    # print(data)
    combination('',data,letters)