class Username:
# This is the default of the username and all the methods are working according to this.
    def __init__(self, username):
        self.username = username
        

# This method checks that the input has at least one underscore.
    def has_underscore(self):
        return "_" in self.username

# This method checkes that the input has at least one digit.
    def has_digit(self):
        return any(char.isdigit() for char in self.username)

# This method checks that the input has at least one English letter.
    def is_alpha(self):
        return any(char.isalpha() for char in self.username)

    def isshort(self):
        if len(self.username) < 3:
            return True

    def islong(self):
        if len(self.username) > 16:
            return True

# This method checks that the input has the correct length between 3 and 16 characters.
    def username_length(self):
        if self.islong() and self.isshort():
            return False
        else:
            return True

    def legit(self):
        if self.username_length and self.has_digit and self.has_underscore and self.is_alpha:
            return True
        else:
            return False

# This creates a user by calling the class Username, and ask the user to put an input.
user1 = Username(input("enter name"))

# Those are calls of the methods on the user we created.
has_underscore = user1.has_underscore()
has_digit = user1.has_digit()
valid_length = user1.username_length()
is_alpha = user1.is_alpha()
short = user1.isshort()
long = user1.islong()
is_legit = user1.legit()
