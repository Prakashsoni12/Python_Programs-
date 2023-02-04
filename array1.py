import array as ar
import numpy as np

arr = ar.array('i', [1,2,3,4,5,6,5,5,7,8,9])
print(arr[2])
print(arr[2:5])
print(arr.count(5))
y = arr.tolist()
print(y)
x = np.array(
    [[5,6,8],
    [5,6,8]]
)
xx = np.array(
    [[5,6,8],
    [5,6,8]]
)
for i in range(2):
    for j in range(2):
        print(x[i][j]+xx[i][j],end='')
