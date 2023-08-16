import string
class Password:

# This is the default password for this class.
    def __init__(self, password):
        self.password = password

# This method checks if the password is too short.
    def passshort(self):
        if len(self.password) < 8:
            return True

# This method checks if the password is too long.
    def passlong(self):
        if len(self.password) > 40:
            return True

    # This method checks that the password in long enough and not too long.
    def password_length(self):
        if self.passlong() and self.passshort():
            return False
        else:
            return True

    # This method checks that there is at least one letter that is a capital letter.
    def is_capital(self):
        return any(char.isupper() for char in self.password)

    #This method checks that there is at least one letter that is a lower case letter.
    def is_lower(self):
        return any(char.islower() for char in self.password)

    # This method checks that there is at least one digit in the password.
    def is_digit(self):
        return any(char.isdigit() for char in self.password)

    # This method checks that the password contains only English characters.
    def is_alpha(self):
        return any(char.isalpha() for char in self.password)

    # This method checks if there is at least one special character in the password.
    def special_char(self):
        return any(char in string.punctuation for char in self.password)

    def legal(self):
        if self.is_alpha and self.is_digit and self.special_char and self.is_lower and self.is_capital and self.password_length:
            return True
        else:
            return False

#This creates a password by calling the class Password, and ask the user to put an input.
pass1 = Password(input("please enter the password: "))

# Those are calls of the methods on the password we created.
is_capital = pass1.is_capital()
is_lower = pass1.is_lower()
is_digit = pass1.is_digit()
is_alpha = pass1.is_alpha()
is_special = pass1.special_char()
is_long = pass1.password_length()
is_legal = pass1.legal()
short = pass1.passshort()
long = pass1.passlong()

