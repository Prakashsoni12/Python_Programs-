# import math

# number = [1,2,3,4,5,6,7,8] 
# number[:3] = [-1,-2,-3] 
# print(number) 

# numbers = []
# for i in range(1,6):
#     numbers.append(2**i)
    
# print(numbers)

# numberss = [2**i for i in range(1,6)]
# print(numberss)
# nn = [49,64,81,100,121]
# new_list = [math.sqrt(n) for n in nn if n%2==0]
# print(new_list)

team1 = ['janet', 'luckey', 'moshy']
team2 = ['rockey', 'clerk', 'jhonson']

result = [(x,y) for x in team1 for y in team2]
print(result)

def function(n,list1=[]):
    list1.append(list1.append(n))
    return list1

for i in range(4):
    list2 = function(i)
print(list2)