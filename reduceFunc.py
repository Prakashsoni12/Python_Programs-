from functools import reduce
import math
def show(n):
    s = 0
    for i in n:
        s = s+i
    return s
a = [1,4,7,9]
print(show(a))

##Using reduce function solving this program
b = [1,2,3,4,5]
print(reduce(lambda x,y:x+y, b))
print(reduce(lambda x,y:x+y, range(1,10)))
## Factorial program using reduce function
print(reduce(lambda x,y:x*y, range(1,6)))
print(reduce(lambda x,y:x+y, filter(lambda x:x%2==0, range(1,11))))

print(math.__doc__)
print(math.sqrt.__doc__)