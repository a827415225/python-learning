print('chr()把编码转换成对应字符')
print('chr(64) represent:',chr(64))


print('ord()把字符转换成对应编码')
print('ord(\'中\') represent:',ord('中'))


#Python的字符串类型是str，如果要在网络上传输，或者保存到磁盘上，
#就需要把str变为以字节为单位的bytes。Python对bytes类型的数据用带b前缀的单引号或双引号表示
#str通过encode()方法可以编码为指定的bytes

print('\'ABC\'.encode(\'ascii\')=','ABC'.encode('ascii'))
print('\'中文\'.encode(\'utf-8\')=','中文'.encode('utf-8'))

#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print('b\'ABC\'.decode(\'ascii\')=',b'ABC'.decode('ascii'))

print('b\'\xe4\xb8\xad\xe6\x96\x87\'.decode(\'utf-8\')=',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('要计算str包含多少个字符，可以用len()函数：')
print('len(\'ABC\')=',len('ABC'),'len(\'中文\')=',len('中文'))

print('len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数')
print('len(\'中文\'.encode(\'utf-8\'))=',len('中文'.encode('utf-8')))



print('''#!/usr/bin/env python3
# -*- coding: utf-8 -*-''')


print('格式化的输出')
print('\'Hello, %s\' % \'world\'')
print('Hello, %s' % 'world')
print('\'Hi, %s, you have $%d.\' % (\'Michael\', 1000000)')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%')
print('\'growth rate: %d %%\' % 7 =','growth rate: %d %%' % 7)


