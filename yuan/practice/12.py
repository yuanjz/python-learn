'''
判断101-200之间有多少个素数，并输出所有素数
'''
import math
def is_prime(n):
    i = int(math.sqrt(n))
    for j in range(2, i+1):
        if n % j == 0:
            return False
    return True
def func():
    total = 0
    for i in range(101, 201):
        if is_prime(i):
            print(i)
            total+=1
    print("总数：",total)
func()
