import random
import string

def gen_random_pass(length):
    if length < 6:
        return "Password length must be at least 6 characters"
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

len=int(input("Enter the length of password: "))
print(gen_random_pass(len))
