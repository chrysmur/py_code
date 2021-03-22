# python-course.eu robot class
import random
class Robot:
    __illegal_names = {'Tony', 'Sabonis'}
    __crucial_health_level = 0.6

    def __init__(self, name):
        self.name = name
        self.health_level = random.uniform(0.5,1) # generate health 

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, name):
        if name in type(self).__illegal_names:
            name = "Rob"
        self.__name = name

    def __add__(self, other):
        # Add two instances by name
        return type(self)(self.__name + '-' + other.__name)

    def need_a_doc(self):
        if self.health_level < type(self).__crucial_health_level:
            return True
        return False

class NurseRobot(Robot):

    def __init__(self, name):
        super().__init__(name)
        self.power = random.uniform(0.8, 1)

    def heal(self, robot):
        if robot.health_level < self.health_level:
            robot.health_level = random.uniform(robot.health_level, self.power)
        
class NinjaRobot(Robot):
    __damage = 0.2
    def __init__(self, name):
        super().__init__(name)

    def attack(self, rival):
        '''We only fight ninjas like us, it about honor'''
        if isinstance(rival, NinjaRobot):
            rival.health_level = rival.health_level * type(self).__damage
        
class NinjaNurseRobot(NinjaRobot, NurseRobot):
    def __init__(self, name):
        super().__init__(name)
    
