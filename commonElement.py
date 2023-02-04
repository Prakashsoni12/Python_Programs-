'''Find the most common element in a list: Write a program that takes a list of integers as
 input and returns the most common element in the list.'''

from collections import Counter

def most_common_element(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

lst = [1, 2, 3, 4, 1, 2, 5, 2]
print(most_common_element(lst))
