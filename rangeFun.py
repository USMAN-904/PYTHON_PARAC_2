
# range() fun is a special fun, returns a sequence of numbers
# starting from zero (by default) and increases by one (by default) 
# but must have to specify size in parenthsis (not default)

# range(start, stop, step) #start and step are bydefault one - step=increment
# range(optional, required, optional)


print(range(5)) #not indexible

# seq = range(5)
# print(seq[0])
# print(seq[1])

# #or
# seq = range(5)
# for i in seq:
#     print(i)

# #or
# for i in range(5):        #start 0, upto 5, increment 1
#     print(i)


# for i in range(2,12,2):   # start from 2 to 12, incement by 2
#     print(i)                # also a way to print even or odd numbers or tables

# #HOW TO PRINT 0 TO 100 EVEN NUMBERS
# for i in range(0,100,2):
#     print(i)

#TABLE OF A NUMBER
no = int(input('enter a number 2-12:')) 
for i in range(1,13):
    print(no,'*',i,'=',no*i)
