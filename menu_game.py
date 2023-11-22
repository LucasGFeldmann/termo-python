from file_manipulation import start_game
from file_manipulation import lose_game
from file_manipulation import win_game
from file_manipulation import reset_game
from game_modes import termo_rules
from game_modes import dueto_rules
from game_modes import quarteto_rules
from game_modes import clear_terminal

def main():
    opt = ""
    while opt != "5":
        clear_terminal()
        print("____TERMO GAME____\n")
        print("1 - Termo")
        print("2 - Dueto")
        print("3 - Quarteto")
        print("4 - RESET")
        print("5 - EXIT\n")
        opt = input("Digite a Opção: ")

        if opt == "1":
            termo_word = start_game()
            clear_terminal()
            print("____TERMO____\n")
            
            result = termo_rules(termo_word)
            if result == "PERDEU":
                lose_game((termo_word))
            elif result == "GANHOU":
                win_game((termo_word))
            print(result)
            input("\nEnter para voltar para o MENU")
        elif opt == "2":
            termo_word_1 = start_game()
            termo_word_2 = start_game()
            clear_terminal()
            print("____DUETO____\n")
            print(termo_word_1,termo_word_2)
            result = dueto_rules(termo_word_1,termo_word_2)
            if result == "PERDEU":
                lose_game((termo_word_1,termo_word_2))
            elif result == "GANHOU":
                win_game((termo_word_1,termo_word_2))
            print(result)
            input("\nEnter para voltar para o MENU")
        elif opt == "3":
            termo_word_1 = start_game()
            termo_word_2 = start_game()
            termo_word_3 = start_game()
            termo_word_4 = start_game()
            clear_terminal()
            print("____QUARTETO____\n")
            print(termo_word_1,termo_word_2,termo_word_3,termo_word_4)
            result = quarteto_rules(termo_word_1,termo_word_2,termo_word_3,termo_word_4)
            if result == "PERDEU":
                lose_game((termo_word_1,termo_word_2,termo_word_3,termo_word_4))
            elif result == "GANHOU":
                win_game((termo_word_1,termo_word_2,termo_word_3,termo_word_4))
            print(result)
            input("\nEnter para voltar para o MENU")
        elif opt == "4":
            reset_game()
        else:
            print("[ERROR] Opção Invalida!")

main()