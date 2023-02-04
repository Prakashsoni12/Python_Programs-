# emptyset = {} #This is Dictionry
# empty_set = set()#this is set

# filled_set = {'apple','banana','orange'}
# print(filled_set)
# filled_set.add('Guavav')
# print(filled_set)

# s = {1,2,3,4,2,5,3,5,3,6,4,3,2,4,5,6,5,3,1,1,2,5,7,8,9}
# print(s)

# print(1 in s)#Membership operator
# s.add(10)
# print(s)
# s.remove(1)
# print(s)
# s2 = {1,2,'bhopal'}
# print(s|s2)#union operation
# s2.clear()
# print(s2)
# s1 = {1,2,3,4}
# s2 = {1,5,6,3}
# print(s1&s2)

word = "programming"
alphabets = {x for x in word}
print(alphabets)#set dose not containes duplicate so output has no duplcate characters
