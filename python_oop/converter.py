
class Length:
    
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    
    def __init__(self, value, unit='m'):
        self.unit = unit
        self.value = value

    @property
    def value(self):
        return self.__value # in meters

    @value.setter
    def value(self, value):
        self.__value = value * type(self).__metric[self.unit]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Length(self.value+other)
        return Length(self.value  + other.value)
    
    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Length(self.value+other)
        self.value += other.value
        return type(self)(self.value)

    # add integer + class or vice versal
    def __radd__(self, other):
        return type(self).__add__(self, other) # self.__add__

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Length(" + str(self, value) + f", {self.unit}"

l = Length(3,'m')
l.x = 9