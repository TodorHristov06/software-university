class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass


def password_too_common(pwd, specials):
    only_digits = pwd.isdigit()
    only_chars = pwd.isalpha()
    only_specials = all(ch in specials for ch in pwd)
    return only_digits or only_chars or only_specials


MIN_PWD_LEN = 8
SPECIAL_CHARACTERS = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < MIN_PWD_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    
    if password_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    
    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    
    print("Password is valid")

