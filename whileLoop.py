
myTuple = (10, 'jamil', 45, 'age')

# count = 0
# while count <=3:
#     print(myTuple[count])
#     count += 1

# count = 0
# while count < len(myTuple):
#     # if myTuple[count] == 45:
#     #     continue
#     #     count += 1
#     print(myTuple[count])
#     count += 1


# find a value in list or tuple

# py_tuple = (23, 45, 89, 55, 45, 88, 21)
# req_no = 55
# i = 0
# while i < len(py_tuple):
#     if py_tuple[i] == req_no:
#         print('Number found at index ', i)
#     else:
#         print('Searching for...')
#     i += 1

i = 0
while i<=10:
    if i%2 == 0:    #to print odd (for even i%2 != 0)
        i += 1
        continue
    print(i)
    i += 1