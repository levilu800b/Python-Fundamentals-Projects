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

# Solution 2

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")