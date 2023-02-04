my_dict = {}
my_dict[1] = 'one'
my_dict[2] = 'two'
my_dict[3] = 'three'
my_dict[4] = 'four'

print(my_dict)

d = dict([(1,'apple'),(2,'bat'),(3,'cat')])
print(d)

print(d.keys())
print(d.values())
print(d.get(1))

d[1] = 'Banana'
print(d)
d.setdefault(4,'hello')
d.setdefault(5)
print(d)
dd = {5:'bhopal',6:'indore',7:'rewa'}
d.update(dd)
print(d)

del d[7]
print(d)
d.pop(1)
print(d)
d.pop(6)
print(d)
