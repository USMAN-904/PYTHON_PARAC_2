# STATIC, SUPER, CLASS & INSTANCE METHOD
# SUPER: a special method used to access/call methods of the parent class
# from child class - super().parClassMethod(self,name)

class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print('His name is', self.name,'age is', self.age)

    def designation(self, desig):
        self.desig = desig
        print('Designation is', self.desig)
        return desig

class child(parent):
    def profession(self, prof):
        self.prof = prof
        print('child profession is', super().designation(prof))

person1 = child('akbar', 45)
person1.designation('Currency exchanger')
person1.profession('Student')