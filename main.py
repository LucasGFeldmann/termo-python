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

def index_green_letters(termo_word, user_word):
    index_exact_position_letter = []
    for index in range(5):
        if termo_word[index] == user_word[index]:
            index_exact_position_letter.append(index)
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
            positions_exist_letter_list.append(index)
            print(positions_exist_letter_list, letter)
    return positions_exist_letter_list

def index_yellow_letters(termo_word, user_word):
    green_index = index_green_letters(termo_word, user_word)
    exist_word_list = exist_letter(termo_word, user_word)
    print(exist_word_list)
    positions_exist_letter_list = positions_exist_letter(user_word, exist_word_list)
    print(positions_exist_letter_list)
    if green_index:
        for right_index in green_index:
            if right_index in positions_exist_letter_list:
                positions_exist_letter_list.remove(right_index)
    return positions_exist_letter_list

def paint_word(user_word, list_green_index, list_yellow_index):
    color_word = "| "
    for index, letter in enumerate(user_word):
        if index in list_green_index:
            color_word = color_word + f" \033[92m{letter}\033[0m |"
        elif index in list_yellow_index:
            color_word = color_word + f" \033[93m{letter}\033[0m |"
        else:
            color_word = color_word + f" {letter} |"
    return color_word


def main():
    termo_word = "CANOA"
    user_word = input_only_letter()
    list_green_index = index_green_letters(termo_word, user_word)
    list_yellow_index = index_yellow_letters(termo_word, user_word)
    print(list_green_index, list_yellow_index)
    color_word = paint_word(user_word, list_green_index, list_yellow_index)
    print(color_word)

main()