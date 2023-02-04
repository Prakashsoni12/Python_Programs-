def div_decorator(func):
    def inner(*args):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i == 0:
                return "please Give proper input"
        return func(*args)
    return inner
        
@div_decorator
def div1(a,b):
    return a/b

@div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(10,5))
print(div2(12,4,10))
    