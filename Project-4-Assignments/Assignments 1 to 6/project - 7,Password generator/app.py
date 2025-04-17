import random
import string

def Generate_password(length = 12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

print (" 🚦 Welcome to the password generator")

user_input = int(input(" 🖇️   Enter the length for your password : \n"))

password = Generate_password(user_input)
print(" 🎯 Your password is here ", password)
