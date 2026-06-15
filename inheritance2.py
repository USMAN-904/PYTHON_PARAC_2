
# multi-level inheritance

class a:
    def funA(self):
        print('This is class a')

class b(a):     # class b is inherited from a
    def funB(self):
        print('This is class b')

class c(b):     # class c is inherited from b, b is inherited from a
    def funC(self):
        print('This is class c')


obj = c()
obj.funA()
obj.funB()
obj.funC()





# multiple inheritance: inheritance from more than one class

class a:
    def funA(self):
        print('\nThis is class a')

class b:    
    def funB(self):
        print('This is class b')

class c(b,a):     # class c is inherited from both b and a
    def funC(self):
        print('This is class c')


obj = c()
obj.funA()
obj.funB()
obj.funC()