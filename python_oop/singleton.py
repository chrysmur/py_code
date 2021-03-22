'''
Singleton is a design pattern that restricts the instantiation of class to exactly one object

'''
class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class SingletonCls(metaclass=Singleton):
    #do stuff
    pass


s = SingletonCls()
s2 = SingletonCls()
print(s == s2)


class Singleton2:
    _instance = None
    def __new__(cls, *args, **kwargs): 
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs) # if this is ommited or super, the instance wil not be created
        return cls._instance

class SingletonCls(metaclass=Singleton):
    #do stuff
    pass

s = SingletonCls()
s2 = SingletonCls()
print(s == s2)
