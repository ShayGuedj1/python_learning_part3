import string
class Password:

    # This is the default password for this class.
    def __init__(self, password):
        self.password = password
        #print(password)

    # This method checks that the password in long enough and not too long.
    def password_length(self):
        if 8 <= len(self.password) < 40:
            return True
        else:
            return False

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
        return any(string.punctuation for _ in self.password)

#This is a function to verify that the methods are able to find an incorrect rule or character.
def legal():
    if is_alpha and is_digit and is_special and is_lower and is_capital and is_long:
        print("password is valid")
    else:
        print("password not valid")

#This creates a password by calling the class Password, and ask the user to put an input.
pass1 = Password(input("please enter the password: "))

# Those are calls of the methods on the password we created.
is_capital = pass1.is_capital()
is_lower = pass1.is_lower()
is_digit = pass1.is_digit()
is_alpha = pass1.is_alpha()
is_special = pass1.special_char()
is_long = pass1.password_length()

#Those are tests to see that the functions and the methods are working as expected.
# print("\nalpha\n--------")
# print(pass1.is_alpha())
# print("\ndigit\n--------")
# print(pass1.is_digit())
# print("\ncapital\n---------")
# print(pass1.is_capital())
# print("\nlower\n--------")
# print(pass1.is_lower())
# print("\nlength\n--------")
# print(pass1.password_length())
# print("\nspecial\n--------")
# print(pass1.special_char())
# print("**********")

legal()
