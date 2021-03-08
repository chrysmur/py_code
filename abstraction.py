#!/usr/bin/python3

# Data Abstraction = Data encapsulation  + Data Hiding
# Encapsulation is bandling of data with methods that operate on the data,
# Information hiding is making inaccessible internal information of a class so that it cant be changed accidentally
# Encapsulation involves the getter and setter methods

# There should be only one way to change the attributes

class Robot:
    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year

    def use_name(self):
        if self.name:
            print(f"{self.name} is available")
        else:
            print("This class has no attribute name")

        if self.build_year:
            print(f"last update in {self.build_year}")
        else:
            print(f"year of creation unknown")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, year):
        self.build_year = year

    def get_build_year(self):
        return self.build_year

    def __repr__(self):
        return f"Class name {self.name}"


if __name__ == "__main__":
    # instantiate class
    robot = Robot('optimus 1', '2065')

    # do we have attribute name?
    robot.use_name()

    # set name
    robot.set_name("new name")

    # Use name again
    robot.get_build_year()

    # Get name
    print(robot.get_name())
