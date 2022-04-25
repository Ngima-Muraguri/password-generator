import random 
import pyperclip

class user:
    new_account = []


    def _init_(self,first_name,second_name,email,password):
        '''
        Args:
            first_name:user first name.
            second_name :user second name.
            email:user email.
            password:user password
        '''

        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password