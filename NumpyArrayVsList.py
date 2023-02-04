import numpy as np
import sys
import time
# lista = range(100000)
# arr11 = np.arange(100000)
# print(sys.getsizeof(87)*len(lista))
# print(arr11.itemsize*arr11.size)

# x = range(10000000)
# y = range(10000000,20000000)
# start_time = time.time()
# c = [x+y for x,y in zip(x,y)]
# print(time.time()-start_time)
a = np.arange(10000000)
b = np.arange(10000000,20000000)
start_time = time.time()
x = a+b
print(time.time() - start_time)