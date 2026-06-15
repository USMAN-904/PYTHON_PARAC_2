# #TO PRINT SUM OF FIRST N NUMBERS
# n= int(input('input any number:'))
# sum = 0

# for i in range(1, n):
#     sum += i
# print('Sum of first', n, 'numbers is:', sum)


# #SAME LOGIC USING WHILE LOOP
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

#FACTORIAL -> MULTIPLICATION OF FIRST N NUMBERS
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print('fact of', n, 'is:', fact)

#FACTORIAL THROUGH FOR LOOP
n = 5
fact = 1
for i in range(1, n):
    fact *= i
print('Factorial :', fact)