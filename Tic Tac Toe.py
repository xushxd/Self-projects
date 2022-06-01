from colorama import init
init()
from colorama import Fore, Back, Style
import os

def print_tictactoe(area_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{Back.WHITE}{Fore.BLACK}', end='')
    for i in [0, 3, 6]:
        print(' ------------- \n ', end='')
        for j in range(3):
            if area_list[i+j] == 'x': print(f'| {Fore.RED}x{Fore.BLACK} ', end='')
            elif area_list[i+j] == 'o': print(f'| {Fore.BLUE}o{Fore.BLACK} ', end='')
            else: print(f'| {area_list[i+j]} ', end='')
        print('| ')
    else: print(f' ------------- {Style.RESET_ALL}\n')

def wins_check(area_list):
    for i in range(0,7,3):
        if area_list[i+0] == area_list[i+1] == area_list[i+2]: return True
    for i in range(3):
        if area_list[i+0] == area_list[i+3] == area_list[i+6]: return True
    if area_list[0] == area_list[4] == area_list[8] or \
        area_list[2] == area_list[4] == area_list[6]: return True
    return False

def dead_heat(area_list):
    for i in area_list:
        if isinstance(i, int): break
    else: return True
    return False

def play():
    area_list = [i for i in range(1, 10)]
    occupied_squares = []

    print_tictactoe(area_list) 
    i = 0
    while True:
        changing_input = input('Input square\'s number (1 to 9)\n')

        # checking input strings parametrs
        if not int(changing_input) in list(range(1, 10)):
            print(f'{Back.RED}Incorrect input!{Back.RESET}')
            continue

        # checking if square is occuped
        if changing_input in occupied_squares:
            print(f'{Back.RED}This square is already occupied!{Back.RESET}')
            continue

        if i%2 == 0: value = 'x'
        else: value = 'o'
        i += 1

        area_list[int(changing_input[0])-1] = value
        occupied_squares.append(changing_input[0]) # occuping square

        print_tictactoe(area_list)
        if wins_check(area_list): 
            print(f' {Back.GREEN} {value} wins! ')
            break

        if dead_heat(area_list):
            print(f'{Back.GREEN}Dead heat!')

play()

if input(f'{Back.RESET}\n Want to play again?\n (y/n):') == 'y':
    play()
