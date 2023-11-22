import os
from game_rules import input_letter
from verify import verify_words
from verify import green

def clear_terminal():
    # Clear terminal for Linux and Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def termo_rules(termo_word):
    list_words = []
    dont_repit = []
    contador = 0
    while contador < 5:
        user_word = input_letter()
        if user_word not in dont_repit:
            dont_repit.append(user_word)
            contador += 1
            word = verify_words(user_word,termo_word)
            list_words.append(word)
            clear_terminal()
            print("____TERMO____\n")
            for item in list_words:
                print(item)
            list_green = green(termo_word, user_word)
            if len(list_green) == 5:
                return "GANHOU"
        else:
            print("[ERROR] Não é permitido repetir palavras\n")
                
    return "PERDEU"

def dueto_rules(termo_word_1,termo_word_2):
    list_words = []
    dont_repit = []
    contador = 0
    fim_1 = ""
    fim_2 = ""
    while contador < 6:
        user_word = input_letter()
        if user_word not in dont_repit:
            dont_repit.append(user_word)
            contador += 1
            
            word_1 = verify_words(user_word,termo_word_1)
            word_2 = verify_words(user_word,termo_word_2)

            if fim_1 != "" and fim_2 != "":
                list_words.append(fim_1 + "-|-" + fim_2)
            elif fim_1 != "":
                list_words.append(fim_1 + "-|-" + word_2)
            elif fim_2 != "":
                list_words.append(word_1 + "-|-" + fim_2)
            else:
                list_words.append(word_1 + "-|-" + word_2)

            clear_terminal()
            print("____DUETO____\n")
            for item in list_words:
                print(item)
            list_green_1 = green(termo_word_1, user_word)
            list_green_2 = green(termo_word_2, user_word)
            if len(list_green_1) == 5 :
                fim_1 = "|   |   |   |   |   |"
            elif len(list_green_2) == 5 :
                fim_2 = "|   |   |   |   |   |"
            if fim_1 == "|   |   |   |   |   |" and fim_2 == "|   |   |   |   |   |":
                return "GANHOU"
        else:
            print("[ERROR] Não é permitido repetir palavras\n")
                
    return "PERDEU"

def quarteto_rules(termo_word_1,termo_word_2,termo_word_3,termo_word_4):
    list_words = []
    dont_repit = []
    contador = 0
    fim_1 = ""
    fim_2 = ""
    fim_3 = ""
    fim_4 = ""
    while contador < 8:
        user_word = input_letter()
        if user_word not in dont_repit:
            dont_repit.append(user_word)
            contador += 1
            
            word_1 = verify_words(user_word,termo_word_1)
            word_2 = verify_words(user_word,termo_word_2)
            word_3 = verify_words(user_word,termo_word_3)
            word_4 = verify_words(user_word,termo_word_4)

            if fim_1 != "" and fim_2 != "" and fim_3 != "" and fim_4 != "":
                list_words.append(fim_1 + "-|-" + fim_2 + "-|-" + fim_3 + "-|-" + fim_4)
            elif fim_2 != "" and fim_3 != "" and fim_4 != "":
                list_words.append(word_1 + "-|-" + fim_2 + "-|-" + fim_3 + "-|-" + fim_4)
            elif fim_1 != "" and fim_3 != "" and fim_4 != "":
                list_words.append(fim_1 + "-|-" + word_2 + "-|-" + fim_3 + "-|-" + fim_4)
            elif fim_1 != "" and fim_2 != "" and fim_4 != "":
                list_words.append(fim_1 + "-|-" + fim_2 + "-|-" + word_3 + "-|-" + fim_4)
            elif fim_1 != "" and fim_2 != "" and fim_3 != "":
                list_words.append(fim_1 + "-|-" + fim_2 + "-|-" + fim_3 + "-|-" + word_4)
            
            elif fim_1 != "" and fim_2 != "":
                list_words.append(fim_1 + "-|-" + fim_2 + "-|-" + word_3 + "-|-" + word_4)
            elif fim_1 != "" and fim_3 != "":
                list_words.append(fim_1 + "-|-" + word_2 + "-|-" + fim_3 + "-|-" + word_4)
            elif fim_1 != "" and fim_4 != "":
                list_words.append(fim_1 + "-|-" + word_2 + "-|-" + word_3 + "-|-" + fim_4)

            elif fim_2 != "" and fim_3 != "":
                list_words.append(word_1 + "-|-" + fim_2 + "-|-" + fim_3 + "-|-" + word_4)
            elif fim_2 != "" and fim_4 != "":
                list_words.append(word_1 + "-|-" + fim_2 + "-|-" + word_3 + "-|-" + fim_4)

            elif fim_3 != "" and fim_4 != "":
                list_words.append(word_1 + "-|-" + word_2 + "-|-" + fim_3 + "-|-" + fim_4)



            elif fim_1 != "":
                list_words.append(fim_1 + "-|-" + word_2 + "-|-" + word_3 + "-|-" + word_4)
            elif fim_2 != "":
                list_words.append(word_1 + "-|-" + fim_2 + "-|-" + word_3 + "-|-" + word_4)
            elif fim_3 != "":
                list_words.append(word_1 + "-|-" + word_2 + "-|-" + fim_3 + "-|-" + word_4)
            elif fim_4 != "":
                list_words.append(word_1 + "-|-" + word_2 + "-|-" + word_3 + "-|-" + fim_4)
            else:
                list_words.append(word_1 + "-|-" + word_2 + "-|-" + word_3 + "-|-" + word_4)

            clear_terminal()
            print("____QUARTETO____\n")
            for item in list_words:
                print(item)
            list_green_1 = green(termo_word_1, user_word)
            list_green_2 = green(termo_word_2, user_word)
            list_green_3 = green(termo_word_3, user_word)
            list_green_4 = green(termo_word_4, user_word)

            if len(list_green_1) == 5 :
                fim_1 = "|   |   |   |   |   |"
            elif len(list_green_2) == 5 :
                fim_2 = "|   |   |   |   |   |"
            elif len(list_green_3) == 5 :
                fim_3 = "|   |   |   |   |   |"
            elif len(list_green_4) == 5 :
                fim_4 = "|   |   |   |   |   |"

            if fim_1 == "|   |   |   |   |   |" and fim_2 == "|   |   |   |   |   |" and fim_3 == "|   |   |   |   |   |" and fim_4 == "|   |   |   |   |   |":
                return "GANHOU"
        else:
            print("[ERROR] Não é permitido repetir palavras\n")
                
    return "PERDEU"