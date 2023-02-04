li = [15,12,3,5,1,18,0]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j]<li[i]:
            temp = li[j]
            li[j] = li[i]
            li[i] = temp
print(li)

for i in range(len(li)):
    min = i
    for j in range(i+1,len(li)):
        if li[j]<li[min]:
            min = j
    li[min],li[i] = li[i],li[min]

print(li)
