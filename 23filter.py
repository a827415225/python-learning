#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6])))


def del_space(n):
    return n and n.strip()

print(list(filter(del_space,['A', '', 'B', None, 'C', '  '])))