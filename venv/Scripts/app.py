# Name : BARYEH,  MICHAEL OSEI AGYEMANG
# Index : 1647617
from flask import Flask, flash, render_template, request
import random
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def choose():
    option = request.form['options']
    text = request.form['message']
    text = text.replace(" ", "")
    key = request.form['key']
    # key = int(key)
    option = request.form['options']
    result = ""
    error = "\nPlease choose an option from the above menu"

    if option == '0':
        return render_template('index.html', output=error)

    if option == '1':
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + int(key) - 65) % 26 + 65)
            else:
                result += chr((ord(char) + int(key) - 97) % 26 + 97)
        if request.method == 'POST':
            return render_template('index.html', output= " \n" + result)

    if option == '2':
        n = random.randint(1, 26)
        key = n
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + int(key) - 65) % 26 + 65)
            else:
                result += chr((ord(char) + int(key) - 97) % 26 + 97)
        if request.method == 'POST':
            return render_template('index.html', output= result + "\n Your key is " + str(key) )

    if option == '3':
        offset_key = 26 - int(key)
        result = ""
        # taversing the text
        for i in range(len(text)):
            char = text[i]

            # encrypting Uppercase
            if char.isupper():
                result += chr((ord(char) + int(offset_key) - 65) % 26 + 65)

            else:
                result += chr((ord(char) + int(offset_key) - 97) % 26 + 97)
        if request.method == 'POST':
            return render_template('index.html', output= "\n\n" + result + "\n\n" )

    if option == '4':
        list = [{'text' : 'first'}, {'text' : 'second'}, {'text' : 'third'}]
        tips = "This is the list of all possible decryption. Look through to find the most likely message"
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
        if request.method == 'POST':
            return render_template('index2.html', result = result, tips=tips, key = key, counter=counter)
       



if __name__ == '__main__':
    app.run(debug=True)
