#!/usr/bin/python3
'''
descriptors are object attributes with binding behavior.
One whose attribute access has been overridden by  methods in the descriptor protocol
the methods include __set__, __get__, __delete__
When an object has any of these methods, it said to be a descriptor

These methods enables addition of managed attributes to the class
The properties class used in @properties, has these methods implemented

when trying to get a value, we check if the value exists in .__dict__ of the class where the descriptor is used
if no value is found, it checks the type(obj) which is the where all classes are extended  https://python-course.eu/python3_descriptors.php
it continues to check through the base classes, excluding the metaclasses
Descriptors are the primary mechanism behind properties, methods, static methods, class methods and super()
'''

class A:
    class_att_A = "class attribute of A"

    def __init__(self):
        self.instance_att_A = "instance attribute of A instance"


class B(A):
    class_att_AB = "class attribute of B"

    def __init__(self):
        super().__init__()
        self.instance_att_AB = "instance attribute of B instance"

'''
# descriptor protocol
from property_deco import cls_property
# cls_property is a descr
descr.__get__(self, obj, objtype=None) #return value
descr.__set__(self, obj, value) # return none
descr.__delete__(self, obj)  # return none
'''
'''
Non data descriptor have only __get__() defined which usually happns to methods
data descriptor  defines __set__ and __delete__
'''

class Descriptor:
    def __init__(self, initval = None):
        print("initializing Descriptor with initval")
        self.__set__(self, initval)

    def __get__(self, instance, owner):
        print("instance and owners", instance, owner)
        print( "Getting self.val", self.val)
        return self.val ** 2

    def __set__(self, instance, value):
        print("Setting self.val to ", value)
        self.val = value


class Myclass:
    x = Descriptor(4)

m = Myclass()
print(m.x)

# We can write descriptors to divert calls to get and set to our own.
# when myclass is called to set value x, it diverts the responsibility to desciptor class which then calls __set__
# this is how property works