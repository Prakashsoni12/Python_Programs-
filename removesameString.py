lis = ['geekseeks','for','geekseeks']
word = 'geekseeks'
n =  2
count =0
for i in range(0,len(lis)):
    if (lis[i]==word):
        count = count+1
    if count == n:
        del lis[i]

print(lis) 