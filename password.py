import random 
import pyperclip

class user:

    '''
    class that generates new instances of user
    '''

    new_account = []


    def _init_(self,first_name,second_name,email,password):
        '''
        method to define properties for our user objects

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

    def save_account(self):
        user.new_account.append(self)


    def generate_password(self):

        '''
        generate new password
        '''

        #characters to generate passwords
        letters = list(string.ascii_letters)
        digits = list(string.digits)
        special_characters = list("!@#$%^&*()")

        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        #length
        password_len = int(input("what length would you like your password to be :"))

        #number of characters
        letters_count = int(input("How many letters do you want in the password: "))
	    digits_count = int(input("How many digits do you want in the password: "))
	    special_characters_count = int(input("How many special characters do you want in the password: "))

        characters_count = letters_count + digits_count + special_characters_count

        #checking password length vs password count
        if characters_count > password_len:
		print("Characters total count is greater than the password length")
		return

        # initialize password
        password = []

        #pick random letters
        for i in range(letters_count):
		    password.append(random.choice(letters))

        #pick random digits
        for i in range(digits_count):
		     password.append(random.choice(digits))

        #pick random special characters
        for i in range(special_characters_count):
		     password.append(random.choice(special_characters))

        #checking for short password
        if characters_count < password_len:
		     random.shuffle(characters)
		for i in range(password_len - characters_count):
			password.append(random.choice(characters))

        
        #shuffle end result
        random.shuffle(password)

        #print list in string
        print("".join(password))







