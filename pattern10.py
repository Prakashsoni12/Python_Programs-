n = int(input("Enter Number: "))
for i in range(0,n):
    for j in range(0,n):
        if i == 0 or j ==(n-1) or i==j:
            print("*",end='')
        else:
            print(end=' ')
    print()
    
