print('''list的定义使用中括号，
tuple定义使用小括号，
dict和set的定义使用大括号，但是在引用时使用中括号
''')




#dict (dictionary)
d = {'TOM':90,'BOB':95,'TIM':98}
print(d)
print(d['TOM'])

print('这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。')

print('由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：')

print(d['TOM'])
d['TOM'] = 91
print(d['TOM'])


print('要避免key不存在的错误，有两种办法，一是通过in判断key是否存在')
print('Thomas' in d)

print('二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：')

print(d.get('Thomas'))
print(d.get('Thomas',-1))

print('要删除一个key，用pop(key)方法，对应的value也会从dict中删除：')
print(d.pop('BOB'))
print(d)

print('''请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

    和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    
    而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。''')
    
    
#set
print('set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。')
print('要创建一个set，需要提供一个list作为输入集合：')    
s = set([1, 2, 3])
print('注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。')

print('重复元素在set中自动被过滤：')
print('s = set([1, 1, 2, 2, 3, 3])')
s = set([1, 1, 2, 2, 3, 3])
print(s)

print('通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：')
print('s.add(4)')
s.add(4)
print(s)
print('s.add(4)')
s.add(4)
print(s)


print('remove(key)方法可以删除元素：')
print('s.remove(4)')
s.remove(4)
print(s)


print('set可以看成数学意义上的无序和无重复元素的集合')
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)

print((s1 and s2))
print((s1 or s2))

print(True&False)
print(False&True)
print(True|False)
print(~True)
print(~False)
print('符号和英文的区别：&和|是针对所有的，而英文的and or not则是只针对布尔变量的')


print('set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象')


print('对于可变对象，比如list，对list进行操作，list内部的内容是会变化的')
print('a = [\'c\',\'b\',\'a\']')
a = ['c','b','a']
print('a.sort()')
a.sort()
print(a)


#再议不可变对象
print('对于不可变对象，比如str，对str进行操作结果')
print('a = \'abc\'')
a = 'abc'
print('a.replace(\'a\', \'A\')')
print(a.replace('a', 'A'))
print(a)
print('虽然字符串有个replace()方法，也确实变出了\'Abc\'，但变量a最后仍是\'abc\'')

#一个行之有效的办法是
b=a.replace('a', 'A')
print(b)


grade={'他':75,'她':80,'它':95}#初始化
exit=input('欢迎使用学生管理系统,进入系统请按y：')#界面提示
menu=['1.录入','2.查询','3.修改','4.学生列表','5.退出']
flag=(exit=='y')#进入系统
while flag:
    for item in menu:
        print('\t'+item)#菜单
    orderer=input('请输入操作序号:')
    while orderer=='1':
        print('开始录入……')
        user=input('请输入学生姓名：')##姓名可能出错，最好判定下







