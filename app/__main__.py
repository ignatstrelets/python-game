import sys
from random import randint
from app.error import *
from app.determinator import *
from app.secret import *
from app.menu import *
from app.help import *


def validate_game_args(args):
    if len(args)==0:
        print(err_no_arguments)
        sys.exit(1)
    elif len(args)<3:
        print(err_not_enough_arguments)
        sys.exit(1)
    elif len(args)%2==0:
        print(err_even_arguments)
        sys.exit(1)
    elif len(args) != len(set(args)):
        print(err_duplication_of_arguments)
        sys.exit(1)
    else:
        return args


def prompt(game_menu, game_args, computer_move, key):
    game_menu.show_menu()
    player_choice = input("Enter your move: ")
    #"""if player_choice != "?" """and type(eval(player_choice)) != int""":
     #   prompt(game_menu, game_args, computer_move, key)
    #else:"""
    if player_choice == "0":
        return
    elif player_choice == "?":
        game_menu.help_table.print()
        prompt(game_menu, game_args, computer_move, key)
    elif player_choice.isdigit() and int(player_choice)<=len(game_args):
        player_move = int(player_choice)-1
        print("Your move: "+game_args[player_move])
        determinator = DeterminatorOfWin(game_args, player_move)
        print("Computer move: "+game_args[computer_move])
        print(determinator.determine_win(computer_move))
        print("HMAC Key: "+key.decode())
    else:
        prompt(game_menu, game_args, computer_move, key)



def main():
    game_args = validate_game_args(sys.argv[1:])
    key = KeyGenerator().key
    computer_move = randint(0, len(game_args)-1)
    hmac_digest = HMACGenerator(key, computer_move).digest
    print("HMAC: "+hmac_digest)
    help_table = HelpTable(game_args)
    game_menu = Menu(game_args, help_table)
    prompt(game_menu, game_args, computer_move, key)


if __name__ == '__main__':
    main()
