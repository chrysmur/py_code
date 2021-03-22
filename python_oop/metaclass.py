'''
We want to create classes that check a condition then adds a method in them if the condition is true
for instance, we can have students in various levels, and only have the thesis question in the phd students only
'''

def thesis(*args):
    return "Computer science related"

class Student:
    def __init__(self, name, level):
        self.name = name
        if level == "PhD":
            self.thesis = thesis

        
s1 = Student("sabs", "masters") # has no thesis
s2 = Student("Doms", "PhD")


# Using metaclasses
# metaclass a class that inherits from type, such that the init method instatiates not an instance of class but a class
class Student(type):
    def __init__(cls, clsname, superclasses, attributedict):
        print(cls, clsname) #<class '__main__.PhD'> PhD
        if clsname == "PhD":
            cls.thesis = thesis

class PhD(metaclass=Student):
    pass
class Masters(metaclass=Student):
    pass

p = PhD() # has thesis
m = Masters() # has no thesis





        

