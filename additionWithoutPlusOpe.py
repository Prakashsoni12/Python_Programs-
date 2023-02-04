def add(a, b):
    # bitwise OR operator
    while b:
        # bitwise AND operator
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

a = 5
b = 7
print(add(a, b))
