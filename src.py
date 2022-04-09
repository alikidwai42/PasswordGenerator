import random

CharacterSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_=?.,:\|}{[]"
while 1:
    password_length = int(input("Length of the password required: "))
    password_count = int(input("How many passwords you need: "))
    
    for count in range(password_count):
        password=""
        for x in range(password_length):
            password_character=random.choice(CharacterSet)
            password = password+password_character
        print("Here is your password: ",password)
