import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
"""
EASY
for letter in range(0,nr_letters):
    print(rd.choice(letters), end="")
for symbol in range(0,nr_symbols):
    print(rd.choice(symbols), end="")
for number in range(0,nr_numbers):
     print(rd.choice(numbers),end="")
"""
password=[]
for letter in range(0,nr_letters):
    password.append(rd.choice(letters))
for symbol in range(0,nr_symbols):
    password.append(rd.choice(symbols))
for number in range(0,nr_numbers):
    password.append(rd.choice(numbers))
#print(password)
rd.shuffle(password)
print(password)

for c in password:
    print(c,end="")
