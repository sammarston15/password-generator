from random import choice, randint, shuffle
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password(data):

    password_list = []
    password_uppercase = list(string.ascii_uppercase)
    password_lowercase = list(string.ascii_lowercase)
    password_numbers = list(string.digits)
    password_symbols = list(string.punctuation)

    # build password information based on user input
    if data['uppercase'] == 'on':
        password_list += password_uppercase
    if data['lowercase'] == 'on':
        password_list += password_lowercase
    if data['numbers'] == 'on':
        password_list += password_numbers
    if data['symbols'] == 'on':
        password_list += password_symbols
    if data['length']:
        # shuffle the password
        shuffle(password_list)

        # set the password length the user chose
        password_list = password_list[:int(data['length'])]


    # build default password information if no user input
    if (data['length'] == '' and data['uppercase'] == None and data['lowercase'] == None 
                                and data['numbers'] == None and data['symbols'] == None):
        password_list = password_uppercase + password_lowercase + password_numbers + password_symbols

        # shuffle the password
        shuffle(password_list)

        # set password length to 13 characters by default
        password_list = password_list[:13]


    # merge the password list back into a string
    password = "".join(password_list)
    # print(password)

    # return the password    
    return password




