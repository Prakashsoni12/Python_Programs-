n = int(input('Enter Number: '))
result = 0
for i in range(1,n):
    if(n%i)==0:
        result = result+i

if result == n:
    print(n,'Perfact number')
else:
    print(n,'Not Perfact Number')
       
        
lower = int(input('Enter First Number: '))
upper = int(input('Enter Second Number: '))

for num in range(lower, upper+1):
    result = 0
    for i in range(1,num):
        if num%i ==0:
            result = result+i
    if result == num:
        print(num)
            
