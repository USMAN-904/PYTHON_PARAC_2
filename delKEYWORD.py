# del KEYWORD IS USED TO DELETE OBJ OR ATTRIBUTES OF OBJ
# OBJ OCCUPIES SPACE IN MEMORY, SO IT IS DELETED

class Student:
    def __init__(self, name):
        self.sName = name

Std1 = Student('AKRAM')
print(Std1)         #legal
print(Std1.sName)   #legal

# del Std1        # DELETES STD 1
# del Std1.sName   # delete attrib of obj

# print(Std1)     #error
# print(Std1.sName)   #error




