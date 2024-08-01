# Recursion
# Factorial (5) => 5X4X3X2X1
def factorial(num):
    if(num==1):
        return 1
    return num * factorial(num-1)
    
print(factorial(4))