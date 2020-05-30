from random import randrange
import sys


def init():
    global board
    global maps
    global start
    global possMove #All possible range to calculate winner
    start = True
    board = [[(3*j)+i+1 for i in range(3)] for j in range(3)]
    maps = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    possMove = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    MakeListOfFreeFields(board)

    print('\nComputer initial start')
    DrawMove(board)
    
    
def DisplayBoard(brd):   
    for y in range(1, 20):
        for x in range(1, 32):
            i =int((x-6)/10)
            j =int((y-4)/6)
            
            if y % 6 == 1:
                print('+', end='') if x % 10 == 1 else print('-', end='')
            else:
                if x % 10 == 1:
                    print('|', end='')
                else:
                    print(brd[j][i], end='') if (x+4) % 10 == 0 and (y+2) % 6 == 0 else print(' ', end='')                
        print()

        
def MakeListOfFreeFields(brd):
    global FreeCell
    FreeCell = []
    for y in range(0,3):
        for x in range(0,3):
            if (brd[y][x] != 'O') and (brd[y][x] != 'X'):
                FreeCell.append([y,x])


def EnterMove(brd): #User Move
    VictoryFor(brd)
    while True:
        user_input = int(input('\nEnter your move [1-9]: '))

        if 1 <= user_input <= 9:
            target = maps[user_input - 1]
            if target in FreeCell:
                brd[target[0]][target[1]] = 'O'
                DisplayBoard(brd)
                DrawMove(brd)
            else:
                print('\nYour choose is currently occupied!')

    
def DrawMove(brd):#Computer move
    global start
    VictoryFor(brd)
    idcek = 4 if start == True else randrange(len(FreeCell))
    start = False
    target = FreeCell[idcek]
    
    print('\nComputer move: ',brd[target[0]][target[1]])
    brd[target[0]][target[1]] = 'X'

    DisplayBoard(brd)
    EnterMove(brd)

    
def VictoryFor(brd):
    MakeListOfFreeFields(brd)

    if len(FreeCell) <= 0:
        print('\nNo move anymore..', end='\n')
        replayGame()
    else:
        for vl in possMove:
            vlist = ''
            for v in vl:
                idx = maps[v-1]
                vlist += str(brd[idx[0]][idx[1]])
                if vlist == 'OOO':
                    print('\nCongratulation, You won!',end='\n')
                    replayGame()
                elif vlist == 'XXX':
                    print('\nSorry You Loose!, The computer is the winner..',end='\n')
                    replayGame()


def replayGame():
    c = input('Do you still want to continue this game? y/n : ').lower()
    if c == 'y':
        init()
    else:
        sys.exit()


# EXECUTE HERE
init()
