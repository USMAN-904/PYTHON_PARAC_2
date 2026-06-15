
# public attributes and funtions are used/ACCESSED outside the scope of a class
# but private attri and funs cann't be accessed outside any class

# to make an attribe or function private, just write double underscore before its name.
# they are used/called within class by other function

#EXAMPLE
class Person:
    def __init__(self, name):
        self.pname = name

    def hello(self):
        print('Hello,', self.pname)
    def __hello(self):    #this is a private fun (we can call it from another fun within the class)
        print('Hello,', self.pname)

P1 = Person('KHALIL')
print(P1.hello())    #legal
print(P1.__hello()) #comp illegal
