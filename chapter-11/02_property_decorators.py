# Property Decorators

class Employee:
    a= 1
    @classmethod
    def show(cls):
        print(f"The Class attribute of a is: {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    
    @name.setter
    def name (self,val):
        self.fname = val.split(" ")[0]
        self.lname = val.split(" ")[1]

        
        
e = Employee();

e.a = 45

e.name = "Rtitik Pathak"
print(e.lname,e.fname)

e.show()