class check_div:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i==0:
                print("you can't dive change the input!!")
        else:
            self.func(*args,**kwargs)
                
@check_div
def div(a,b):
    return a/b
@check_div
def div1(a,b,c):
    return a/b/c

print(div(12,5))
print(div1(20,4,2))