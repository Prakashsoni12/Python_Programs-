n= int(input("Enter Number: "))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=' ')
        k = k+1
    print()
        

s = input("Enter String")
length = len(s)
for i in range(length):
    for j in range(i+1):
        print(s[j],end=' ')
    print()
        
