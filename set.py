
# unique, immmutable and unordered

my_set = {2, 4, 6, 4, 'usman', 'usman'}

print('the list:', my_set)   # will ignore 4 and 'usman'
print('its sze:', len(my_set)) #return 4 (ignores duplicacy) 

# first_print -> {2, 4, 'usman', 6}
# second print -> {'usman', 2, 4, 6}
# means unordered

# immutable: existing values are immutable, rest of list is mutable means we can add, remove items
# funtions

my_set.add(10) #add 10
my_set.remove(2)    #remove 2
print('\nupdated set:\n', my_set)

# pop() fun: remove/prints random value from list
print('\nRandom value throgh pop fun:', my_set.pop())

my_set.clear()
print('\nafter clearing list:\nThe list:', my_set)
print('its sze:', len(my_set))


# union() and intersectin() funtions

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('\n union of sets:\n', set1.union(set2))
print('\n intersection of sets:\n', set1.intersection(set2))

