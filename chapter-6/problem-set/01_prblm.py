
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))



if(a>b and a>c and a>d):
    print("Number is A: ",a)
elif(b>a and b>c and b>d):
    print("Number is B: ",b)
elif(c>a and c>b and c>d):
    print("Number is C: ",c)
else:
    print("Number is D: ",d)