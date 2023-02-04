import numpy as np
from numpy import random

#x = random.randint(100,size=(3,5))
arr = np.array([41,42,2,3,4,6,7,8,9])
# filter_array = []
# for even in arr:
#     if even%2==0:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)
             
# newarr  = arr[filter_array]

filter_array = arr%2==0
newarr = arr[filter_array]
print(newarr)
print(arr)