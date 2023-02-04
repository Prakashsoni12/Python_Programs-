import math
n = int(input('Enter Number: '))
result = math.factorial(n)
print("Factorial of", n,"is ",result)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n = int(input('ENter NUmber: '))
print(fact(n))

n = int(input("ENter Number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factoria of ",n," is ",fact)
    
