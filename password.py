## create a class
class User:
    """generate an instance of a class
    """
    user_list=[]#list of users
    def __init__(self,username,password):
        self.username = username
        self.password =password