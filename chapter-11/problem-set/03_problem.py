class Employee:
    salary = 2433
    increment = 20
    
    @property
    def salary_after_increment(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @increment.setter
    def increment(self,salary):
        self.increment = (salary/self.salary)-1*100


e = Employee()

print(e.salary_after_increment)

