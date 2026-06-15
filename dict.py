

myDict = {                      # are keys, values combinations
    'studen_name' : 'Wisal',        
    'student_age' : 16,
    'subjects' : {  # sub dictionary
        'eng' : 80,
        'urdu' : 90,
        'maths' : 100
    }
}

# print(myDict) # prints whole dictinary
print(myDict['studen_name']) #to print one value
print(myDict['subjects']['urdu'])   #to print value of nested dict

print(myDict.keys()) # prints all keys present in dic
print(myDict.values())

myDict.update({'fatherName':'Noor'}) #inserts key:value pair into existing dic
print('\n',myDict)


