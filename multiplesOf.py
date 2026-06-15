
num = int(input("enter a number:"))
mulOf = int(input('Enter multple of nUmber (2-10):'))

if mulOf % num == 0:
    print(mulOf, 'is multiple of ', num)
else:
    print(mulOf, ' is Not a multiple', num)