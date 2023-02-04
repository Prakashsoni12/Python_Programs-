'''Fibonacci sequence: Write a program that generates the 
Fibonacci sequence up to a given number.'''

n = int(input("Enter Number: "))
a = 0
b = 1
print(a,b,end=' ')
for i in range(1,n+1):
    c = a+b
    print(c,end=' ')
    a = b
    b = c
    
