###Password's Generator using python with user customize
import random
import string

# importing required Modules....

print ("Generate your customize Passaword>>>")

# Get any name or word's from the user....... 

base_name=input("Enter a Name or Word that you want to include in Password:")
position=input("where do you want your name/word in the password? (start/middle/end):") #htis line is used to specific position of name/word
#the position if it dosn't seleted any one then it will take start as default...
# Asking user preferences for character types from the user :
use_upper = input("This Includes the Upppercase in the password ? (y/n):").lower() == 'y'
use_lower = input("This Includes the Lowercase in the password ? (y/n):").lower() == 'y'
use_digits = input("This Includes the Numbers (0-9) in the password ? (y/n):").lower() == 'y'
use_symbols = input("This Includes the symbols(@#!$&*) in the password ? (y/n):").lower() == 'y'

# digits and symbols includes numbers(0-9),symbols includes (@#!$&*).....
 
#validateing the length of password
while True:
    try:
        length=int(input("Enter the desired total  password length (min 6):  "))
        if length < 6:
            print("The password must be in 6 characters long,check your input again!...")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
# Validate number of passwords
while True:
    try:
        count=int(input(" How many passwords would you like to generate?:"))
        if count <= 1:
            print("Please Enter the number greater than 1.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
##Build the character pool...
char_pool = ''
if use_upper:
    char_pool += string.ascii_uppercase  # 'A' to 'Z'
if use_lower:
    char_pool += string.ascii_lowercase  # 'a' to 'z'
if use_digits:
    char_pool += string.digits # '0' to '9'
if use_symbols:
    char_pool += string.punctuation # '@','#',etc....

##Default characters if nothing is selected..

if not char_pool:
    print("No Characters has selected, using all default characters is selected")
    char_pool = string.ascii_letters + string.digits +string.punctuation     #if user dosn't select any one of the condition then this block will take default characters

##Generate multiple passwords
with open("generated_passwords.txt", "w") as file:
  file.write("Generated Passwords:\n")
  print("Generated Passwords:")
  for i in range(count):
    remaining_length = length - len(base_name)
    if remaining_length < 0:
        # Trim base name if it's too long
        final_password = base_name[:length]
    else:
         random_part = ''.join(random.choices(char_pool, k=remaining_length))
         if position == 'start':
          final_password = base_name + random_part
         elif position == 'end':
          final_password = random_part + base_name
         elif position == 'middle':
          half = remaining_length // 2
          first_half = random_part[:half]
          second_half = random_part[half:]
          final_password = first_half + base_name + second_half
         else:
          final_password = base_name + random_part

    print(f"{i + 1}: {final_password}")
    file.write(f"{i + 1}: {final_password}\n") ## This is use to wirte the file /save the passwords.list

     ## Shuffles the characters so the base name isn’t always in the same place.
## Joins the list back into a string and prints the final password.
