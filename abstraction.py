#!/usr/bin/python3

# Data Abstraction = Data encapsulation  + Data Hiding
# Encapsulation is bandling of data with methods that operate on the data,
# Information hiding is making inaccessible internal information of a class so that it cant be changed accidentally
# Encapsulation involves the getter and setter methods

# There should be only one way to change the attributes

class Robot:
    #Class attributes
    Three_Laws = (
    """A robot may not injure a human being""",
    """A robot must obey the orders given to it by human beings""",
    """A robot must protect humans then its own existence""")
    __counter = 0
    __instance = None

    def __init__(self,
                 name=None,
                 build_year=None):
        self.__name = name
        self.__build_year = build_year
        #Count the  instances of this class type(self) evaluates to Robot
        type(self).__counter += 1
        type(self).__instance = self

    def __del__(self):
        type(self).__counter -= 1
    
    @classmethod
    def robot_instances(cls):
        return cls, Robot.__counter # Access class attr using the class
    
    # class method used where static methods have to call other static methods
    # instead of hardcoding the class name
    @classmethod
    def get_instance(cls):
        return cls.__instance

    @staticmethod
    def robot_creator():
        return "By Sabonis"

    def use_name(self):
        if self.__name:
            print(f"{self.__name} is available")
        else:
            print("This class has no attribute name")

        if self.__build_year:
            print(f"last update in {self.__build_year}")
        else:
            print(f"year of creation unknown")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, year):
        self.__build_year = year

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return self.__name
    
    def __str__(self):
        return self.__name

class Pet:
    _class_info = "pet animals"
    #by defining this method as a regular method
    #Class that import it and redefine _class_info will have their own displayed
    # def about(self):
    #     return "This calss is about " + self._class_info + "!"
    
    # making it static will ensure imports only display _class_info of imported
    # @staticmethod
    # def about():
    #     return "This class is about " + Pet._class_info + "!"

    #making it a class method imply that _class_info in inheriting classes 
    # will access about with their own class name and the new classinfo
    @classmethod
    def about(cls):
        return f"Class about {cls._class_info}"
class Dog(Pet):
    _class_info =  "man's best friend"


class Cat(Pet):
    _class_info = "All kinds of cats"

class Racoon(Pet):
    pass


if __name__ == "__main__":
    
    p = Pet()
    d = Dog()
    c = Cat()
    r = Racoon()

    print(p.about())
    print(d.about())
    print(c.about())
    print(r.about())