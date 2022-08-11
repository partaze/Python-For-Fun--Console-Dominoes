import time,random,copy,sys
from src.DominoTile import DominoTile,DominoSet
from src.Game import draw_hand
from colorama import Fore,Back,Style


def rules(width,height):
    from __main__ import menu
    a = '''To see who gets to play first each player draws a tile from the set.'''
    b = '''The one with the highest double will go first. If a double wasn't drawn'''
    c = '''the person with the heaviest tile (the greater sum) will go first.'''
    d = '''The computer will always play a double if it gets to start but you do'''
    e = '''not have to.You can play whatever you like on the first go.'''
    f = '''Match your tiles with the ones on the board. Use your numberpad to select'''
    g = '''a tile followed by enter to play it. If you cannot make a move, use 0 to''' 
    h = '''go fish. It will remain your turn until you can play a tile.'''
    j = '''You will not be able to pass if there are still domino tiles in the pile.'''
    k = '''The one who plays all the tiles in their hand wins.'''
    l = '''If no one can make a move and the pile is empty, the winner will be'''
    m = '''decided based on the sum of the tiles in their hand.'''
    
    print((Fore.YELLOW + Back.BLACK +'*'*width)*3)
    for i in range(height-19):
        if i==(1):
            print('*'*6 + (' '*((width-12)//2)) + Fore.RED+"RULES"+ Fore.YELLOW+(' '*(((width-12)//2)-5))+'*'*6)
        if i==(3):
            print('*'*6 + (' '*((width-12)//5)) + a + (' '*((((width-12)//5))*2-11))+'*'*6)
        if i==(4):
            print('*'*6 + (' '*((width-12)//5)) + b + (' '*((((width-12)//5))*2-14))+'*'*6)
        if i==(5):
            print('*'*6 + (' '*((width-12)//5)) + c + (' '*((((width-12)//5))*2-9))+'*'*6)
        if i==(6):
            print('*'*6 + (' '*((width-12)//5)) + d + (' '*((((width-12)//5))*2-12))+'*'*6)
        if i==(7):
            print('*'*6 + (' '*((width-12)//5)) + e + (' '*((((width-12)//5))*2-2))+'*'*6)
        if i==(9):
            print('*'*6 + (' '*((width-12)//5)) + f + (' '*((((width-12)//5))*2-16))+'*'*6)
        if i==(10):
            print('*'*6 + (' '*((width-12)//5)) + g + (' '*((((width-12)//5))*2-15))+'*'*6)
        if i==(11):
            print('*'*6 + (' '*((width-12)//5)) + h + (' '*((((width-12)//5))*2-3))+'*'*6)
        if i==(12):
            print('*'*6 + (' '*((width-12)//5)) + j + (' '*((((width-12)//6))*2-8))+'*'*6)
        if i==(14):
            print('*'*6 + (' '*((width-12)//5)) + k + (' '*((((width-12)//5))*2+6))+'*'*6)
        if i==(15):
            print('*'*6 + (' '*((width-12)//5)) + l + (' '*((((width-12)//5))*2-10))+'*'*6)
        if i==(16):
            print('*'*6 + (' '*((width-12)//5)) + m + (' '*((((width-12)//5))*2+5))+'*'*6)
        else:
            print('*'*6 + (' '*(width-12)) +'*'*6)
        
    print(('*'*width)*3)
    
    while True:
        back=input("PRESS ENTER TO GO BACK")
        if back=='':
            menu()
            break

def about(width,height):
    from __main__ import menu
    a = '''This is v1.0. There might be a few bugs that Im unaware of.'''
    b = '''I wrote this program for someone dear to me and I wanted'''
    c = '''to do it a little bit different; with my own spin.'''
    d = '''I like to think that I have given it a GUI feel although'''
    e = '''it is console based.'''
    f = '''I plan to launch a real GUI version in the near future so '''
    g = '''stay posted. In the meantime enjoy the game!''' 
    h = '''For display purposes, the game is best played with the window'''
    j = '''maximized or in full screen mode Try not to press any buttons.'''
    k = '''before you are asked to!'''
    l = '''Any comments or advice, direct them to my github page:'''
    m = '''https://github.com/partaze'''
    
    print((Fore.YELLOW + Back.BLACK +'*'*width)*3)
    for i in range(height-19):
        if i==(1):
            print('*'*6 + (' '*((width-12)//2)) + Fore.RED+"ABOUT"+ Fore.YELLOW+(' '*(((width-12)//2)-5))+'*'*6)
        if i==(3):
            print('*'*6 + (' '*((width-12)//5)) + a + (' '*((((width-12)//5))*2-2))+'*'*6)
        if i==(4):
            print('*'*6 + (' '*((width-12)//5)) + b + (' '*((((width-12)//5))*2+1))+'*'*6)
        if i==(5):
            print('*'*6 + (' '*((width-12)//5)) + c + (' '*((((width-12)//5))*2+7))+'*'*6)
        if i==(6):
            print('*'*6 + (' '*((width-12)//5)) + d + (' '*((((width-12)//5))*2+1))+'*'*6)
        if i==(7):
            print('*'*6 + (' '*((width-12)//5)) + e + (' '*((((width-12)//4))*3-11))+'*'*6)
        if i==(9):
            print('*'*6 + (' '*((width-12)//5)) + f + (' '*((((width-12)//5))*2-1))+'*'*6)
        if i==(10):
            print('*'*6 + (' '*((width-12)//5)) + g + (' '*((((width-12)//5))*2+13))+'*'*6)
        if i==(11):
            print('*'*6 + (' '*((width-12)//5)) + h + (' '*((((width-12)//5))*2-4))+'*'*6)
        if i==(12):
            print('*'*6 + (' '*((width-12)//5)) + j + (' '*((((width-12)//5))*2-5))+'*'*6)
        if i==(13):
            print('*'*6 + (' '*((width-12)//5)) + k + (' '*((((width-12)//4))*3-15))+'*'*6)
        if i==(15):
            print('*'*6 + (' '*((width-12)//5)) + l + (' '*((((width-12)//5))*2+3))+'*'*6)
        if i==(16):
            print('*'*6 + (' '*((width-12)//5)) + m + (' '*((((width-12)//4))*3-17))+'*'*6)
        else:
            print('*'*6 + (' '*(width-12)) +'*'*6)
        
    print(('*'*width)*3)
    
    while True:
        back=input("PRESS ENTER TO GO BACK")
        if back=='':
            menu()
            break
def clear():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    sys.stdout.flush()
    
def numberError(play,where,width,height):
    clear()
    print('\n'*(height//2))
    if where==1:
        print(Fore.YELLOW+Back.BLACK+"Number has to be a digit between 1 and 28 without spaces or commas.".center(width,' ')+ '\n')
        time.sleep(3)
        goes_first(play,width,height)
    elif where==2:
        print(Fore.YELLOW+Back.BLACK+"Number has to be a digit. Try again.".center(width,' ')+ '\n')
        time.sleep(2)
    else:
        print(Fore.YELLOW+Back.BLACK+"Number has to be between the given range. Try again.".center(width,' ')+ '\n')
        time.sleep(2)
    
def goes_first(play,width,height,gamescore):
    clear()
    print('\n'*(height//2))
    print(Fore.YELLOW+Back.BLACK+"Who will go first?".center(width,' ')+ '\n')
    number = input("Pick a number between 1 and 28 to draw a tile:")
    a = False
    b = False
    where = 1
    a = number.isdigit()
    if a:
        b = int(number)in range(1,29)
        time.sleep(1)
    else:
        numberError(play,where,width,height)
    
    if b==True:
        tile = play.domset[int(number)-1]
        play.removed.append(tile)
        play.domset.remove(tile)     #Removes the picked tile from the domino set
        i= random.randint(0,26)
        robotile = play.domset[int(i)]
        clear()
        print(Style.RESET_ALL)
        print(Back.BLACK)
        global player
        player= DominoTile.show(tile,robotile,width)
        play.domset.append(tile)           #Returns the picked tile to the domino set
        play.removed.remove(tile)
        clear()
        DominoSet.shuffle(play,width,height)
        clear()
        draw_hand(player,play,width,height,gamescore)
    else:
        numberError(play,where,width,height)


    