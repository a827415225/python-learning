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

