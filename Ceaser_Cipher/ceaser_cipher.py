alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def ceaser(text, shift , direction):
        if (direction == "encode"):
            text_list = []
            text_list = list(text)
            shift_num = 0
            cipher_text = ""
            for letter in text_list:
                if letter in alphabet:
                    shift_num = alphabet.index(letter) + shift
                    cipher_text += alphabet[shift_num]
                else:
                    cipher_text += letter 
            print(cipher_text)  
        elif (direction == "decode"):
            cipherd_text = ""
            decrpyt_list = list(text)
            for letter in decrpyt_list:
                if letter in alphabet:
                    decrpyt_position = alphabet.index(letter) - shift
                    cipherd_text += alphabet[decrpyt_position]
                else:
                    cipherd_text += letter 
            print(cipherd_text)
        else:
            print("Give me the proper value")
    
    ceaser(text , shift , direction)

    restart = input("Type yes if you want to go again, Otherwise No: ")
    if restart == "no":
        should_continue = False
        print("Good Bye")

    



"""

def encrypt(plain_text, shift):
    text_list = []
    text_list = list(plain_text)
    shift_num = 0
    cipher_text = ""
    for letter in text_list:
        shift_num = alphabet.index(letter) + shift
        cipher_text += alphabet[shift_num]
    print(cipher_text)


def decrypt(decrpyt_text, decrpyt_shift):
    cipherd_text = ""
    decrpyt_list = list(decrpyt_text)
    for letter in decrpyt_list:
        decrpyt_position = alphabet.index(letter) - decrpyt_shift
        cipherd_text += alphabet[decrpyt_position]
    print(cipherd_text)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Give me the following words")

    """