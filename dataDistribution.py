from numpy import random
import  numpy as np

x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x)
print('----------------------------------')
#random parmutation
ar = np.array([1,2,3,4,5,6])


random.permutation(ar)
print(ar)