
f = open('fileHandling.txt', 'r')

# data = f.read()            #reads the whole file
# characters = f.read(5)    #read specified characters from the file
line1 = f.readline()        # READS entire line
print(line1)

line2 = f.readline()
print(line2)


f.close()



file = open('writeFile.txt', 'w') 
file.write('This is a sample file')

file = open('writeFile.txt', 'a')
file.write('\nThis data is appended.')


file.close()






#file opening different modes
# r, w, a   read, write, append mode
# r+    read and write(overwrite)     (pointer at begining), NO TRUNCATE
# w+    read and write(overwrite)       TRUNCATE
# a+    read and append              pointer at end, NO TRUNCATE

# TO DELETE A PYTHON FILE, THERE IS NO f.remove() fun
# FOR WE HAVE TO IMPORT A MODULE NAMED 'OS', AND USE ITS FUN remove
# import os
# os.remve('file_name')