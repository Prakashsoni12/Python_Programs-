##print the armstrong number between 1 to 1000
# for i in range(1001):
#     num = i
#     result = 0
#     n = len(str(i))
#     while (i!=0):
#         digit = i%10
#         result = result+digit**n
#         i =i//10
#     if num == result:
#         print(num)

n = int(input("ENter number"))
r = 0
x = n
while n>0:
    a = n%10
    r = r+a*a*a
    n = n//10
if r == x:
    print("Armstrong")
else:
    print("Not armstrong")

