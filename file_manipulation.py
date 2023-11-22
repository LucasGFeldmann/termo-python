from game_rules import only_letter

import random

def read_termo_words(arquivo):
    # Abre palavras termo
    try:
        list_termo_words = open(arquivo, 'r')
        termo_words = list_termo_words.readlines()
    except FileNotFoundError:
        list_termo_words = open(arquivo, 'w')
        input("Seu jogo está LIMITADO! Adicione palavras no aquivo 'words_termo.txt'")
        list_word = ["CATAR\n","PODAR\n","PARAR\n","JOGAR\n","CATAR\n","PODAR\n","PARAR\n","JOGAR\n"]
        list_termo_words.writelines(list_word)
        termo_words = list_word
        
    list_termo_words.close()
    return termo_words

def rewrite_termo_txt(termo_words):
    list_termo_words = open('words_termo.txt', 'w')
    list_termo_words.writelines(termo_words)
    list_termo_words.close()

def choose_random_word(termo_words):
    # Sorteira a palavra
    while True:
        # Tratamento de arquivo de texto vazio
        try:
            index = random.randrange(len(termo_words))
        except ValueError:
            input("Seu jogo está LIMITADO! Adicione palavras no aquivo 'words_termo.txt'")
            #list_termo_words = open('words_termo.txt', 'w')
            #list_word = ["CATAR\n","PODAR\n","PARAR\n","JOGAR\n","CATAR\n","PODAR\n","PARAR\n","JOGAR\n"]
            #return "PODAR\n"
            


        termo_word = termo_words[index].replace("\n","")
        if None != only_letter(termo_word):
            termo_words.pop(index)
            rewrite_termo_txt(termo_words)
            return termo_word.upper()
        else:
            termo_words.pop(index)
            rewrite_termo_txt(termo_words)

def append_word_to_file(word, file):
    # Adiciona a palavra para as já usadas
    words_used = open(file, 'a')
    words_used.write(word + "\n")

def reset_game():
    list_words = read_termo_words('words_termo.txt')
    list_useds = read_termo_words('words_used.txt')
    sum = list_words + list_useds
    open('words_used.txt','w')
    rewrite_termo_txt(sum)

def start_game():
    termo_words = read_termo_words('words_termo.txt')
    termo_word = choose_random_word(termo_words)
    return termo_word

def win_game(termo_word):
    if type(termo_word) == tuple:
        for word in termo_word:
            append_word_to_file(word, 'words_used.txt')
    else:
        append_word_to_file(termo_word, 'words_used.txt')

def lose_game(termo_word):
    if type(termo_word) == tuple:
        for word in termo_word:
            append_word_to_file(word, 'words_termo.txt')
    else:
        append_word_to_file(termo_word, 'words_termo.txt')