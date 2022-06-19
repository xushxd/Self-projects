import time
import keyboard
import os
from colorama import *
init()

text = ''' The walrus is a large flippered marine mammal with a discontinuous distribution about the North Pole in the Arctic Ocean and subarctic seas of the Northern Hemisphere. The walrus is the only living species in the family Odobenidae and genus Odobenus.  '''
text = text.strip()

cursor = 0
mistakes = 0
have_time=False

def print_typer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text[:cursor], end='')
    print(f'{Back.WHITE}{Fore.BLACK}{text[cursor]}{Style.RESET_ALL}', end='')
    print(text[cursor+1:])
    print()
    if have_time: print('speed =', int(cursor / (time.time() - start_time) * 60))
    else: print('speed = 0')

print_typer()

while True:
    if keyboard.is_pressed(text[cursor]):
        if cursor == 0:
            start_time = time.time()
            have_time = True

        if cursor != len(text)-1:
            cursor += 1
            print_typer()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(text)
            print(f'{Back.GREEN}Your speed is {int(len(text) / (time.time() - start_time) * 60)}')
            quit()