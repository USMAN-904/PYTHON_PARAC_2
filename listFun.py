#the same or mostly functions apply to tuples and strings as well
list_1 = ['JAMAL', 203, 17, 'Karo Dara']

print(list_1)
print(list_1[0])

list_2 = [12, 36, 78, 45]
list_2.append(302)
list_2[2] = 25 #list is mutable, unlike string which is immutable

print('updated list:', list_1)

list_3 = [56, 69, 75, 40]
list_3.sort()
print('ascending sort:', list_3)

list_4 = [45, 56, 98, 12]
list_4.sort(reverse=True)
print('descending sort:', list_4)

list_5 = [45, 89, 21, 53]
list_5.reverse() # reverse the value as they are
print('reversed list:', list_5)

list_6 = [12, 45, 66, 78]
list_6.insert(1,70)
print('after insertion:',list_6)