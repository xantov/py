from random import randrange, randint
import time
import sys
import os
from termcolor import colored

os.system('color')

#Mainboard is refference for all List!
def init():
    global modeGame
    global mainBoard
    global freeBoard
    global scoreBoard
    global possibleLine

    modeGame = 3
    start = randrange(10)
    scoreBoard=[]
    mainBoard = []
    freeBoard = []
    possibleLine=[]

    modeGame = int(input('Welcome to Tic Tac Toe Games, choose game mode (3-20): '))
    print()
    print(
        '+---------+---------+---------+',
        '|         ' + colored('TIC TAC TOE', 'green') + '         |',
        '|          ' + colored('-G A M E-', 'red') + '          |',
        '+---------+---------+---------+', sep = '\n')
    print()

    SetBoard(modeGame)
    GenerateScoreBoard(modeGame)
    possibleLine = scoreBoard[:]
    if start % 2 == 0:
        print('\nComputer initial start')
        RenderBoard(modeGame, mainBoard)
        ComputerMove(modeGame, mainBoard)
    else:
        print('\nYou move first')
        RenderBoard(modeGame, mainBoard)  
        UserMove(modeGame, mainBoard)

def SetBoard(mod):
    global mainBoard
    for i in range(0, mod * mod):
        mainBoard.append(i + 1)

def RenderBoard(mod, board):
    i = 0
    for y in range(1, int((mod * 6)) + 2):
        for x in range(1, int((mod * 10) + 2)):
            if y % 6 == 1:
                if x % 10 == 1:
                    print(colored('+', 'cyan'), end='')
                else:
                    print(colored('-','cyan'), end='')
            else:
                if x % 10 == 1:
                    print(colored('|','cyan'), end='')
                else:
                    if (x+4) % 10 == 0 and (y+2) % 6 == 0:
                        i += 1
                        # print(i,j, end='')
                        if len(str(board[i-1])) >= 2:
                            print('', end='\x08' * (len(str(board[i-1])) - 1) )
                            if board[i-1] == 'X':
                                print(colored(board[i-1], 'red'), end='')
                            elif board[i-1] == 'O':
                                print(colored(board[i-1], 'green'), end='')
                            else:
                                print(board[i-1], end='')
                        else:
                            if board[i-1] == 'X':
                                print(colored(board[i-1], 'red'), end='')
                            elif board[i-1] == 'O':
                                print(colored(board[i-1], 'green'), end='')
                            else:
                                print(board[i-1], end='')
                    else:
                        print(' ', end='')                
        print()

def GenerateScoreBoard(mod):
    # global boardGameStatic
    #diagonal1
    val = 1
    line=[]
    for i in range(mod):
        line.append(val)
        # line.append(val)
        val += mod+1
    scoreBoard.append(line)

    #diagonal2
    line =[]
    val = mod
    for i in range(mod):
        line.append(val)
        val += mod-1
    scoreBoard.append(line)

    #row
    line =[]
    val = 0
    for y in range(mod):
        for x in range(mod):
            line.append(x+1+val)
        scoreBoard.append(line)
        line=[]
        val += mod

    #col
    line =[]
    val = 1
    for x in range(mod):
        for y in range(mod):
            line.append(x+val)
            val += mod
        scoreBoard.append(line)
        line=[]
        val = 1
 
    return scoreBoard

def ComputerMove(mod, board): #Computer Move
    id_ok = ComputerAssisted(mod, board) - 1
    board[id_ok] = 'X'

    print('Computer move..wait a minute')
    time.sleep(1.5)
    print(colored('Computer type: ' + str(id_ok + 1), 'yellow'))
    RenderBoard(mod, board)
    UpdateScore(mod, board)
    GetScore(mod, board)
    UserMove(mod, board)

def UserMove(mod, board): #User Move
    freeCell=[]
    for c in board:
        if c not in ['X','O']:
            freeCell.append(c)
            
    while True:
        try:
            usermove = int(input('\nEnter your move [1-{}]: '.format(mod * mod)))
        except ValueError:
            print('\nChoose a number between 1 and {}!'.format(mod * mod))
            try:
                usermove = int(input('\nEnter your move [1-{}]: '.format(mod * mod)))
            except ValueError:
                print()
                print('\nDasar Bandel!..Choose a number between 1 and {}!'.format(mod * mod))
                usermove = int(input('Enter your move [1-{}]: '.format(mod * mod)))

        if usermove not in freeCell:
            print('\nYour choose is currently occupied!')
            print()
        else:
            board[usermove-1] = 'O'
            break
    else:
        print('\nChoose a number between 1 and {}!'.format(mod * mod))

    UpdateScore(mod, board)
    RenderBoard(mod, board)
    GetScore(mod, board)
    ComputerMove(mod, board)

def UpdateScore(mod, board):
    global scoreBoard
    global possibleLine
    tmpSB = []
    allSB = []

    for sc in possibleLine:
        for c in sc:
            tmpSB.append(board[c-1])
        allSB.append(tmpSB)
        tmpSB=[]
    scoreBoard = allSB[:]

def GetScore(mod, board):
    global scoreBoard
    sumScore = 0
    cScore = 0
    uScore = 0

    count = 0
    for x in board:
        if x not in ['X','O']:
            count +=1

    for sc in scoreBoard:
        cScore = (sc.count('X') * 10)
        uScore = (sc.count('O') * -10)

        if cScore == 10 * mod:
            print(colored('Computer Win', 'red'))
            replayGame()
            break
        elif uScore == -10 * mod:
            print(colored('You Win!', 'green'))
            replayGame()
            break
        elif count == 0:
            print(colored('You stucked!', 'red'))
            print('Computer score: {}, Your score: {}'.format(cScore, -uScore))
            replayGame()
            break

def ComputerAssisted(mod, board):
    global scoreBoard
    sumScore = 0
    cScore = 0
    uScore = 0
    tmpSc = []
    allSc = []
    for sc in scoreBoard:
        for s in sc:
            if s == 'X':
                sumScore += 10
            elif s == 'O':
                sumScore -= 10
            else:
                sumScore += 0
        allSc.append(sumScore)
        sumScore = 0


    maxC = max(allSc)
    minU = min(allSc)

    idMax = allSc.index(maxC)
    idMin = allSc.index(minU)

    if maxC == 10 * (mod - 1) and minU > -10 * (mod - 1) or maxC == 10 * (mod - 1) and minU == -10 * (mod - 1):
        tmpMax = []
        listMax = scoreBoard[idMax]
        # print('listmax', listMax)
        for ls in listMax:
            if ls not in ['X','O']:
                tmpMax.append(ls)
        
        lmax = len(tmpMax)
        idxOut = randrange(lmax)
        vmax = tmpMax[idxOut]
        # print (vmax)
        return vmax

    elif minU == -10 * (mod - 1) and maxC < 10 * (mod - 1):
        tmpMin = []
        listMin = scoreBoard[idMin]
        for ln in listMin:
            if ln not in ['X','O']:
                tmpMin.append(ln)
        
        lmin = len(tmpMin)
        idnOut = randrange(lmin)
        vmin = tmpMin[idnOut]
        return vmin

    elif minU == -10 * (mod - 1):
        tmpMin1 = []
        listMin1 = scoreBoard[idMin]
        
        for ln1 in listMin1:
            if ln1 not in ['X','O']:
                tmpMin1.append(ln1)
        
        lmin1 = len(tmpMin1)
        idnOut1 = randrange(lmin1)
        vmin1 = tmpMin[idnOut1]
        return vmin1

    elif maxC < 10 * (mod - 1) and minU > -10 * (mod - 1):
        tmp0=[]
        for x in board:
            if x not in ['X','O']:
                tmp0.append(x)
        l0 = len(tmp0)
        id0 = randrange(l0)
        v0 = tmp0[id0]
        return v0

def replayGame():
    c = input('Do you still want to continue this game? Y/N : ')
    if c == 'Y' or c == 'y' or c == 'yes':
        init()
    else:
        sys.exit()

#EXECUTE
init()