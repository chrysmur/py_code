

# A function to count the number of calls to a function
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__ = func.__name__

    return helper

@call_counter
def f():
    pass

print(f.calls) # returns 0
for  _ in range(10):
    f()
 
print(f.calls) # returns 10


# Similar to checking for condition before adding a method to a class
# we check the type of method in attribute dict and modify those methods to count the calls
class FuncCallCounter(type):
    #metaclass to decorate all the methods of subclass with call counter

    @staticmethod
    def call_counter(func):
        '''
        we create a wrapper function that counts how many times its is called,
        we assign the name of the func to be the name of the func so that we count the number of times func is called
        return wrapper
        '''
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        wrapper.__name__ = func.__name__
        return wrapper

    def __new__(cls, classname, superclasses, attributedict):
        # We modify the  new method which is called to create instances so that it modifies methods in the attributedict
        # we decorate all not primitive methods 
        for attr in attributedict:
            if callable(attributedict[attr]) and not attr.startswith("__"):
                attributedict[attr] = cls.call_counter(attributedict[attr])

        return type.__new__(cls, classname, superclasses, attributedict)

class A(metaclass=FuncCallCounter):

    def call1(self):
        pass
    
    def call2(self):
        pass


if __name__ == "__main__":
    x = A()
    print(x.call1.calls, x.call2.calls)
    x.call1()
    print(x.call1.calls, x.call2.calls)
    x.call1()
    x.call2()
    print(x.call1.calls, x.call2.calls)