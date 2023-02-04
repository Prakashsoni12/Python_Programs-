q1 = """ Is Python case sensitive when dealing with identifiers?
a. Yes
b. No
c. Machine Dependent
d. None"""

q2 = """ Which of the following is not a keyword?
a. eval
b. assert
c. local
d. Pass"""

q3 = """" Which one of these is floor Division?
a. /
b. //
c. %
d. None"""

q4 = """"What is the output of this 3*1**3?
a. 27
b. 9
c. 3
d. 1"""

q5 = """" "a"+"bc" =??
a. a
b. bc
c. bca
d. abc"""

quetions = {q1:'a',q2:'a',q3:'b',q4:'c',q5:'d'}

name = input("Enter Your Name: ")
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print("Hello ",name," Welcome to the quiz world!")
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

score = 0
for i in quetions:
    print()
    
    print(i)
    print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    flag1 = input("Do you want to skip this quetions(yes/no): ")
    print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    if flag1 == "yes":
        continue
    ans = input('Enter your answer (a/b/c/d): ')
    if ans==quetions[i]:
        score = score+1
        print()
        print('|*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*|')
        print("    Correct answer, you got", score ," score.")
        print('|*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*|')
    else:
        score = score-1
        print('x-x-x-x-xx-x-x-x-xx-x-x-x-xx-x-x')
        print(" Wrong answer, you lost -1 pont. ")
        print('x-x-x-x-xx-x-x-x-xx-x-x-x-xx-x-x')
    print()
    print('^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^') 
    flag2 = input("Do you wants to quit the quiz(yes/no): ")
    print('^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^')
    if flag2 == "yes":
        break
print()
print('*~*~*~*~*~*~*~*~*~*~*~*~')   
print("Final Score: ",score)
print('*~*~*~*~*~*~*~*~*~*~*~*~')  

        
        
        
        
        