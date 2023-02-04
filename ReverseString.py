'''Reverse a string: Write a program that takes a string as input and 
returns the reverse of the string.'''
def strrev(string):
    rs = ''
    for i in string:
        rs = i+rs
    return rs

string = 'Hello'
print(strrev(string))