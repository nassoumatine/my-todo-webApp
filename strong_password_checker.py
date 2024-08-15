"""
This program checks the strength of a given password based on three conditions
"""

password = input("Enter new password: ")
result = []
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)
# Checking if there is a number in the password
digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

# Checking if there is at least one upper character
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")

