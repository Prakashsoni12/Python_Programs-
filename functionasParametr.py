def function1():
    print("I am function1")
    
def function2(func):
    print(" i am from function 2")
    func()

function2(function1)
