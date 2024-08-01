
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


def greatesNumber(a,b,c):
    largest_num = a  
    
    if b > largest_num:
        largest_num = b
    if c > largest_num:
        largest_num = c
        
    return largest_num
    
print(greatesNumber(a,b,c))