from  collections import Counter
li = [1,2,3,4,5,6,6,7,8,9]

n = 6
count =0
for i in li:
    if i == n:
        count = count+1

print('{} has ocured {} times'.format(n,count))
x = 7
dic = Counter(li)
print(dic)
print('{} has ocured {} times'.format(x,dic[x]))
