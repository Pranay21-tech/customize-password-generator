# customize-password-generator
A customizable password generator is a tool that lets you create strong, unique passwords by allowing you to specify the type of characters, length, and other parameters you want. These generators are essential for online security, helping you create passwords that are difficult to guess or crack. 
Key features of a customizable password generator:
Password Length:
You can specify how many characters you want in your password. 
Character Types:
You can choose to include uppercase letters, lowercase letters, numbers, and symbols in your password. 
Exclusions:
Some generators allow you to exclude specific characters, like similar-looking characters (e.g., 1 and l) or symbols that might be confusing. 
Word Incorporation:
Some generators allow you to add a word or phrase to your password, making it more memorable while still being strong. 
Randomness:
Good generators produce genuinely random passwords, making them difficult to guess or crack. 
Benefits of using a customizable password generator:
Stronger Passwords:
Customizable generators allow you to create passwords that are more complex and harder to crack. 
Unique Passwords:
By generating unique passwords for each account, you reduce the risk of a hacked account compromising other accounts. 
Increased Security:
Strong, random passwords help protect your accounts from unauthorized access. 
Ease of Use:
Password generators make it easy to create strong passwords without having to manually create them. 










💻 Custom Password Generator in Python
This script allows you to generate secure, customizable passwords based on user preferences. It also supports inserting a chosen word or name at a specific position (start, middle, or end) within the generated passwords.

📦 Features
Include a custom word or name in the password
Choose the position of the custom word (start, middle, or end)
Select the character types to include:
Uppercase Letters (A-Z)
Lowercase Letters (a-z)
Numbers (0-9)
Symbols (!@#$%&* etc.)
Set password length (minimum 6 characters)

Generate multiple passwords at once

Save all generated passwords to a file: generated_passwords.txt
🪟 How to Run on Windows
✅ 1. Make sure Python is installed
Open Command Prompt and check:
bash
python --version
If not installed, download and install Python from https://www.python.org/downloads/. Make sure to check the box “Add Python to PATH” during installation.

✅ 2. Save the script
Open Notepad or any text editor.

Paste your Python code.

Save the file as password_generator.py (make sure the extension is .py, not .txt).

✅ 3. Run the script
Open Command Prompt, navigate to the folder where the script is saved using cd:

bash
cd path\to\your\folder
Run the script:

bash
python password_generator.py
The program will run in the terminal and prompt you for inputs.

Enter a Name or Word that you want to include in Password: John
where do you want your name/word in the password? (start/middle/end): middle
This Includes the Upppercase in the password ? (y/n): y
This Includes the Lowercase in the password ? (y/n): y
This Includes the Numbers (0-9) in the password ? (y/n): y
This Includes the symbols(@#!$&*) in the password ? (y/n): y
Enter the desired total  password length (min 6): 12
How many passwords would you like to generate?: 5


📝 Output
Generated passwords will be printed on the screen and saved to:

generated_passwords.txt
Example content:

Generated Passwords:
1: A2@Jo#hn5!c
2: M@Jo2hn7$c!
3: QwJo#hn9@Lp
...


🐧 How to Run on Linux
✅ 1. Check if Python is installed
Open a terminal and type:
bash
python3 --version
If not installed:

bash
sudo apt update
sudo apt install python3
✅ 2. Save the script
Open any text editor (e.g., gedit, nano, or VS Code).

Paste your Python code.

Save it as password_generator.py.
Example with nano:
bash
nano password_generator.py
Paste the code, press Ctrl+O to save, then Ctrl+X to exit.
✅ 3. Run the script
In the terminal:
bash
python3 password_generator.py
📁 Output Location
The generated passwords are saved in a file named:
generated_passwords.txt
This file will be located in the same folder where the Python script is run.
