

class Teacher:
    def __init__(self):
        # self.name = name
        # self.branch = branch
        # self.college = college
        print("Teacher Constructor is Called")
        
class Students(Teacher):
    def __init__(self):
        super().__init__()
        print("Student Constructor is called")
        


s = Students()

print(s)
        
    