'''Anagram check: Write a program that takes two strings as input and checks if they are anagrams of each other.
'''

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if is_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")