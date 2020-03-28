'''
修改字符串的几个方法
'''
name = 'susie liu'
#首字母大写
print(name.title())
print('#####################################')

#全大写
print(name.upper())
print('#####################################')

#全小写
print(name.lower())
print('#####################################')

#合并拼接字符串  '+'
string = 'abc'
int = 123
string2 = 'def'
result = string + str(int) + string2
print(result)
print('#####################################')

#制表符或换行符添加空白
print('python')
print('\tpython')
print('\n\tlanguage\n\tpython')
print('#####################################')

#删除空白
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print('#####################################')

#两个int类型做加减乘除只能，结果只能是int；有一个是浮点型，结果就可以是浮点型
a = 3
b = 2
c = 3 / 2
print(c)
print('#####################################')

print(5+3)
print(9-1)
print(2+6)
print(16/2)
print('#####################################')

#最喜欢的数字8
favorite_number = 6
print('最喜欢的数字是：' + str(favorite_number))

import this

