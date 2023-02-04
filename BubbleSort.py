#bubble sort program in asceding order
li = [10,17,0,23,4,2,6,23]
print("Unsorted list: ",li)
for j in range(len(li)-1):
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            li[i], li[i+1] = li[i+1],li[i]      
print("Sorted list :", li)

#bubble sort proggramm in descending order
lis = [10,17,0,23,4,2,6,23]
print("unsorted list :", lis)
for j in range(len(lis)-1):
    for i in range(len(lis)-1):
        if lis[i]<lis[i+1]:
            lis[i],lis[i+1] = lis[i+1],lis[i]      
print(lis)

