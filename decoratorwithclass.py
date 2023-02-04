def check_name(method):
    def inner(name_ref):
        if name_ref.name == "Prakash":
            print("Both Names are same: ")
        else:
            method(name_ref)
    return inner

class Printing:
    def __init__(self,name):
        self.name = name
    @check_name
    def print_name(self):
        print("Entered user name is : ",self.name)
    
p = Printing("soni")
p.print_name()
        