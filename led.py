#Create 7x5 LED Matrix Numbers
import os
from termcolor import colored
os.system('color')

num     = str(input('Input your numbers (0-9): '))
number  = []
for n in num:
    if n in ['0','1','2','3','4','5','6','7','8','9']:
        number.append(n)
        
on_led  = str(input('LED style (@,#,X,O) [Optional]: '))
space   = str(input('Space between LED (0-5) [Optional]: '))
col     = str(input('Choose LED color (red, green, blue, yellow) [Optional]: '))

on_led  = on_led if on_led != '' else 'O'
off_led = ' '

space   = (int(space) * ' ') if space != '' else ' '
color   = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white']

col     = col if col in color else 'red'

led     = [
        [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],#0
        [[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0]],#1
        [[0,1,1,1,0],[1,0,0,0,1],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1]],#2
        [[1,1,1,1,1],[0,0,0,1,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,0]],#3
        [[0,0,0,1,0],[0,0,1,1,0],[0,1,0,1,0],[1,0,0,1,0],[1,1,1,1,1],[0,0,0,1,0],[0,0,0,1,0]],#4
        [[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,0]],#5
        [[0,0,1,1,0],[0,1,0,0,0],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],#6
        [[1,1,1,1,1],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]],#7
        [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],#8
        [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,1],[0,0,0,0,1],[0,0,0,1,0],[0,1,1,0,0]] #9
        ]

print()
for y in range(7):
    for i in number:
        for x in range(5):
            ld = colored(on_led, col) if led[int(i)][y][x] == 1 else colored(off_led, 'grey')
            print(ld, end='')
        print('', end=space)
    print()

print()
