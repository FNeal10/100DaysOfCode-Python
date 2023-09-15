import random

lst_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst_numbers = '1234567890'
lst_symbols = '!@#$%^&*()'

num_of_letters = int(input("Enter number of letters: "))
num_of_numbers = int(input("Enter number of number: "))
num_of_symbols = int(input("Enter number of symbols: "))

pass_letter = random.choices(lst_letters,k=num_of_letters)
pass_numbers = random.choices(lst_numbers,k=num_of_numbers)
pass_symbols = random.choices(lst_symbols,k=num_of_symbols)

random.shuffle(pass_letter)
random.shuffle(pass_numbers)
random.shuffle(pass_symbols)

print(''.join(pass_letter+pass_numbers+pass_symbols))