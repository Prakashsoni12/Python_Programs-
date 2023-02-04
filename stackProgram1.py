stack = []
def push():
    num = int(input("Enter Element : "))
    stack.append(num)
    print(stack)
    
def pop():
    if not stack:
        print("Stack Empty!!")
    else:
        e = stack.pop()
        print("Removed element is: ",e)

while True:
        match = input("Enter which operation you want performe: 1. Push, 2.Pop, 3.Quit")
        if match == "1":
            push()
        elif match == "2":
            pop()
        else:
            break
        