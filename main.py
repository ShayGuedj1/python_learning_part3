import username
import password
import errors

user = username.user1
pwd = password.pass1



def check_input(username, password):
    if username.username_length() and username.has_digit() and username.has_underscore() and username.is_alpha() and \
            password.is_alpha() and password.is_digit() and password.special_char() and password.is_lower() and \
            password.is_capital() and password.password_length():
        print("ok")
    else:
        print("notok")

check_input(user, pwd)
