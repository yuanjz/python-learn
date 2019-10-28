'''
001题目：有四个数字：1、2、3、4，
能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
def fun():
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            if i != j:
                for k in range(1, 5):
                    if k != i and k != j:
                        print(i*100+j*10+k)
                        count=count+1
    print(count)
fun()
