"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；

利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；

20万到40万之间时，高于20万元的部分，可提成5%；

40万到60万之间时高于40万元的部分，可提成3%；

60万到100万之间时，高于60万元的部分，可提成1.5%；

高于100万元时，超过100万元的部分按1%提成。

从键盘输入当月利润I，求应发放奖金总数？
"""
def funcname(x):
    bonus = 0
    if x <= 100000:
        bonus = x*0.1
    elif x > 100000 and x <= 200000:
        bonus = 10000 + (x-100000)*0.075
    elif x > 200000 and x <= 400000:
        bonus = 10000 + 7500 + (x-20000)*0.05
    elif x > 400000 and x <= 600000:
        bonus = 10000 + 7500 + 10000 + (x-400000)*0.03
    elif x > 600000 and x <= 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + (x-600000)*0.015
    elif x > 1000000:
        bonus=10000+7500+10000+6000+6000+(i-1000000)*0.01
    print(bonus)
funcname(int(input()))
