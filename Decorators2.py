def upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_d
@upper
def string():
    return "good moring"

print(string())