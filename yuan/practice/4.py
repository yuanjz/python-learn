"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def funcname():
    print("input year:")
    year = int(input())
    print("input month:")
    month = int(input())
    print("input day:")
    day = int(input())
    total = 0
    total = day
    while month > 1:
        total+=month_days[month-1]
        month-=1
    if year%400==0 or year%4==0:
        total+=1
    print("total:", total)
funcname()