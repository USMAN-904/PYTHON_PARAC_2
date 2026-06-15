
# class student:
#     name = None
#     fatherName = None
#     address = None

#     def inputData(self):
#         self.name = input('Input std Name:')
#         self.fatherName = input('Enter FatherName:')
#         self.address = input('Enter his/her add:')

#     def printData(self):
#         print(self.name, 's/o', self.fatherName, 'Vil:', self.address)

# Student_1 = student()
# Student_1.inputData()
# Student_1.printData()






class car:
    def __init__(self):    #constructor, auto called on creation of obj
        self.handBrake = True
        self.clutch = False
        self.switch = False
        self.acc = False
        
    def startCar(self):
        self.handBrake = False  #hand break tured off
        self.clutch = True      #clutch pressed
        self.switch = True      #switch turned on (key inserted and turned)
        self.acc = True         #accelerator pressed
        print('Car started.')      #car started

carStart = car()
carStart.startCar()