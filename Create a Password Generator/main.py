# Password Generator Project

import random

# ASCII Characters to use in the password
ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_numbers = "0123456789"
ascii_symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"

# Ask the user how many letters, numbers and symbols they want in their password
num_letters = int(input("How many letters would you like in your password? \n"))
num_numbers = int(input("How many numbers would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like in your password? \n"))
num_total = num_letters + num_numbers + num_symbols

# Create a list of random letters, numbers and symbols
password_list = []
for character in range(0, num_letters):
    password_list.append(random.choice(ascii_letters))
for character in range(0, num_numbers):
    password_list.append(random.choice(ascii_numbers))
for character in range(0, num_symbols):
    password_list.append(random.choice(ascii_symbols))

# Shuffle the list
random.shuffle(password_list)

# Convert the list to a string
password = ""
for character in range(0, num_total):
    password += password_list[character]

# Print the password
print(f"Your password is: {password}")

# Output
# How many letters would you like in your password? 5
# How many numbers would you like in your password? 5
# How many symbols would you like in your password? 5
# Your password is: 4@3&2%1!5