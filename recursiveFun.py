
# RECURSION
# WHEN A FUNCTION CALLS ITSELF REPEATEDLY IS CALLED RECURSION

def recursiveFun(num):
    if num == 0:
        return           #RETURNS nothing, RETURNS the control back to the calling fun (called base case)
    print(num)          # will go infinite if base case is not used
    recursiveFun(num-1) #num-1=4, num-2=3, num-3=2, num-4=1, num-5=0; num=5

recursiveFun(5)


# CALCULATING FACTORIAL USING RECURSIVE FUNTION
# n! = (n-1)! * n
def Fact(n):
    if n==0 or n==1:
        return 1        # Fact(0) and fact(1) =1, so return 1
    return Fact(n-1)*n  # n! = (n-1)! * n

print('\nCalculated factorial:', Fact(4))



#CALCULATING SUM FROM 1 TO N USING RECURSION
def sumOFn(n):
    if n==0:
        return 0
    return sumOFn(n-1) + n

sum = sumOFn(5)
print('\nSUM from 1 to N is', 'is:', sum)



#RECUSIVE FUNTION TO PRINT ALL ITEMS OF A LIST
def printList(fruits, idx=0):
    if idx == len(fruits):
        return
    print(fruits[idx])
    printList(fruits, idx+1)

fruits = ['apple','banana','mango','orange']
printList(fruits)