import unittest #import unittestmodule
from user import User #import the user class

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("MilcahMuraguri","#Youcannotfind5") #new User created