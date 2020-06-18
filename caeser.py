# Name : BARYEH,  MICHAEL OSEI AGYEMANG
# Index : 1647617
import random


# note to self
# Make it only alphabets
# functions start here
# Encrypting input
def encrypt(key):
    text = input(" Please enter text to encrypt \n")
    text = text.replace(" ", "")
    result = ""
    # taversing the text
    for i in range(len(text)):
        char = text[i]
        # if characters are Uppercase
        if char.isupper():
            result += chr((ord(char) + int(key) - 65) % 26 + 65)

        # if characters are lowercase
        else:
            result += chr((ord(char) + int(key) - 97) % 26 + 97)

    print("Text  : " + text)
    return result


# encrypting with random key
# def rand_encrypt():
#     text = input(" Please enter text to encrypt \n")
#     text = text.replace(" ", "")
#     key = input(" Input preferred key  \n (!!!Must be between 0 and 27) \n")
#     key = int(key)
#     result = ""
#     # taversing the text
#     for i in range(len(text)):
#         char = text[i]
#         # if characters are Uppercase
#         if char.isupper():
#             result += chr((ord(char) + int(key) - 65) % 26 + 65)
#
#         # if characters are lowercase
#         else:
#             result += chr((ord(char) + int(key) - 97) % 26 + 97)
#
#     print("Text  : " + text)
#     return result


# decrypting input

def decrypt():
    text = input(" Please enter encrypted text here \n")
    text = text.replace(" ", "")
    key = int(input("Enter decrypt key \n"))
    offset_key = 26 - key
    key = int(key)
    result = ""

    # taversing the text
    for i in range(len(text)):
        char = text[i]

        # encrypting Uppercase
        if char.isupper():
            result += chr((ord(char) + int(offset_key) - 65) % 26 + 65)

        else:
            result += chr((ord(char) + int(offset_key) - 97) % 26 + 97)

    print("Encrypted text  : " + text)
    print("Shift used : " + str(int(key)))

    return result


# using brute force
def brute_force():
    text = input(" Please enter encrypted text here \n")
    text = text.replace(" ", "")
    counter = 26

    for key in range(1, 26):
        counter = counter - 1
        result = ""
        for i in range(len(text)):
            char = text[i]
            # encrypting Uppercase
            if char.isupper():
                result += chr((ord(char) + int(key) - 65) % 26 + 65)
            else:
                result += chr((ord(char) + int(key) - 97) % 26 + 97)
        print("Shift key " + str(counter) + "  : " + result)
        # print(" \n " + result)
    print(" \n Look through to find the most likely message")


# Homepage
option = input(
    "\n \t\t\t Hello , Welcome to Caeser's Palace \n Choose your prefered option below \n\n 1. Encrypt Message "
    "\n 2. Decrypt Message \n 3. Brute Force \n 4. Find key (Experimental Stage) \n")

if option == '1':
    print(" 1.Encrypt with your key  \n 2.Encrypt with Random key")
    encrypt_input = input()
    if encrypt_input == '1':
        key = input(" Input preferred key  \n (!!!Must be between 0 and 27) \n")
        key = int(key)
        print("Encrypted Text : " + encrypt(key))
    elif encrypt_input == '2':
        n = random.randint(1, 26)
        key = n
        print("Encrypted Text : " + encrypt(key))
        print("Your key is : " + str(key))

if option == '2':
    print("Decrypted text: " + decrypt())
if option == '3':
    print(" This option provides a list of all possible decrypts \n")
    brute_force()
