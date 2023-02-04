def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@str_upper #decorator 
def print_str():
    return "Hello Good Morning!"
print(print_str())

print('------------------------------------')
#Decoratoe 2 example
def div_decorator(func):
    def inner(x,y):
        if y == 0:
            return "Given Proper Input"
        return func(x,y)
    return inner

@div_decorator
def div(a,b):
    return a/b
print(div(4,0))
        