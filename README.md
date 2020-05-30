# py - python simple projects
Simple project for python learning

The following are sample input and output of the projects:

**TIC TAC TOE**
```
Welcome to Tic Tac Toe Games, choose game mode (3-20): 5

+-------------------------------------------------+
|                   TIC TAC TOE                   |
|                     G A M E                     |
+-------------------------------------------------+

Computer initial start
Computer move..wait a minute
Computer type: 17
+---------+---------+---------+---------+---------+
|         |         |         |         |         |
|         |         |         |         |         |
|    1    |    2    |    3    |    4    |    5    |
|         |         |         |         |         |
|         |         |         |         |         |
+---------+---------+---------+---------+---------+
|         |         |         |         |         |
|         |         |         |         |         |
|    6    |    7    |    8    |    9    |   10    |
|         |         |         |         |         |
|         |         |         |         |         |
+---------+---------+---------+---------+---------+
|         |         |         |         |         |
|         |         |         |         |         |
|   11    |   12    |   13    |   14    |   15    |
|         |         |         |         |         |
|         |         |         |         |         |
+---------+---------+---------+---------+---------+
|         |         |         |         |         |
|         |         |         |         |         |
|   16    |    X    |   18    |   19    |   20    |
|         |         |         |         |         |
|         |         |         |         |         |
+---------+---------+---------+---------+---------+
|         |         |         |         |         |
|         |         |         |         |         |
|   21    |   22    |   23    |   24    |   25    |
|         |         |         |         |         |
|         |         |         |         |         |
+---------+---------+---------+---------+---------+

Enter your move [1-25]:
```

**IMAGE TO TEXT**
```
Masukkan file gambar (jpg/png): pyt.png
Masukkan tinggi output (Rekomendasi max 70): 50
Adjustmen kontras (10-90): 35
Tambahkan spasi pada output? ketik Ya/ Tidak : n

Apabila output terlalu gelap, naikkan nilai kontras!

····························································································
····························································································
····························································································
·········································t(input('W·········································
··································erateScoreBoard(modeGame··································
······························start')RenderBoard(modeGame,main······························
···························vefirst')RenderBoard(modeGame,mainBoar···························
························almainBoardforiinrange(0,mod*mod):mainBoard.························
······················range(1,int((mod*6))+2):forxinrange(1,int((mod*1······················
····················','cyan'),end='')else:print(colored('-','cyan'),end=····················
··················yan'),end='')else:if(x+4)%10==0and(y+2)%6==0:i+=1#print(··················
·················2:print('',end='\x08'*(len(str(board[i-1]))-1))ifboard[i-1·················
···············'red'),end='')elifboard[i-1]=='O':print(colored(board[i-1],'gr···············
··············[i-1],end='')else:ifb···················t(colored(board[i-1],'re··············
·············'O':print(colored(b························')else:print(board[i-1]·············
············='')print()defGener···························oardGameStatic#diagonal···········
···········ge(mod):line.append·····#li·····················d+1scoreBoard.append(li··········
··········val=modforiinrange(m····line.····················1scoreBoard.append(line)·········
·········ryinrange(mod):forxin····e(mod····················l)scoreBoard.append(line·········
········colline=[]val=1forxinr·····mod·····················ne.append(x+val)val+=mods········
·······d(line)line=[]val=1retu·····························od,board):#ComputerMoveid_·······
·······isted(mod,board)-1board·····························e..waitaminute')time.sleep(······
······lored('Computertype:'+str····························ard(mod,board)UpdateScore(m······
·····tScore(mod,board)UserMove(mod,board)defU··············ard):#UserMovefreeCell=[]for·····
·····fcnotin['X','O']······································ove·······put('\nEnteryourmo·····
····'.format(mod*mo········································ber·········nd{}!'.format(mod····
····y:usermove=in··········································d*m···········ValueError:prin····
····('\nDasarBan···········································od*···········ve=int(input('En···
···rmove[1-{}]:'···········································rin············oseiscurrentlyo···
···d!')print()e············································Cho············tween1and{}!'.f···
···mod*mod))Upd············································Sc··············ComputerMove(m···
···rd)defUpdate···········································ibl··············llSB=[]forscinp··
···leLine:forci··········································mpSB··············Board=allSB[:]d··
··tScore(mod,bo·······································uScore···············board:ifxnotin[··
··'O']:count+=1··················cScore=(sc.count('X')*10)·················'O')*-10)ifcSco··
··10*mod:print(················rWin','red'))replayGame(····················0*mod:print(col··
··('YouWin!','g···············me()·········································ed!','red'))pri··
···omputerscore··············{}'···········································fComputerAssist··
···d,board):glo··············um············································inscoreBoard:fo··
···c:ifs=='X':s·············ifs············································nd(sumScore)su···
···=0maxC=max(al············(al···········································x(minU)ifmaxC==···
···d-1)andminU>-············ma············································listMax=scoreBo···
····ax]#print('li···········Ma···········································append(ls)lmax=l···
····ax)idxOut=rand··········)v··········································ifminU==-10*(mod····
····xC<10*(mod-1):tm········is········································nnotin['X','O']:tm····
·····nd(ln)lmin=len(tmpMin)idn················in)vmin=tmpMin·······]returnvminelifminU=·····
·····1):tmpMin1=[]listMin1=sco···············orln1inlistMin1:ifln1notin['X','O']:tmpMin·····
······1)lmin1=len(tmpMin1)idnO······························in[idnOut1]returnvmin1elif······
·······1)andminU>-10*(mod-1):t······························,'O']:tmp0.append(x)l0=len······
·······drange(l0)v0=tmp0[id0]r·······················c=·····('Doyoustillwanttocontinu·······
········)ifc=='Y'orc=='y'orc==······················xit(····ECUTEinit()fromrandomim········
·········dintimporttimeimports······················rimpo···oloredos.system('color'·········
··········enceforallList!defini·····················balm····oardglobalfreeBoardglob·········
···········ssibleLinemodeGame=3····························d=[]mainBoard=[]freeBoa··········
············deGame=int(input('Wel·························segamemode(3-20):'))pri···········
·············nerateScoreBoard(modeG·····················eBoard[:]ifstart%2==0:p·············
··············t')RenderBoard(modeGame,m·············uterMove(modeGame,mainBoar··············
···············)RenderBoard(modeGame,mainBoard)UserMove(modeGame,mainBoard)de···············
·················riinrange(0,mod*mod):mainBoard.append(i+1)defRenderBoard(m·················
··················*6))+2):forxinrange(1,int((mod*10)+2)):ify%6==1:ifx%10==··················
····················e:print(colored('-','cyan'),end='')else:ifx%10==1:pr····················
······················)%10==0and(y+2)%6==0:i+=1#print(i,j,end='')iflen······················
························str(board[i-1]))-1))ifboard[i-1]=='X':print(························
···························':print(colored(board[i-1],'green'),en···························
······························print(colored(board[i-1],'red'),······························
··································='')else:print(board[i-1··································
·········································dGameStatic········································
····························································································
····························································································
····························································································
```

**5x7 LED MATRIX**
```
Input your numbers (0-9): 0123456789
LED style (@,#,X,O) [Optional]: @
Space between LED (0-5) [Optional]: 3
Choose LED color (red, green, blue, yellow) [Optional]: blue

 @@@      @      @@@    @@@@@      @    @@@@@     @@    @@@@@    @@@     @@@<br />
@   @    @@     @   @      @      @@    @        @          @   @   @   @   @\
@  @@     @         @     @      @ @    @@@@    @          @    @   @   @   @
@ @ @     @        @       @    @  @        @   @@@@      @      @@@     @@@@
@@  @     @       @         @   @@@@@       @   @   @    @      @   @       @
@   @     @      @          @      @        @   @   @    @      @   @      @
 @@@     @@@    @@@@@   @@@@       @    @@@@     @@@     @       @@@     @@
 
 OOO      O      OOO    OOOOO      O    OOOOO     OO    OOOOO    OOO     OOO
O   O    OO     O   O      O      OO    O        O          O   O   O   O   O
O  OO     O         O     O      O O    OOOO    O          O    O   O   O   O
O O O     O        O       O    O  O        O   OOOO      O      OOO     OOOO
OO  O     O       O         O   OOOOO       O   O   O    O      O   O       O
O   O     O      O          O      O        O   O   O    O      O   O      O
 OOO     OOO    OOOOO   OOOO       O    OOOO     OOO     O       OOO     OO

```

**Caesar Chiper**
```python
#TEST
step =27

ec ='The Caesar cipher is named after Julius Caesar..'
print('Encryped text: ',end='')
for e in ec:
    print(CzEncrypt(e,step),end='')

dc='Uif Dbftbs djqifs jt obnfe bgufs Kvmjvt Dbftbs..'
print('\nDecrypted text: ',end='')
for x in dc:
    print(CzDecrypt(x,step),end='')
```
```
Output:
Encryped text: Uif Dbftbs djqifs jt obnfe bgufs Kvmjvt Dbftbs..
Decrypted text: The Caesar cipher is named after Julius Caesar..
```
