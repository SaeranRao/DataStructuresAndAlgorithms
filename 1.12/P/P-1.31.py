# =======================================
# P-1.31
# 编写一个“找零钱”的Python程序。程序应该将两个数字作为输入，一个是需要支付的钱数，另一个是你给的钱数。当你需要支付的和所给钱数不同时，它应该返回所找的纸币和硬币的数量，纸币，硬币面值参考现政府的货币体系，试设计程序以便返回尽可能少的纸币和货币。
price_yuan = 0.0
pay_yuan = 0.0
change_yuan = 0.0
flag = True

value_yuan = (100,50,20,10,5,1,0.5,0.1)
info_yuan = {'100':['张','纸币'],'50':['张','纸币'],'20':['张','纸币'],'10':['张','纸币'],'5':['张','纸币'],'1':['张','纸币'],'0.5':['个','硬币'],'0.1':['个','硬币']}


try:
    price_yuan = float(input("请输入总价："))
    pay_yuan = float(input("请输入支付金额："))
    if price_yuan <= 0:
        raise ValueError("请输入正确的总价")
    if pay_yuan <= 0:
        raise ValueError("请输入正确的总价")
    change_yuan = round(pay_yuan - price_yuan,1)
    if change_yuan < 0:
        raise ValueError("请输入足够额度的支付金额")
except ValueError as e:
    print(e)
    flag = False
if flag:
    times = 0
    print("找零总额：",change_yuan,sep='')
    for n in range(0,len(value_yuan)):
        if change_yuan // value_yuan[n] >= 0:
            times = change_yuan // value_yuan[n]
            if times != 0:
                print(
                    value_yuan[n],'元的',
                    info_yuan[str(value_yuan[n])][1],
                    int(times),
                    info_yuan[str(value_yuan[n])][0],
                    sep = ''
                    )

            change_yuan = change_yuan - value_yuan[n] * times
            times = 0