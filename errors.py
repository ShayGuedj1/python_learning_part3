import username
import password

class UsernameContainsIllegalCharacter(Exception):
    """Raised when username contains illigal characters"""
    pass
# If the username is missing a special character, it will notify the user.
try:
    if not (username.user1.has_digit() and username.user1.has_underscore() and username.user1.is_alpha()):
        raise UsernameContainsIllegalCharacter
    else:
        pass
except UsernameContainsIllegalCharacter:
    print("Error: UsernameContainsIllegalCharacter.\nUsername contains an illegal character or missing a mandatory character.\n")

class UsernameTooShort(Exception):
    """Raised when username is too short"""
    pass
# If the username is too short, it will notify the user.
try:
    if username.user1.isshort():
        raise UsernameTooShort
    else:
        pass
except UsernameTooShort:
    print("Error: UsernameTooShort.\nUsername is too short.\n")

class UsernameTooLong(Exception):
    """Raised when the username is too long"""
    pass
# If the username is too long, it will notify the user.
try:
    if username.user1.islong():
        raise UsernameTooLong
    else:
        pass
except UsernameTooLong:
    print("Error: UsernameTooLong.\nUsername is too long.\n")

class PasswordMissingCharacter(Exception):
    """Raised when the password is missing at least one mandatory character"""
    pass
# If the password is missing a special character, it will notify the user.
try:
    if not (password.pass1.is_alpha() and password.pass1.is_digit() and password.pass1.is_lower()
            and password.pass1.is_capital() and password.pass1.special_char()):
        raise PasswordMissingCharacter
    else:
        pass
except PasswordMissingCharacter:
    print("Error: PasswordMissingCharacter.\nPassword is missing a special characters.\n")

class PasswordTooShort(Exception):
    """Raised when the password is too short with less than 8 characters"""
    pass
# If the password is too short, it will notify the user.
try:
    if password.pass1.passshort():
        raise PasswordTooShort
    else:
        pass
except PasswordTooShort:
    print("Error: PasswordTooShort.\nPassword is too short.\n")

class PasswordTooLong(Exception):
    """Raised when the passowrd is too long with more than 40 characters"""
    pass
# If the password is too long, it will notify the user.
try:
    if password.pass1.passlong() and not password.pass1.passshort():
        raise PasswordTooLong
    else:
        pass
except PasswordTooLong:
    print("Error: PasswordTooLong.\nPassword is too long.\n")
