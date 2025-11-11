import random


def generate_password(length):
    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{};:,.<>?/'
    all_characters = letters_lower+letters_upper+digits+symbols
    password = ''
    for i in range(length):
        password += random.choice(all_characters)

    return password


length = int(input("Enter the desired password length:"))
password = generate_password(length)
print("Generated Password:", password)
