# for loop is basically and mainly used for iteration/traversal purpose

# pyList = [23, 'khan', 78, 9.4, 0]

# for i in pyList:
#     print(i)

# name = 'Sharadha Khapra'
# for i in name:
#     print(i)


score = (23, 34, 67, 74, 32)
index = 0
val = 74
for i in score:
    if i == val:
        print('Number found', index)
    index += 1
    