#列表是一系列按特定顺序排列的元素组成
#列表是有序集合

digits = ['11', '22', '33', '44']
print(digits[0])
#[-1]最后一个元素  [-2]：返回倒数第二个元素
print(digits[-1])
print('#####################################')

#可像使用变量一样使用列表中的其他元素
print('my favorite number is:'+digits[2])
print('#####################################')

names = ['xiaoliuliu', 'xiaoyuanyuan']
print(names[0])
print(names[1])
print('#####################################')

#修改列表中的元素
digits = ['11', '22', '33', '44']
digits[0] = '00'
print(digits)
print('#####################################')

#列表中添加元素
digits = ['11', '22', '33', '44']
digits.append('55')
print(digits)

#列表中插入元素
digits = ['11', '22', '33', '44']
digits.insert(2, '99')
print(digits)
print('#####################################')

#删除列表中的元素  del  指定索引值删除
digits = ['11', '22', '33', '44']
del digits[0]
print(digits)

#括号内不添加索引值，默认删除最后一个元素，反之按照索引删除  pop()
digits = ['11', '22', '33', '44']
digits.pop(0)
print(digits)

#若列表中有重复的元素，默认删除第一个出现的值   remove()
digits = ['11', '22', '33', '44']
digits.remove('11')
print(digits)
print('#####################################')

#列表正向排序 sort()
list1 = ['cc', 'bb', 'dd', 'aa']
list1.sort()
print(list1)
print('#####################################')

list2 = ['cc', 'bb', 'dd', 'aa']
list2.sort(reverse=True)
print(list2)

#临时排序  sorted()
list3 = ['cc', 'bb', 'dd', 'aa']
#print('list3 is:', list3.sorted())
print(sorted(list3))




#反向打印列表   reverse()
list4 = ['cc', 'bb', 'dd', 'aa']
list4.reverse()
print('list4 is:', list4)


#确定列表的长度
list5 = ['11', '33', '55']
print(len(list5))





