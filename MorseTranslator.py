from pydub import AudioSegment # able to use after 'pip install pydub'

def morseCodeTranslator():
    morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
'.': '-....-', ',': '.-.-.-', '(': '-.--.', ')': '-.--.-', '?': '..--..', '/': '-..-.'}
    
    def encrypt(text):
        text = text.replace('\n', ' ').replace('\t', ' ')
        spaceSelector = int(input("Do you want to mark 'space' with '/' or ' '?(1. '/', 2. ' ')(Input option number): "))
        if spaceSelector == 1:
            encryptData = ""
            for letter in text:
                if letter != ' ':
                    encryptData += morseCode[letter] + ' '
                else:
                    encryptData += '/ '
        elif spaceSelector == 2:
            encryptData = ""
            for letter in text:
                if letter != ' ':
                    encryptData += morseCode[letter] + ' '
                else:
                    encryptData += ' '
        else:
            raise Exception("Wrong input")
        print(encryptData)
    
    def decrypt(morse):
        morse = morse.replace('/', ' ')
        morse += ' '
        reverseMorseCode = {v:k for k, v in morseCode.items()}
        decryptData = ""
        morseWord = ""
        spaceCounter = 0
        for sign in morse:
            if sign != ' ':
                morseWord += sign
                spaceCounter = 0
            else:
                spaceCounter += 1
                if spaceCounter == 1:
                    if morseWord:
                        decryptData += reverseMorseCode[morseWord]
                        morseWord = ""
                    else:
                        continue
                else:
                    spaceCounter = 0
                    decryptData += ' '
        print(decryptData)

    # Encrypt / Decrypt 입력 (Input Encrypt / Decrypt)
    cryptOption = int(input("Select function to use (1. Encrypt, 2. Decrypt)(Input option number): "))

    # Encrypt 데이터 입력 (Input data to Encrypt)
    if cryptOption == 1:
        inputOptionNL = int(input("Select way to get data (1. File, 2. Manual input)(Input option number): " ))
        if inputOptionNL == 1:
            fileName = input("Input file address: ")
            fileName = fileName.replace('\\', '/').replace('"', '')
            fileNL = open(fileName, 'r')
            dataNL = fileNL.read()
            dataNL = dataNL.upper()
            fileNL.close()
        elif inputOptionNL == 2:
            dataNL = input("Input text to encrypt: ")
            dataNL = dataNL.upper()
        else:
            raise Exception("Wrong input")
        encrypt(dataNL)

    # Decrpyt 데이터 입력 (Input morse code to Decrpyt)
    elif cryptOption == 2:
        inputOptionMorse = int(input("Select way to get data (1. Audio file, 2. Text file, 3. Manual input)(Input option number): "))
        if inputOptionMorse == 1:
            print("This function is not available yet.")
        elif inputOptionMorse == 2:
            fileName = input("Input file address: ")
            fileName = fileName.replace('\\', '/').replace('"', '')
            fileMorse = open(fileName, 'r')
            dataMorse = fileMorse.read()
            fileMorse.close()
        elif inputOptionMorse == 3:
            dataMorse = input("Input morse code to decrypt: ")
        else:
            raise Exception("Wrong input")
        decrypt(dataMorse)
    
    else:
        raise Exception("Wrong Input")

morseCodeTranslator()