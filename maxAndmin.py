arr = [10,20,30,40,50]

max = arr[0]
n =len(arr)
for i in range(1,n):
    if arr[i]>max:
        max = arr[i]

print(max)

min = arr[0]
n =len(arr)
for i in range(1,n):
    if arr[i]<min:
        min = arr[i]

print(min)