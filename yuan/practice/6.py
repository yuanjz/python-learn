'''
斐波那契数列
'''
def funcname(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return funcname(n-1) + funcname(n-2)
print(funcname(int(input())))
