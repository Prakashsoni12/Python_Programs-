cube =lambda x: x*x*x
a = [1,2,3,4,5]
print(tuple(map(cube,a)))

print(list(map(lambda x:x*x,[1,2,3,4])))
def sum(x,y):
    return x+y

aa = [1,2,3,4]
bb = [2,3,4,5]
print(list(map(sum,aa,bb)))

print(list(map(lambda x,y: x+y, aa,bb)))