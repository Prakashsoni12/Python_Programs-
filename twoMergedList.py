'''Merge two sorted lists: Write a program that takes two sorted lists as input and returns a new list that contains all the elements of both lists in sorted order.
'''
def merge_sorted_lists(list1, list2):
    # merge the two lists
    merged_list = list1 + list2
    # sort the merged list
    merged_list.sort()
    return merged_list

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]

merged_list = merge_sorted_lists(list1, list2)
print("The merged list is: ",merged_list)
