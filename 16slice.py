L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print('L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。')
L[:3]
print(L[-2:0])
L = list(range(100))
print(L)
#前10个数，每两个取一个
print(L[:10:2])
print(L[::5])

print(L[:])
print(L)


print('tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple')
a=(1,2,3,4,5)
print(type(a))
print(a[0:3])#用中括号
print('字符串\'xxx\'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：')
print('ABCDEFG'[:3])


#练习题
#! /usr/bin/python3
# -*- coding utf-8 -*-
def trim(s):
	while s[:1]==' ':
		s=s[1:]
	while s[-1:]==' ':
		s=s[:-1]
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!') 

	