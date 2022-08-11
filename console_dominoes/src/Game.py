from src.DominoTile import DominoTile,DominoSet
from src.DominoTile import build,build_tup,build_first
from colorama import Fore,Back,Style
from src.RoboLogic import robo_first,robo_normal
import copy,time,random

class Game:
    
    def __init__(self,a=[]):
        self.hand = a 
        
    def __str__(self,width):
        storage = []
        game=1
        hand_display=""
        storage =build_tup(self,width,game,storage)
        if len(self.hand)<=7:
            hand_display=build(0,len(self.hand),len(self.hand)-1,4,3,storage,hand_display)
            a = ' '*((width//8))
            num=""
            for i in range(1,8):
                num+=a +str(i)+' '
                if i==7:
                    num+='\n'
            hand_display+= num
        else:
            hand_display=build(0,7,6,4,3,storage,hand_display)
            a = ' '*((width//8))
            num=""
            for i in range(1,8):
                num+=a +str(i)+' '
            hand_display+= num +'\n'
            hand_display=build(7,len(self.hand),len(self.hand)-1,4,3,storage,hand_display)
            a = ' '*((width//8))
            num=""
            for i in range(8,15):
                num+=a +str(i)
            hand_display+= num
        
        return hand_display.center(width,' ')
        
class Board:
    
    def __init__(self):
        self.board = []
        self.first = DominoTile(0,0)
        self.left = DominoTile(0,0)
        self.right = DominoTile(0,0)
        self.vertical = []
        
    def __str__(self,width,play):
        storage = []
        game=2
        board_display=""
        storage =build_tup(self,width,game,storage)
        tile = self.get_first()
        num1 = self.board.index(tile)
        num2 = len(self.board)-1
        board_display = build_first(self,num2,num1,len(self.board),len(self.board)-1,width,storage,board_display,play)
            
        return board_display
    
    def set_first(self):
        tile =self.board[0]
        del self.first
        self.first = tile
    
    def get_first(self):
        return self.first
    
    def set_left_vertical(self,tile):
        del self.left
        self.left = tile
         
    def get_left_vertical(self):
        return self.left
    
    def set_right_vertical(self,tile):
        del self.right
        self.right = tile
    
    def get_right_vertical(self):
        return self.right

global remaining
global robo_hand
global player_hand
global gameboard       
        
def draw_hand(player,play,width,height,gamescore): 
    from src.Rules import clear
    clear()
    print('\n'*(height//2))
    print(Fore.YELLOW+Back.BLACK+"LET'S PICK UP SOME TILES!.".center(width,' ')+ '\n')
    time.sleep(1.5)
    n = len(gamescore.round)
    gamescore.set_round(n+1)
    gameboard = Board()
    remaining = len(play.domset)
    if player==False:
        remaining=robo_pick(width,height,play,remaining,player)
        remaining=player_pick(width,height,play,remaining,player)
        
    if player==True:
        remaining=player_pick(width,height,play,remaining,player)
        remaining=robo_pick(width,height,play,remaining,player)
        
    clear()
    global first
    first=True
    board(height,width,player,first,gameboard,remaining,play,gamescore)
    
        
def player_pick(width,height,play,remaining,player):
    alist = []
    for i in range(7):
        remaining,alist=pick(remaining,width,height,play,alist)
    global player_hand
    player_hand = Game(alist)
    print("READY!".center(width,' ')+ '\n')
    time.sleep(1)
    return remaining
        
def robo_pick(width,height,play,remaining,player):
    from src.Rules import clear
    a =[]
    for i in range(7):
        b = random.randint(0,remaining-1)
        tile = play.domset[b]
        a.append(copy.deepcopy(tile))
        remaining=remove_tile(play,b)
    global robo_hand
    robo_hand = Game(a)
    clear()
    print('\n'*(height//3))
    print("Computer is picking".center(width,' ')+ '\n')
    print("................".center(width,' ')+ '\n')
    time.sleep(1)
    print("READY!".center(width,' ')+ '\n')
    time.sleep(1)
    return remaining
        
def remove_tile(play,a):
    del play.domset[a]
    remaining = len(play.domset)
    return remaining

def board(height,width,player,first,gameboard,remaining,play,gamescore):
    top(width,remaining,play)
    middle(width,player,first)
    bottom(width,height,player,first,gameboard,remaining,play,gamescore)
    
def top(width,remaining,play):
    from src.Rules import clear
    remaining = len(play.domset)
    clear()
    print(Fore.RED+Back.GREEN+"CONSOLE DOMINOES".center(width," "))
    print(Fore.BLACK+"0 to pick up new domino tile"+' '+("Pile: "+str(remaining)+" left").rjust(width-29))
    print(f"1 - {len(player_hand.hand)} to play tile"+' '*(width-18))
    print("P to pass  Q to quit"+' '+ "You can only pass when the pile is empty".rjust(width-21))
    
def middle(width,player,first):
    if player==True:
        print("Your Turn"+' '*(width-9))
        if first==True:
            print("Choose the first domino tile for the board".center(width,' '))
            #first=False
        else:
            print("Play or Pick up a domino tile".center(width,' '))
    else:
        print("Computer's Turn"+' '*(width-15))
        if first==True:
            print("Computer will choose the first domino tile for the board".center(width,' '))
            
        else:
            print("....Computer is thinking....".center(width,' '))
        
        
def bottom(width,height,player,first,gameboard,remaining,play,gamescore):
    
    if first==True:
        a=(height//3)*2
        print(Fore.BLACK+Back.GREEN+(' '*width)*(a-1))
        
    else:
        a=((height//3)*2 - (height//4)*2)-4
        print(Fore.BLACK+Back.GREEN+(' '*width)*(a-3))
        print('\n')
        print(Board.__str__(gameboard,width,play))
        if len(gameboard.board)<10:
            print((' '*width)*(a+4))
        else:
            print((' '*width)*(a))
    print("Your Hand".center(width,' '))
    print(Game.__str__(player_hand,width))
    if len(player_hand.hand)==0 or len(robo_hand.hand)==0:
        if player==False:
            print("You have no more tiles left.".center(width,' '))
            player=True
        else:
            print("Computer has no more tiles left.".center(width,' '))
            player=False
        time.sleep(4.5)
        gamescore.set_wintype("Normal")
        if player==True:
            gamescore.set_playerpoints(1)
            gamescore.set_robopoints(0)
        else:
            gamescore.set_playerpoints(0)
            gamescore.set_robopoints(1)    
        winner(player,width,height,gamescore)
   
    if player==True:
        go = input('*: ')
        if first==True:
            normal_play(go,player_hand,gameboard,first,remaining,play,width,height,player,gamescore)
            if len(gameboard.board)>0:
                gameboard.set_first()
                first=False
            else:
                normal_play(go,player_hand,gameboard,first,remaining,play,width,height,player,gamescore)
        else:
            normal_play(go,player_hand,gameboard,first,remaining,play,width,height,player,gamescore)
            
        player=False
        board(height,width,player,first,gameboard,remaining,play,gamescore)
    else:
        time.sleep(1)
        if first==True:
            gameboard = robo_first(first,robo_hand,width,gameboard)
            gameboard.set_first()
            first=False
        else:
            gameboard,remaining = robo_normal(robo_hand,gameboard,remaining,play,width,height,player_hand,player,gamescore)

        player=True
        board(height,width,player,first,gameboard,remaining,play,gamescore)
            
def normal_play(go,player_hand,gameboard,first,remaining,play,width,height,player,gamescore):
    a = go.isdigit()
    if a==True:
      goget=int(go)
      if goget in range(1,len(player_hand.hand)+1):
          tile = player_hand.hand[goget-1]
          orient_tile(gameboard,tile,first,width,height,player,play,remaining,gamescore)
          player_hand.hand.remove(tile)
      elif goget==0:
          if remaining>0:
              remaining= fish(remaining,first,player_hand,play,width,height,player,gameboard,gamescore)
              board(height,width,player,first,gameboard,remaining,play,gamescore)
          else:
              where=5
              invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
      else:
          where=4
          invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
    elif a==False:
        b = go.isalpha()
        if b==True:
            go=go.lower()
            if go=='p':
               missturn(play,width)
            elif go=='q':
                giveup(height,width,player,first,gameboard,remaining,play,gamescore)
            else: 
                where=3
                invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
    if go=='' or go.isspace()==True:
         where=4
         invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
    
         
def orient_tile(gameboard,tile,first,width,height,player,play,remaining,gamescore):
    if first==True:
        gameboard.board.append(copy.deepcopy(tile))
    else:
        tile2= gameboard.board[0]
        if len(gameboard.board)==1:
            tile1= gameboard.board[0]
        else:
            tile1= gameboard.board[-1]
        left=(int(tile2.get_left()))
        right=(int(tile1.get_right()))
        a = tile.get_left()
        b = tile.get_right()
        if a==right :
            gameboard.board.append(copy.deepcopy(tile))
        elif b==left:
            gameboard.board.insert(0,copy.deepcopy(tile))
        elif a==left or b==right:
            flip(tile,left,right,gameboard)
        else:
            where=2
            invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
    
def flip(tile,left,right,gameboard):
    del tile.whole
    tile.whole = tile.reversed
    if tile.get_left()==right:
        gameboard.board.append(copy.deepcopy(tile))
    else:
        gameboard.board.insert(0,copy.deepcopy(tile))
           
def invalid(where,width,height,player,first,gameboard,remaining,play,gamescore):
        if where==1:
            print("You cannot go fish on the first move. Sorry.".center(width,' ')+ '\n')
        if where==2:
            print("Invalid move.Try again".center(width,' ')+ '\n')
        if where==3:
            print("P to pass. Q to quit. 0 to go fish. 1-? to play.".center(width,' ')+ '\n')
        if where==4:
            print("You fucked up. Try again".center(width,' ')+ '\n')
        if where==5:
            print("There are no tiles left. P to pass".center(width,' ')+ '\n')
        time.sleep(2.5)
        board(height,width,player,first,gameboard,remaining,play,gamescore)

def missturn(play,width):
    remaining = len(play.domset)
    if remaining==0:
        pass
    else:
        print("You cannot pass just yet. 0 to pick up a tile.".center(width,' ')+ '\n')
        time.sleep(2)

def fish(remaining,first,player_hand,play,width,height,player,gameboard,gamescore):
    if first==True:
        where=1
        invalid(where,width,height,player,first,gameboard,remaining,play,gamescore)
    else:
        remaining,player_hand.hand=pick(remaining,width,height,play,player_hand.hand)
    return remaining

def pick(remaining,width,height,play,alist):
    from src.Rules import clear,numberError
    a = False
    b = False
    remaining = len(play.domset)
    while a==False or b==False:
            clear()
            print('\n'*(height//2))
            print(("Pick a number between 1 and "+str(remaining)).center(width,' ')+ '\n')
            number = input()
            a = number.isdigit()
            if a:
                b = int(number)-1 in range(remaining)
                if b==False:
                    where = 3
                    numberError(play,where,width,height)
            else:
                where = 2
                numberError(play,where,width,height)
            if b==True:
                tile = play.domset[int(number)-1]
                alist.append(copy.deepcopy(tile))
                remaining=remove_tile(play,int(number)-1)

    return remaining,alist

def winner(player,width,height,gamescore):
    from src.Rules import clear
    from __main__ import menu
    clear()
    a=((height//3)*2 - (height//4)*2)
    print((' '*width)*(a))
    print("DOMINOES!!".center(width,' ')+ '\n')
    if player==True:
        print("YOU WON".center(width,' ')+ '\n')
        gamescore.set_winner("Player")
    else:
        print("COMPUTER WON".center(width,' ')+ '\n')
        gamescore.set_winner("Computer")
    time.sleep(2)
    print("Play Again?")
    while True:
        again = input("Y or N :  ")
        a=again.lower()
        if a == 'y':
            print("LETS PLAY THE NEXT ROUND".center(width,' ')+ '\n')
            time.sleep(2)
            nextround(player,width,height,gamescore)
        if a == 'n':
            print("THANKS FOR PLAYING".center(width,' ')+ '\n')
            time.sleep(2)
            menu()
            break

def nextround(player,width,height,gamescore):
    from src.Rules import clear
    clear()
    a=((height//3)*2 - (height//4)*2)
    print((' '*width)*(a))
    print("CURRENT SCORES".center(width,' ')+ '\n')
    gamescore.showScores(width)
    time.sleep(6)
    play = DominoSet()
    DominoSet.shuffle(play,width,height)
    clear()
    draw_hand(player,play,width,height,gamescore)
    

def noMoreMoves(player,width,height,player_hand,robo_hand,gamescore):
    from src.Rules import clear
    import sys
    clear()
    a=((height//3)*2 - (height//4)*2)
    print((' '*width)*(a))
    print("NO MORE VALID MOVES LEFT!!".center(width,' ')+ '\n')
    time.sleep(1.5)
    a ='Let\'s count your points'
    for i in a:
        print(i+'  ',end=' ')
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1.5)
    ptotal=findTotal(player_hand)
    gamescore.set_playerpoints(ptotal)
    rtotal=findTotal(robo_hand)
    gamescore.set_robopoints(rtotal)
    if ptotal>rtotal:
        player=True
    else:
        player=False
    gamescore.set_wintype("Points")
    clear()
    print(f"Your Hand Totals: {ptotal}".center(width,' '))
    print(Game.__str__(player_hand,width))
    print(f"Computer\'s Hand Totals: {rtotal}".center(width,' '))
    print(Game.__str__(player_hand,width))
    time.sleep(3)
    winner(player,width,height,gamescore)
     
def findTotal(self):
    total=0
    for tile in self.hand:
        total+=self.total
    return total
        
def giveup(height,width,player,first,gameboard,remaining,play,gamescore):
    from src.Rules import clear
    from __main__ import menu
    clear()
    a=((height//3)*2 - (height//4)*2)
    print((' '*width)*(a))
    print("ARE YOU SURE YOU WANT TO QUIT?".center(width,' ')+ '\n')
    time.sleep(2)
    
    while True:
        again = input("Y or N :  ")
        a=again.lower()
        if a == 'n':
            print("LETS KEEP PLAYING".center(width,' ')+ '\n')
            time.sleep(2)
            board(height,width,player,first,gameboard,remaining,play,gamescore)
            break
        if a == 'y':
            print("THANKS FOR PLAYING".center(width,' ')+ '\n')
            time.sleep(2)
            menu()
            break