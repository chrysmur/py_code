from abc import abstractmethod, ABC

'''
    We define a abstract class with abstract method username_params 
    Subclasses will have to define what their usernames should look like
'''
class BaseUser(ABC):
    
    def __init__(self, username):
        self.username = username
        super().__init__()

    @abstractmethod
    def username_params(self):
        pass


class User(BaseUser):
    def username_params(self):
        if not self.username.isalnum():
            self.username = "defaultuser"
        

# we can have an implementation in the abstract calss
class BaseUser(ABC):
    
    def __init__(self, username):
        self.username = username
        super().__init__()

    @abstractmethod
    def username_params(self):
        print("Implementation code for ", self.username)
        pass

class NewUser(BaseUser):
    def username_params(self):
        super().username_params()
        print("Do the checks now")

#TESTS
#user = UserModel() # Throws an exception TypeError: Can't instantiate abstract class BaseUser with abstract methods username_params
user = User("#$ja") # username = "#$ja, which is not alnum"
user.username_params() # now username = defaultuser
user = NewUser("kris") # username = kris
print(vars(user))