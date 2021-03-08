# Password Generator
import random
letters_of_alphabet = ['a','b','c','d', 'e', 'f', 'g', \
'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t',\
'u','v','w','x','y','z','A','B','C','D', 'E', 'F', 'G', 'H',\
'I', 'J','K','L','M','N','O', 'P','Q', 'R','S','T', 'U', 'V', \
'W', 'X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%','&','(', ')', '*', '+']

print(" *****************Welcome to the Python Password Generator *******************")
# Get the number of letters, symbols and numbers in the password that user wants to add

number_letters = int(input("How many letters would you like in your password \n")
)
number_symbols = int(input("How many symbols would like ?\n"))
number_numbers = int(input("How many numbers would you like ? \n"))

password = ""
#easy method : Letters followed by symbols then numbers
# print the letters as random from the list
for char in range(1, number_letters+1):
    random_letter = random.choice(letters_of_alphabet)
    password += random_letter

# print symbols 
for char in range(1, number_symbols+1):
    random_symbol = random.choice(symbols)
    password += random_symbol

# print numbers
for char in range(1, number_numbers+1):
    random_number = random.choice(numbers)
    password += random_number

print(f"Using the format of letters followed by symbols followed by numbers \n password: {password}")
# hard method of having no order of letters, symbols or letters
# restricted to only number that users add as a constraint

password_length = number_numbers + number_symbols + number_letters

password_dict = { "letters": ['a','b','c','d', 'e', 'f', 'g', \
'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t',\
'u','v','w','x','y','z','A','B','C','D', 'E', 'F', 'G', 'H',\
'I', 'J','K','L','M','N','O', 'P','Q', 'R','S','T', 'U', 'V', \
'W', 'X','Y','Z'], "numbers": ['0','1','2','3','4','5','6','7','8','9'], 
"symbols": ['!', '#', '$', '%','&','(', ')', '*', '+']}
password_hard = ""
list_keys = ["letters", "numbers", "symbols"]
# randomize on the choice whether a char would be a letter, symbol or number

for char in range(1, password_length+1):
    char_type = random.choice((list_keys))
    password_hard = password_hard + random.choice(password_dict[char_type])

print(f"\n The password with random position of symbol, number or letter  is \n{password_hard}")
