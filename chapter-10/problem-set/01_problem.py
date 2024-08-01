

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pinCode):
        self.name = name
        self.salary = salary
        self.pinCode = pinCode
    
    
p1 = Programmer("Ritik",5000,5858)

print(p1.company,p1.name,p1.pinCode,p1.salary)