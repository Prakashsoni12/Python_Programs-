def quicksort(arr):
    # base case: if the length of the array is 0 or 1, it is already sorted
    if len(arr) <= 1:
        return arr
    # choose the pivot as the middle element of the array
    pivot = arr[len(arr) // 2]
    # create sub-arrays for elements less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # recursively sort the left and right sub-arrays and concatenate the results
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


