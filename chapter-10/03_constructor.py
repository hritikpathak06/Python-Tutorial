# OOPS(Object Oriented Programming)
class Employee:
    language = "Python"
    salary = 13400
    
    def __init__(self,name,salary,language) : #dunder method called
        self.name = name
        self.salary = salary
        self.language = language
        print("I Am Creating an Object")
    

    

ritik = Employee("Kartik",4555,"Rust")

print(ritik.language,ritik.name,ritik.salary)



    