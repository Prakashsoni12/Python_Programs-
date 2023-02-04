n = int(input("Enter Number: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==4 or col-row==2 or row-col==2 or row+col==8:
            print("*",end='')
        else:
            print(end=' ')
    print()
