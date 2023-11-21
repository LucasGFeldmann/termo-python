def input_only_letter():
    while True:
        user_word = input("Digite sua palavra: ")
        try:
            if len(user_word) == 5 and user_word.isalpha():
                return user_word.upper()
            else:
                raise TypeError("[ERROR] É permitido apenas 5 letras.")
        except TypeError:
            print("[ERROR] É permitido apenas 5 letras.")

def letter_counter(word):
    list_letter_2x = []
    list_letter_3x = []
    list_letter_1x = []
    list_letter_4x = []
    list_letter_5x = []

    for letter in word:
        if letter in list_letter_4x:
            list_letter_5x.append(letter)
        elif letter in list_letter_3x:
            list_letter_4x.append(letter)
        elif letter in list_letter_2x:
            list_letter_3x.append(letter)
        elif letter in list_letter_1x:
            list_letter_2x.append(letter)
        else:
            list_letter_1x.append(letter)
        
    def minus(list_letter_1x,list_letter_2x):
        list_copy = list_letter_1x.copy()
        for letter in list_letter_1x:
            if letter in list_letter_2x:
                list_copy.remove(letter)
        return list_copy
        
    list_letter_1x = minus(list_letter_1x,list_letter_2x)
    list_letter_2x = minus(list_letter_2x,list_letter_3x)
    list_letter_3x = minus(list_letter_3x,list_letter_4x)
    list_letter_4x = minus(list_letter_4x,list_letter_5x)

    print(list_letter_1x)
    print(list_letter_2x)
    print(list_letter_3x)
    print(list_letter_4x)
    print(list_letter_5x)

    return list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x

def index_green_letters(termo_word, user_word):
    index_exact_position_letter = []
    for index in range(5):
        if termo_word[index] == user_word[index]:
            index_exact_position_letter.append((index, termo_word[index]))
    return index_exact_position_letter

def exist_letter(termo_word, user_word):
    exist_word_list = []
    for termo_letter in termo_word:
        for user_letter in user_word:
            if termo_letter == user_letter and termo_letter not in exist_word_list:
                exist_word_list.append(termo_letter)
    return exist_word_list

def positions_exist_letter(user_word, exist_word_list):
    '''( pavra do termo, lista de palavras que existem em relação a palavra do usuario)'''
    positions_exist_letter_list = []
    for index, letter in enumerate(user_word):
        if letter in exist_word_list:
            positions_exist_letter_list.append((index, letter))
    return positions_exist_letter_list

def second_position(list_tupla):
    seconds = []
    for item in list_tupla:
        seconds.append(item[1])
    return seconds


def utilities(list_1):
    list_2 = []
    for x in list_1:
        list_2.append(x[1])
    return list_2

def remove_yellow(letter_list, tupla_list):
    list_copy = list(tupla_list)
    for tupla in tupla_list:
        if tupla[1] not in letter_list:
            list_copy.remove(tupla)
    print("AAAA",list_copy)
    return list_copy

def sequencia(user_word, positions_exist_letter_list, list_green_index, list_repit_letters,):
    letters_yellow = utilities(positions_exist_letter_list)
    copy_list = letters_yellow.copy()
    for index, letter in enumerate(user_word):
        if (index,letter) in list_green_index and letter in letters_yellow and letter in list_repit_letters:
            try:
                letters_yellow.remove(letter)
            except:
                pass
    
    copy_list = remove_yellow(letters_yellow, positions_exist_letter_list)

    return copy_list


def teste(user_word, positions_exist_letter_list, list_green_index, list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x):

    copy_list = sequencia(user_word, positions_exist_letter_list, list_green_index, list_letter_1x,)

    return copy_list

def sub_yellow(user_word,list_green_index,positions_exist_letter_list):
    copy_list = list(positions_exist_letter_list)
    for index, letter in enumerate(user_word):
        if (index,letter) in list_green_index and (index,letter) in positions_exist_letter_list:
            copy_list.remove((index,letter))
            
    return copy_list

def index_yellow_letters(termo_word, user_word, list_green_index,list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x):
    exist_word_list = exist_letter(termo_word, user_word)
    positions_exist_letter_list = positions_exist_letter(user_word, exist_word_list)
    positions_exist_letter_list = sub_yellow(user_word,list_green_index,positions_exist_letter_list)
    print(list_green_index,positions_exist_letter_list)
    positions_exist_letter_list = teste(user_word, positions_exist_letter_list, list_green_index, list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x)

    
    return positions_exist_letter_list

def paint_word(user_word, list_green_index, list_yellow_index):
    color_word = "| "
    for index, letter in enumerate(user_word):
        if (index, letter) in list_green_index:
            color_word = color_word + f" \033[92m{letter}\033[0m |"
        elif (index, letter) in list_yellow_index:
            color_word = color_word + f" \033[93m{letter}\033[0m |"
        else:
            color_word = color_word + f" {letter} |"
    return color_word

def main():
    termo_word = "CANOA"
    list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x = letter_counter(termo_word)

    user_word = input_only_letter()

    list_green_index = index_green_letters(termo_word, user_word)

    list_yellow_index = index_yellow_letters(termo_word, user_word, list_green_index, list_letter_1x,list_letter_2x,list_letter_3x,list_letter_4x, list_letter_5x)



    #print(list_green_index, list_yellow_index)
    color_word = paint_word(user_word, list_green_index, list_yellow_index)
    print(color_word)

main()