def replacechar(string, old_char,new_char):
    strnew_char = ''
    for i in string.casefold():
        if old_char == i:
            strnew_char = strnew_char+new_char
        else:
            strnew_char = strnew_char+i
    return strnew_char

string = "Hello WOrld"
new_string = replacechar(string,'o','g')
print(new_string)

def replchar(string,old_char,new_char):
    return string.replace(old_char,new_char)

string = "Hello WOrld"
new_string = replchar(string,'o','g')
print(new_string)