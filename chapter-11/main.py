# Inheritance in oops
class Employee:
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The Name of the employee is {self.name} and the salary is {self.salary}")
      
      
class Coder:
    language = "Python"
    def print_language(self):
        print(f"Out of all language here is your language: {self.language}")  

        
class Programmer(Employee,Coder):
    company = "ITC Info Tech"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")
        
        
a = Employee()
b = Programmer()
c = Coder()

c.print_language("Javascrpt")

# print(a.company,b.company,b.show("Ritik",5000))