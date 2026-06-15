 
#FUCTION TO CALCULATE FACTORIAL

def calcFact(num):
    fact = 1
    for i in range(1, num+1):   #1-6 (LAST IS NOT INCLUDED)
        fact *= i
    print('Factorial is',fact)
    
calcFact(5)

#FUNCTION TO CONVERT USD TO PKR
def usdTOpkr(usd_val):
    PKR = usd_val * 273
    print(usd_val,'USD =', PKR,'PKR')

usdTOpkr(5)