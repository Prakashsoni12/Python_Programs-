import math
#this is the docString,(we can only write docstring in this way only)
def add_number(x,y):
    '''this function takes 
         two arguments.
    '''
    return x+y
    
print(add_number(10,5))
print(add_number.__doc__)
print(dir(math))