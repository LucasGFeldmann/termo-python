import os
from verify import verify_words
from verify import green

def only_letter(word):
    if len(word) == 5 and word.isalpha():
        return word
    else:
        return None

def input_letter():
    while True:
        user_word = input("Digite sua palavra: ")
        if None != only_letter(user_word):
            return user_word.upper()
        else:
            print("[ERROR] É permitido apenas 5 letras.")

def dont_repit_word(list_words, word):
    while True:
        if word not in list_words:
            return word
        else:
            input_letter()
        