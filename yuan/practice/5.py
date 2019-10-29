'''
输入三个整数x,y,z，请把这三个数由小到大输出
'''

def funcname():
    print("请输入三个整数，逗号分隔")
    list = input().split(",")
    list.sort()
    print(list)
funcname()
