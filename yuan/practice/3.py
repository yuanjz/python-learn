"""
一个整数，它加上100后是一个完全平方数，
再加上168又是一个完全平方数，请问该数是多少？
"""
import math
def is_sqrt(n):
    a=int(math.sqrt(n))
    return a*a==n
def funcname():
    x=-100
    while x<10000:
        if is_sqrt(x+100) and is_sqrt(x+268):
            print(x)
        x=x+1
funcname()
