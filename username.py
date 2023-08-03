class User:
    def __init__(self, username):
        self.username = username
        print(username)

    def has_underscore(self):
        return "_" in self.username

    def has_digit(self):
        return any(char.isdigit() for char in self.username)

    def is_alpha(self):
        return any(char.isalpha() for char in self.username)

    def username_length(self):
        if 3 <= len(self.username) < 16:
            return True
        else:
            return False


user1 = User(input("enter name"))

has_underscore = user1.has_underscore()
has_digit = user1.has_digit()
valid_length = user1.username_length()
is_alpha = user1.is_alpha()

def legit():
    if valid_length and has_digit and has_underscore and is_alpha and not None:
        return True
    else:
        return False



print("\nunder\n--------")
print(user1.has_underscore())
print("\ndigit\n--------")
print(user1.has_digit())
print("\nlength\n--------")
print(user1.username_length())
print("\nalpha\n--------")
print(user1.is_alpha())
print("**********")
print(legit())
