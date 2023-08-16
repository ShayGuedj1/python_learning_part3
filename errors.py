import username
import password

class UsernameContainsIllegalCharacter(Exception):
    """Raised when username contains illegal characters"""
    pass

class UsernameTooShort(Exception):
    """Raised when username is too short"""
    pass

class UsernameTooLong(Exception):
    """Raised when the username is too long"""
    pass

class PasswordMissingCharacter(Exception):
    """Raised when the password is missing at least one mandatory character"""
    pass

class PasswordTooShort(Exception):
    """Raised when the password is too short with less than 8 characters"""
    pass

class PasswordTooLong(Exception):
    """Raised when the password is too long with more than 40 characters"""
    pass

def check_username(username):
    if not (username.has_digit() and username.has_underscore() and username.is_alpha()):
        raise UsernameContainsIllegalCharacter

    if username.isshort():
        raise UsernameTooShort

    if username.islong():
        raise UsernameTooLong

def check_password(password):
    if not (password.is_alpha() and password.is_digit() and password.is_lower()
            and password.is_capital() and password.special_char()):
        raise PasswordMissingCharacter

    if password.passshort():
        raise PasswordTooShort

    if password.passlong() and not password.passshort():
        raise PasswordTooLong



try:
    check_username(username.user1)
except UsernameContainsIllegalCharacter:
    print("Error: UsernameContainsIllegalCharacter.\nUsername contains an illegal character or is missing a mandatory character.\n")
except UsernameTooShort:
    print("Error: UsernameTooShort.\nUsername is too short.\n")
except UsernameTooLong:
    print("Error: UsernameTooLong.\nUsername is too long.\n")

try:
    check_password(password.pass1)
except PasswordMissingCharacter:
    print("Error: PasswordMissingCharacter.\nPassword is missing a special character.\n")
except PasswordTooShort:
    print("Error: PasswordTooShort.\nPassword is too short.\n")
except PasswordTooLong:
    print("Error: PasswordTooLong.\nPassword is too long.\n")
