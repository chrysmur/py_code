#!/usr/bin/python3
'''
By making attributes public, we make it difficult to change the setter and getter methods in the future
we can access instance.x = 1, or using the interface instance.set_x(9)
There should be only one way of modifying x
Instead of making x private and using setter and getter like in java
We using properties to show that the method handling x ought to be treated like an attribute
'''
class P:
    '''
    We have to call  get_x and set_x to handle x
    we can call instance.x = 9 but this is setting a new variable that doesnt alredy exist
    '''
    def __init__(self, x):
        self.set_x(x)
    
    def get_x(self):
        return self.__x 

    def set_x(self, x):
        if x < 0:
            self.__x = x
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

class P1:
    '''
    x as property defines getter method and x.setter defines the setter method
    by defining setter as x we can call self.x = x in init
    '''
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x 
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = x
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


class P2:
    '''
    By making x= property we can set the values by assign instance.x = 0 and 
    also by calling setter and getter method. Which is bad

    '''
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x 
    
    def set_x(self, x):
        if x < 0:
            self.__x = x
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(get_x, set_x)

class P3:
    '''
    To solve P2 we make setter and getter methods to be private

    '''
    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x 
    
    def __set_x(self, x):
        if x < 0:
            self.__x = x
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)

class Robot:
    '''
    If an attribute is needed by users, make it public.
    if an attribute is needed but it requires some processing, maybe checks  before assignment,
    or calculation, make it a property with @
    '''
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable"
        elif s <= 0:
            return "I feel bad"
        elif s <= 10:
            return "Seems to be okay"
        else:
            return "Great"


x = Robot("marvo", 1989, 0.2, 0.4)
y = Robot("Cal", 1889, -0.4, 0.3)

print(x.condition)
print(y.condition)
