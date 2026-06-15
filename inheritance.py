#single inheritance: one parent one child
#multi-level inheritance: parent - child - child
#multiple inheritance: more than one parent one child

class Car:          #general class - all cars hav these start/stop properties
    def start(self):
        print('Car can start.')

    def stop(self):
        print('Car can stopp.')



class toyotaCar(Car):       #specific car - specific properties -other prop are inherited
    def bulletproof(self):
        print('Car is bullet proofed.')



car1 = toyotaCar()

car1.start()    #method of base class
car1.stop()         #method of base class
car1.bulletproof()  #method of derived class

