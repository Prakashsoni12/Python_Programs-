a = [10,20,30,40,50]
b = [1,2,3,4,5]
print(list(filter(lambda x: x ,a)))
print(list(filter(lambda x: x%2==1, b)))

print(list(filter(lambda x: x>25, a)))
print(list(filter(lambda x: x<=30, a)))

print(list(filter(lambda x: x, range(1,10))))
print(list(filter(lambda x:x%2 ==1, range(1,20))))
