class Node:
    def __init__(self, data=0, next=0):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_begging(self, data):
        node = Node(data, self.head)
        self.head = node

    def printl(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 and index > self.get_length():
            raise Exception('Invalid case')

        if index == 0:
            self.add_at_begging(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 and index > self.get_length():
            raise Exception('Invalid case')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


root = LinkedList()
# root.insert_values(["banana", "mango", "grapes", "orange"])
root.add_at_begging(10)
root.add_at_begging(20)
root.add_at_begging(30)
root.printl()
root.get_length()
