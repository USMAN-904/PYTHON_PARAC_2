class student:
    name = None
    fatherName = None
    address = None

    def __init__(self):
        self.name = input('Input std Name:')
        self.fatherName = input('Enter FatherName:')
        self.address = input('Enter his/her add:')
        print('\n', self.name, 'S/O', self.fatherName, 'Vill:', self.address, end='\n\n')


    # def printData(self):
    #     print('\n', self.name, 'S/O', self.fatherName, 'Vill:', self.address, end='\n\n')

Student_1 = student()

Student_2 = student()
