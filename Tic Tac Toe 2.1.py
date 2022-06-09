'''
How to play:
use "wsda" for movement, 
"e" for selecting, 
"f1" for start over,
"f2" for change style
"esc" for exit.
'''
import keyboard
from colorama import init
init()
from colorama import Fore, Back, Style
import os

def print_tictactoe(area_list):
    if style == 1: frames = ('╔═══╦═══╦═══╗', '╠═══╬═══╬═══╣', '╚═══╩═══╩═══╝', '║')
    else: frames = ('┌───┬───┬───┐', '├───┼───┼───┤', '└───┴───┴───┘', '│')

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{Back.LIGHTWHITE_EX}{Fore.BLACK} {frames[0]} \n ', end='')
    for i in [0, 3, 6]:
        if i != 0: print(f' {frames[1]} \n ', end='')
        for j in range(3):
            if area_list[i+j] == 'x' and c != i+j: print(f'{frames[3]} {Fore.RED}x{Fore.BLACK} ', end='')
            elif area_list[i+j] == 'o' and c != i+j: print(f'{frames[3]} {Fore.BLUE}o{Fore.BLACK} ', end='')
            elif area_list[i+j].isdigit() and c != i+j: print(f'{frames[3]}   ', end='')
            elif area_list[i+j] == 'x': print(f'{frames[3]} {Back.WHITE}{Fore.RED}x{Fore.BLACK}{Back.LIGHTWHITE_EX} ', end='')
            elif area_list[i+j] == 'o': print(f'{frames[3]} {Back.WHITE}{Fore.BLUE}o{Fore.BLACK}{Back.LIGHTWHITE_EX} ', end='')
            elif area_list[i+j].isdigit() and player == 'x': print(f'{frames[3]} {Back.WHITE}{Fore.BLACK}x{Fore.BLACK}{Back.LIGHTWHITE_EX} ', end='')
            elif area_list[i+j].isdigit() and player == 'o': print(f'{frames[3]} {Back.WHITE}{Fore.BLACK}o{Fore.BLACK}{Back.LIGHTWHITE_EX} ', end='')
        print(f'{frames[3]} ')
    else: print(f' {frames[2]} {Style.RESET_ALL}\n')

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
        if i.isdigit(): return False
    return True

def play_again():
    print('Press "e" to play again or "esc" to exit')
    while True:
        keyboard.read_key()
        if keyboard.is_pressed('e') or keyboard.is_pressed('enter'):
            return play()
        elif keyboard.is_pressed('esc'): quit()

def play():
    area_list = [str(i) for i in range(9)]
    cycle_counter = 0
    global c, player, style
    c = 0
    player = 'x'
    style = 1

    while True:
        print_tictactoe(area_list)

        if wins_check(area_list):
            print(f' {Back.GREEN} {player} wins!{Back.RESET}\n')
            play_again()
        elif dead_heat(area_list):
            print(f' {Back.GREEN} Dead heat! {Back.RESET}')
            play_again()

        if cycle_counter%2 == 0: player = 'x'
        else: player = 'o'

        keyboard.read_key() # stops loop untill any key is pressed

        if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
            if c > 2:
                c -= 3
        elif keyboard.is_pressed('down') or keyboard.is_pressed('s'):
            if c < 6:
                c += 3
        elif keyboard.is_pressed('left') or keyboard.is_pressed('a'):
            if c not in (0, 3, 6):
                c -= 1
        elif keyboard.is_pressed('right') or keyboard.is_pressed('d'):
            if c not in (2, 5, 8):
                c += 1
        elif keyboard.is_pressed('enter') or keyboard.is_pressed('e'):
            if area_list[c].isdigit():
                area_list[c] = player
                cycle_counter += 1
        elif keyboard.is_pressed('f1'): # clear the area and start the game over
            play()
        elif keyboard.is_pressed('f2'):
            if style == 1: style += 1
            else: style = 1
        elif keyboard.is_pressed('esc'):
            print('Game over')
            break

if __name__ == '__main__':
    play()
