# Name : BARYEH, MICHAEL OSEI AGYEMANG
# Index : 1647617

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

        # trying to put result to a variable

        print("Shift key " + str(counter) + "  : " + result)
    print(" \n This is the list of all possible decryption. Look through to find the most likely message")


brute_force()

