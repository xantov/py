from random import randrange
import time
import sys
import os
from termcolor import colored

os.system('color')

class TTT:
    def __init__(self):
        self.__mod = int(input('Welcome to Tic Tac Toe Games, choose game mode (3-20): '))
        self.__mod = 3 if self.__mod == 0 or self.__mod == '' else self.__mod
        self.__rule = int(input('Choose game rule: '))
        self.__rule = self.__mod if int(self.__rule) <= 0 or int(self.__rule) > self.__mod else self.__rule
        self.__mainBoard =[self.i + 1 for self.i in range(self.__mod * self.__mod)]
        # Score board
        self.__lineSore = [[(self.__mod * self.j) + self.i + 1 for self.i in range(self.__mod)] for self.j in range(self.__mod)]
        self.__rowScore = [[(self.j + 1) + (self.__mod * self.i) for self.i in range(self.__mod)] for self.j in range(self.__mod)]
        self.__diag1Score = [(self.__mod * self.i) + (self.i + 1) for self.i in range(self.__mod)]
        self.__diag1Score_left = [[(self.__mod * self.i) + (self.i + 1) + self.n for self.i in range(self.__mod-self.n)] for self.n in range(1,self.__mod-self.__rule+1)]
        self.__diag1Score_right = [[(self.__mod * self.i) + (self.i + (self.__mod * self.n)) +1 for self.i in range(self.__mod-self.n)] for self.n in range(1,self.__mod-self.__rule+1)]
        self.__diag2Score = [(self.__mod * self.i) + (self.__mod - self.i) for self.i in range(self.__mod)]
        self.__diag2Score_left = [[(self.__mod * self.i) + (self.__mod - self.i) - self.n for self.i in range(self.__mod-self.n)] for self.n in range(1,self.__mod-self.__rule+1)]
        self.__diag2Score_right = [[(self.__mod * self.i) + (self.__mod - self.i)+(self.__mod * self.n) for self.i in range(self.__mod-self.n)] for self.n in range(1,self.__mod-self.__rule+1)]
        self.__scoreBoard = self.__lineSore + self.__rowScore+self.__diag1Score_left+self.__diag1Score_right+self.__diag2Score_left+self.__diag2Score_right
        self.__scoreBoard.append(self.__diag1Score)
        self.__scoreBoard.append(self.__diag2Score)
        # End Score board
        self.__start = randrange(10)
        self.__freeBoard =[]
        self.__freeCell =[]
        self.__possibleLine =[]
        self.__isComputer = True

        print()
        print('+' + '-' * ((self.__mod * 10) - 1) + '+',
              '|' + ' ' * ((self.__mod * 10 - 11) // 2) + 'TIC TAC TOE' + ' ' * ((self.__mod * 10 - 11) // 2) + '|',
              '|' + ' ' * ((self.__mod * 10 - 7) // 2) + 'G A M E' + ' ' * ((self.__mod * 10 - 7) // 2) + '|',
              '+' + '-' * ((self.__mod * 10) - 1) + '+', sep='\n')
        print('MODE: '+str(self.__mod)+'x'+str(self.__mod))
        print('RULE: '+str(self.__rule)+' ['+'X'* self.__rule +','+'O'* self.__rule + ']')
        print()

        self.EmptyCell()
        self.RenderBoard()

        self.__possibleLine = self.__scoreBoard[:]

        if self.__start % 2 == 0:
            print('\nComputer initial start')
            self.ComputerMove()
        else:
            print('\nYou move first')
            self.__isComputer = False
            self.UserMove()


    def RenderBoard(self):
        self.i = 0
        for self.y in range(1, int((self.__mod * 6)) + 2):
            for self.x in range(1, int((self.__mod * 10) + 2)):
                if self.y % 6 == 1:
                    print(colored('+', 'cyan'), end='') if self.x % 10 == 1 else print(colored('-', 'cyan'), end='')
                else:
                    if self.x % 10 == 1:
                        print(colored('|', 'cyan'), end='')
                    else:
                        if (self.x + 4) % 10 == 0 and (self.y + 2) % 6 == 0:
                            self.i += 1
                            if len(str(self.__mainBoard[self.i - 1])) >= 2:
                                print('', end='\x08' * (len(str(self.__mainBoard[self.i - 1])) - 1))
                                if self.__mainBoard[self.i - 1] == 'X':
                                    print(colored(self.__mainBoard[self.i - 1], 'red'), end='')
                                elif self.__mainBoard[self.i - 1] == 'O':
                                    print(colored(self.__mainBoard[self.i - 1], 'green'), end='')
                                else:
                                    print(self.__mainBoard[self.i - 1], end='')
                            else:
                                if self.__mainBoard[self.i - 1] == 'X':
                                    print(colored(self.__mainBoard[self.i - 1], 'red'), end='')
                                elif self.__mainBoard[self.i - 1] == 'O':
                                    print(colored(self.__mainBoard[self.i - 1], 'green'), end='')
                                else:
                                    print(self.__mainBoard[self.i - 1], end='')
                        else:
                            print(' ', end='')
            print()


    def EmptyCell(self):
        self.__freeCell=[]
        for self.c in self.__mainBoard:
            if self.c not in ['X', 'O']:
                self.__freeCell.append(self.c)


    def ApplyMove(self):
        self.EmptyCell()
        self.RenderBoard()
        self.UpdateScore()
        self.GetScore()
        if self.__isComputer:
            self.__isComputer = False
            self.UserMove()
        else:
            self.__isComputer = True
            self.ComputerMove()


    def UserInput(self):
        self.usermove = int(input('\nEnter your move [1-{}]: '.format(self.__mod * self.__mod)))


    def UserError(self):
        print('\nChoose a number between 1 and {}!'.format(self.__mod * self.__mod))


    def UserMove(self):  # User Move
        while True:
            try:
                self.UserInput()
            except ValueError:
                self.UserError()
                try:
                    self.UserInput()
                except ValueError:
                    self.UserError()
                    self.UserInput()
            if self.usermove not in self.__freeCell:
                print('\nYour choose is currently occupied!')
                print()
            else:
                self.__mainBoard[self.usermove - 1] = 'O'
                break
        else:
            self.UserError()

        self.ApplyMove()


    def ComputerMove(self):  # Computer Move
        self.id_ok = self.ComputerAssisted() -1
        self.__mainBoard[self.id_ok] = 'X'

        print('Computer move..wait a minute')
        time.sleep(1.5)
        print(colored('Computer type: ' + str(self.id_ok + 1), 'yellow'))
        self.ApplyMove()


    def UpdateScore(self):
        self.allSB = []
        for self.sc in self.__possibleLine:
            self.tmpSB = []
            for self.c in self.sc:
                self.tmpSB.append(self.__mainBoard[self.c - 1])
            self.allSB.append(self.tmpSB)
        self.__scoreBoard = self.allSB[:]


    def GetScore(self):
        self.countFree = sum([1 for self.x in self.__mainBoard if self.x not in ['X', 'O']])

        for self.sc in self.__scoreBoard:
            for self.i in range(self.__rule):
                if self.sc[self.i:self.i + self.__rule] == ['X' for self.z in range(self.__rule)]:
                    print(colored('Computer Won', 'red'))
                    self.ReplayGame()
                    break
                elif self.sc[self.i:self.i + self.__rule] ==  ['O' for self.z in range(self.__rule)]:
                    print(colored('You Won!', 'green'))
                    self.ReplayGame()
                    break
                elif self.countFree == 0:
                    print(colored('You all stucked!', 'red'))
                    # print('Computer score: {}, Your score: {}'.format(self.cScore, -self.uScore))
                    self.ReplayGame()
                    break


    def ComputerAssisted(self):
        self.tmpTarget = []
        self.target = 0
        self.tg = 0
        self.MaxC = False
        self.MaxU = False
        for self.sc in self.__scoreBoard:
            for self.i in range(self.__rule):
                if self.sc[self.i:self.i + self.__rule].count('X') >= self.__rule-1 and self.sc[self.i:self.i + self.__rule].count('O') == 0:
                    for t in self.sc[self.i:self.i + self.__rule]:
                        if t not in ['X', 'O']:
                            self.target = int(t)
                            break
                elif self.sc[self.i:self.i + self.__rule].count('O') >= self.__rule-1 and self.sc[self.i:self.i + self.__rule].count('X') == 0:
                    for t in self.sc[self.i:self.i + self.__rule]:
                        if t not in ['X', 'O']:
                            self.target = int(t)
                            break
                elif self.target == 0 and 0 <= self.sc[self.i:self.i + self.__rule].count('X') < self.__rule-2 and self.sc[self.i:self.i + self.__rule].count('O') == 0:
                    for t in self.sc[self.i:self.i + self.__rule]:
                        if t not in ['X','O']:
                            self.tmpTarget.append(int(t))
                            self.tg = randrange(0, len(self.tmpTarget))
                            self.target = self.tmpTarget[self.tg]
                        break

        if self.target == 0:
            self.tg = randrange(0, len(self.__freeCell))
            self.target = self.__freeCell[self.tg]
        # print('target',self.target)
        return self.target


    def ReplayGame(self):
        self.c = input('Do you still want to continue this game? Y/N : ').lower()
        if self.c in ['y', 'yes', 'ya', 'ok']:
            self.__init__()
        else:
            sys.exit()
