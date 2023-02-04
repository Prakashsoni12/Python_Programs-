def check_unique(numbers):
    unique_num = set(numbers)
    if len(unique_num) == len(numbers):
        return True
    else:
        return False

numbers = [1,2,3,4,5,6]
print(check_unique(numbers))
numbers1 = [1, 2, 3, 4, 5, 5]
print(check_unique(numbers1))