import username
import password
import errors

user = username.user1

pwd = password.pass1

# userillegalchar = errors.UsernameContainsIllegalCharacter()
# usertooshort = errors.UsernameTooShort()
# usertoolong = errors.UsernameTooLong()
# passinvalidchar = errors.PasswordMissingCharacter()
# passtooshot = errors.PasswordTooShort()
# passtoolong = errors.PasswordTooLong()
# This function checks that all the parameters are correct. If somthing is miising,
# it will alert using the try and exept.
def check_input(username, password):
    # If the passowrd and username are correct, it will print ""
    if username.username_length() and username.has_digit() and username.has_underscore() and username.is_alpha() and \
            password.is_alpha() and password.is_digit() and password.special_char() and password.is_lower() and \
            password.is_capital() and password.password_length():
        print("ok")


check_input(user, pwd)
