def green(termo_word, user_word):
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
    color_word = "|"
    for index, letter in enumerate(user_word):
        if (index, letter) in greens:
            color_word = color_word + f" \033[92m{letter.upper()}\033[0m |"
        elif letter in yellows:
            color_word = color_word + f" \033[93m{letter.upper()}\033[0m |"
            yellows.remove(letter)
        else:
            color_word = color_word + f" {letter.upper()} |"
    return color_word

def verify_words(user_word, termo_word):
    '''Entrada: palavra a ser verificada com sua referencia.
        Retorna a palavra verificada com cores.'''
    greens = green(termo_word, user_word)
    yellows = yellow(termo_word, greens)
    color_word = paint_word(user_word, greens, yellows)
    return color_word
