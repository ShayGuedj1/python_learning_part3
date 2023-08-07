class UsernameContainsIllegalCharacter(Exception):
    """Raised when username contains illigal characters"""
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
    """Raised when the passowrd is too long with more than 40 characters"""
    pass
