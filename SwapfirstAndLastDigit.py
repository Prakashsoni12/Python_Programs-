lis = [1,2,3,4]

size = len(lis)
# temp = lis[0]
# lis[0] = lis[size-1]
# lis[size-1] = temp
lis[0],lis[-1] = lis[-1],lis[0]

print(lis)

