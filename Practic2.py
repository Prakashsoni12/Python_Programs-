def palindrom_string(string):
    return string == string[::-1]

string = "pop"
if palindrom_string(string):
    print('palindrom')
else:
    print('Not palindrom')
