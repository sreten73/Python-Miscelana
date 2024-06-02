import re
import string
import random

# function for generating password
def gen(passlen):
    # all capital letters from A-Z
    s1 = string.ascii_uppercase
    # all lower case letters from A-Z
    s2 = string.ascii_lowercase
    # all numbers from 0-9
    s3 = string.digits
    # all special characters
    s4 = string.punctuation

    # create a list of all the characters
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # generate random list of the all characters
    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    return pas

# check if password has lowercase, uppercase and digit
def check_password():

    while True:

        # ask user for the length of the passwords
        passlen = int(input("Enter lenght of the password(Minimal number of character is 10):\n "))

        # generating password
        new_pass = gen(passlen)

        if len(new_pass) < 10:
            print ( 'Please, your password is less than 8 characters. Try again.' )
            continue

        if lowcase.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a lowercase character' )
            print ( 'Please, try again unless use at least one lowercase' )
            continue

        if upcase.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a uperrcase character' )
            print ( 'Please, try again unless use at least one uppercase' )
            continue

        if digit.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a digit character' )
            print ( 'Please, try again unless use at least one digit' )
            continue

        if punctuation.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a special character' )
            print ( 'Please, try again unless use at least one special character' )
            continue
        else:
            print ( 'New Password is valid and saved' )
            break
    return new_pass


lowcase = re.compile(r'[a-z]')
upcase = re.compile(r'[A-Z]')
digit = re.compile(r'(\d)')
punctuation = re.compile(r'\W')

new_pass_1 = check_password()

print(f'Your password is: {new_pass_1}')