n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j == n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

def pattern(n):
    cen = n//2+1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == cen:
                print('*',end='')
            else:
                print(" ",end='')
        print()
pattern(5)
    
