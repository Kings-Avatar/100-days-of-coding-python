letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
password=""
for i in range(1,nr_letters+1):
    pass_letters= random.choice(letters)
    password+= pass_letters
for j in range(1,nr_symbols+1):
    pass_symbols= random.choice(symbols)
    password+= pass_symbols
for j in range(1,nr_numbers+1):
    pass_numbers= random.choice(numbers)
    password+= pass_numbers
nr_password=len(password)
final_password=random.sample(password,nr_password)
output_password="".join(final_password)
print(output_password)
