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
            index_exact_position_letter.append((index, termo_word[index]))
    return index_exact_position_letter

def yellow(termo_word,greens):
    termo_list = list(termo_word)
    contador = len(greens)
    while contador > 0:
        contador -= 1
        termo_list.pop(greens[contador][0])
    return termo_list

def paint_word(user_word, greens, yellows):
    color_word = "| "
    for index, letter in enumerate(user_word):
        if (index, letter) in greens:
            color_word = color_word + f" \033[92m{letter}\033[0m |"
        elif letter in yellows:
            color_word = color_word + f" \033[93m{letter}\033[0m |"
            yellows.remove(letter)
        else:
            color_word = color_word + f" {letter} |"
    return color_word

def main():
    termo_word = "CANOA"
    user_word = input_only_letter()
    greens = index_green_letters(termo_word, user_word)
    yellows = yellow(termo_word, greens)
    color_word = paint_word(user_word, greens, yellows)
    print(color_word)
main()