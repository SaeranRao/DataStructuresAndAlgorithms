# =======================================
# C-1.27
# 在1.8节中，我们对于计算所给整数的因子时提供了3种不同的生成器的实现方式。1.8节末尾处的第三种方法是最有效的，但我们注意到，它没有按递增顺序来产生因子。修改生成器，使得其按照递增顺序来产生因子，但同时保持其性能优势。 
def factors(n):
    k=1
    while k <= n:
        yield k
        k += 1

for i in (factors(5)):
    print(i)