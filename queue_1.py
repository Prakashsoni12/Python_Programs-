queue = []


def enqueue():
    element = input("Enter elements: ")
    queue.append(element)
    print(element, "is added to queue.")


def dequeue():
    if not queue:
        print("Queue is empty:")
    else:
        e = queue.pop()
        print("Element removed from queue", e)


def display():
    print(queue)


while True:
    print("Enter 1 for adding element, 2 for Deleting ,3 for display elements, 4 for exit. ")
    choice = int(input("Enter Number as mentioned above: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Inputted wrong input.")
