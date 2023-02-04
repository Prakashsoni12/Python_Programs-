'''Palindrome check: Write a program that checks if a given word or phrase is
 a palindrome (a word or phrase that reads the same forwards and backwards)'''

def revstring(string):
    rs = ''
    for i in string:
        rs = i + rs 
    if rs == string:
        return 'palindrom'
    else:
        return 'Not palindrom'

def palindrom_Str(word):
    return word == word[::-1]

string = 'Hello'
if palindrom_Str(string):
    print("String is palindrom")
else:
    print("String is not palindrom")



       
