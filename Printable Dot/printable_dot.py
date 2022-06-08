import keyboard
import os
from colorama import init, Fore, Back, Style
init()
'''
все тут работает отлично, надо дописать checkwin файл        
'''
size = 15 # change area's size


def draw_area(area, player):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in area:
        for j in i:
            if j == '+': print('+', end=' ')
            elif j == 'b': print(f'{Fore.BLUE}o{Fore.RESET}', end=' ')
            elif j == 'r': print(f'{Fore.RED}o{Fore.RESET}', end=' ')
            elif j == 'c+' and player == 'b': print(f'{Back.WHITE}{Fore.BLUE}+{Style.RESET_ALL}', end=' ')
            elif j == 'c+' and player == 'r': print(f'{Back.WHITE}{Fore.RED}+{Style.RESET_ALL}', end=' ')
            elif j == 'cb': print(f'{Back.WHITE}{Fore.BLUE}o{Style.RESET_ALL}', end=' ')
            elif j == 'cr': print(f'{Back.WHITE}{Fore.RED}o{Style.RESET_ALL}', end=' ')
        print()

def save(area, c):
    """
    сохраняет арену в файл saves.txt
    """
    saves_name = input('Enter save name and press enter button two times:\n')
    save_area = ''
    for i in area:
        for j in i:
            save_area += j + ','
        save_area += '\n'
    with open('saves.txt', 'w') as f:
        f.write(f'{saves_name}\n{save_area}{c[0]}{c[1]}')

def read_save():
    '''
    начинает игру с начала рисуя арену в файле saves.txt
    '''
    with open('saves.txt', 'r') as f:
        lines = f.readlines()
        print('Last save:\n')
        print(f'{Back.WHITE}{Fore.BLACK}1. {lines[0]}{Style.RESET_ALL}')
        print('Press e to load the save')
        area = [i.split(',') for i in lines[1:-1]]
        c = [int(lines[-1][0]), int(lines[-1][1])]

    return (area, c)

def cursor(c, area, move=[0, 0]):
    # you cannot exit our of arena
    if c[0] == len(area)-1 and move[0] == 1 or \
        c[0] == 0 and move[0] == -1 or \
        c[1] == len(area[0])-1 and move[1] == 1 or \
        c[1] == 0 and move[1] == -1:
        return area
    area[c[0]][c[1]] = area[c[0]][c[1]][1] # 'c+'->'+'
    c[0] += move[0]
    c[1] += move[1]
    area[c[0]][c[1]] = 'c' + area[c[0]][c[1]] # '+'->'c+'
    return area

def start_game(area, c):
    '''
    начало игры
    '''
    player = 'b'
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_area(area, player)
    while True:
        keyboard.read_key() # stops loop untill any key is pressed
        if keyboard.is_pressed('w'):
            area = cursor(c, area, [-1, 0])
            draw_area(area, player)
        elif keyboard.is_pressed('s'):
            area = cursor(c, area, [1, 0])
            draw_area(area, player)
        elif keyboard.is_pressed('a'):
            area = cursor(c, area, [0, -1])
            draw_area(area, player)
        elif keyboard.is_pressed('d'):
            area = cursor(c, area, [0, 1])
            draw_area(area, player)
        elif keyboard.is_pressed('f2'): # save
            save(area, c)
            keyboard.wait('enter')

        elif keyboard.is_pressed('enter') or keyboard.is_pressed('e'):
            if area[c[0]][c[1]] != 'c+':
                print(f'\nThis point is already ocuppied', end='')
                continue
            elif player == 'b': 
                area[c[0]][c[1]] = 'cb'
                player = 'r'
            elif player == 'r': 
                area[c[0]][c[1]] = 'cr'
                player = 'b'
            draw_area(area, player)

        elif keyboard.is_pressed('esc'):
            print('Game end')
            quit()
        elif keyboard.is_pressed('f1'): # clear the area and start game
            area = [['+' for j in range(size)] for i in range(size)]
            c = [0, 0]
            area[c[0]][c[1]] = 'c+'
            start_game(area, c)

        # keyboard.send("backspace")

def main_menu():
    area = [['+' for j in range(size)] for i in range(size)]
    c = [0, 0] # at the beginning cursor is on 0, 0 
    area[c[0]][c[1]] = 'c+'


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n     Main menu')
        if c[0] == 0 : print(f'\n       {Back.WHITE}{Fore.BLACK}Start{Style.RESET_ALL}')
        else: print(f'\n       Start')
        if c[0] == 1 : print(f'\n       {Back.WHITE}{Fore.BLACK}Saves{Style.RESET_ALL}')
        else: print(f'\n       Saves ')
        if c[0] == 2 : print(f'\n    {Back.WHITE}{Fore.BLACK}How to play{Style.RESET_ALL}')
        else: print(f'\n    How to play')

        keyboard.read_key() # stops loop untill any key is pressed
        if keyboard.is_pressed('s'):
            if c[0] < 2: c[0] += 1
        elif keyboard.is_pressed('w'):
            if c[0] > 0: c[0] += -1
        elif keyboard.is_pressed('esc'):
            quit()
            
        elif keyboard.is_pressed('enter') or keyboard.is_pressed('e') and c[0] == 0:
            start_game(area, c)
            print(area, c)
        elif keyboard.is_pressed('enter') or keyboard.is_pressed('e') and c[0] == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            read_save()
            while True:
                keyboard.read_key()
                if keyboard.is_pressed('esc'):
                    main_menu()
                elif keyboard.is_pressed('e'):
                    area, c = read_save()
                    start_game(area, c)
                    print(area, c)
        elif keyboard.is_pressed('enter') or keyboard.is_pressed('e') and c[0] == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nPress "esc" to exit.')
            print('Press "e" to enter or occupy a point.')
            print('Press "f2" to save area.')
            while True:
                keyboard.read_key()
                if keyboard.is_pressed('esc'):
                    main_menu()

if __name__ == '__main__':
    main_menu()