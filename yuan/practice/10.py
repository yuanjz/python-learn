'''
暂停一秒输出，并格式化当前时间
'''
import datetime, time
i=0
while i<5:
    i+=1
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
