import collections

def count_characters(file_path):
    # create an empty dictionary
    char_count = {}
    # open the file for reading
    with open(file_path, 'r') as file:
        # read the contents of the file
        contents = file.read()
        # iterate over each character in the file
        for char in contents:
            # if the character is already in the dictionary, increment the count
            if char in char_count:
                char_count[char] += 1
            # if the character is not in the dictionary, add it with a count of 1
            else:
                char_count[char] = 1
    return char_count

result = count_characters("example.txt")
print(result)


def count_characters(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return dict(collections.Counter(contents))

result = count_characters("example.txt")
print(result)
