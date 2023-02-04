## Prime number proggram
# first_n = int(input("Enter Number: "))
# secon_n = int(input("Enter Last Number: "))
# for num in range(first_n,secon_n+1):
#      if num > 1:
#          for i in range(2,num):
#              if(num%i)==0:
#                  break
#          else:
#              print(num)
            
# num = int(input("Enter Number: "))
# i = 2
# while i< num:
#     if num%i==0:
#         print(num,"is not prime number as it is",num//i,"times,",i)
#         break
#     i += 1
# else:
#     print(num, "is prime number")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for i in range(1,21):
    if is_prime(i):
        print(i)

#
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
        return 'prime'
    else:
        return 'Not prime'
print(prime(7))