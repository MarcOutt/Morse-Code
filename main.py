alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "- ",
    "u": "..- ",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def text_to_morse(text):
    text_code = ""
    for letter in text.lower():
        if letter in alphabet:
            text_code += alphabet[letter] + " "
    print(text_code)


def morse_to_text(code):
    code_list = code.split()
    text = ""
    for letter in code_list:
        for key, value in alphabet.items():
            if letter == value:
                text += key
    print(text)


print("""       _
      //\\
     | \\/
     ||~                                             _     _
     ||_                                            [ L___I ]
     | /\\                                          |   ...   |
    ,@\\/    ,@@@,            ,@@@@@,              |   :::   |
    @,    ,@@"   "@@@,     ,@@"     "@@@,    ,@@@@"|   '''   |
jgs "@@@@@"          "@@@@@"            "@@@@"     '========='
""")

while True:
    try:
        answer = input("1 - Translate text to Morse code\n"
                       "2 - Translate Morse code to text\n"
                       "3 - Exit\n"
                       "Choose an option (1, 2, or 3): ")
        if answer == '1':
            user_input = input("Please write your text to translate it into Morse code: ")
            text_to_morse(user_input)
        elif answer == '2':
            user_input = input("Please write your Morse code to translate it into text: ")
            morse_to_text(user_input)
        elif answer == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    except Exception as e:
        print(f"An error occurred: {e}")
