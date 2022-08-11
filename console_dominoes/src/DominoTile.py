import random
import time
import sys
from colorama import Fore,Back

class DominoTile:
      
      def  __init__(self, left, right):
          
          self.whole = (left, right)
          self.reversed =(right,left)
          total = left + right
          self.total = total
      
      def get_left(self):
          self.left = self.whole[0]
          return self.left
          
      def get_right(self):
          self.right = self.whole[1]
          return self.right
          
      def __str__(self):
          
          outer ='_'*3+' '
          blank = '|   '
          bl2 = '|___|___|'
          a = f'{self.whole[0]}'.center(3,' ') + '|'
          b = f'{self.whole[1]}'.center(3,' ') + '|'
          fil = ' |' + a+ b 
          tdisplay = '  '+ outer*2+'\n'+ ' ' + blank*2 + '|'+'\n' + fil + '\n ' +bl2
          return tdisplay
      
      def vertical(self,width,right=False,r3=0,r4=0):
          outer ='_'*3
          blank = '|   '
          bl2 = '|___|'
          a = f'{self.whole[0]}'.center(3,' ') + '|'
          b = f'{self.whole[1]}'.center(3,' ') + '|'
          fil = ' |' + a
          fil2 = ' |' + b
          if right==True:
              r = ' '*((width-r3))
              r2 = ' '*((width-r4))
              tdisplay = r2 + outer+'\n'+r+' '+ blank + '|'+'\n' + r+fil + '\n '+r +bl2+'\n'+ r +' '+blank+ '|'+'\n' + r+ fil2 + '\n '+r +bl2
          else:
              fil = ' |' + b
              fil2 = ' |' + a
              tdisplay = '    '+ outer+'\n'+ '   ' + blank + '|'+'\n' + '  '+fil + '\n '+'  ' +bl2+'\n'+ '   ' + blank + '|'+'\n' +'  '+ fil2 + '\n '+'  ' +bl2
          return tdisplay
      
      def show(tile,robotile,width):
          
          print(Fore.YELLOW+Back.BLACK+('*'*width)*3+'\n')
          print("You picked:".center(width,' '))
          print(tile)
          print('\n'+('*'*width)*3+'\n')
          print("Computer picked:".center(width,' '))
          print(robotile)
          print('\n'+('*'*width)*3+'\n')
          
          a = tile.whole[0] + tile.whole[1]
          b = robotile.whole[0]+ robotile.whole[1]
          if a > b:
              print("YOU START".center(width,' '))
              player = True
          else:
              print("COMPUTER STARTS".center(width,' '))
              player = False
          time.sleep(2)
          return player
              

class DominoSet(DominoTile):
    
    def __init__(self):
        self.removed = []
        self.domset = []
        x = 0                
        for j in range(x,7):
            for k in range(x,7):
                tile=DominoTile(j,k)
                self.domset.append(tile)
                if k==6:
                  x+=1
    
    def shuffle(self,width,height):
          
          print('\n'*(height//2)+ ' '*(width//4), end=' ')
          a ='mixing tiles'
          for i in a:
              print(i+'   ',end=' ')
              sys.stdout.flush()
              time.sleep(0.2)
              
          time.sleep(0.2)
          random.shuffle(self.domset)
          random.shuffle(self.domset) #Shuffle it twice for good luck :)
          
              
    def  __str__(self,width):
              domset_display=""
              storage = []
              game=0
              storage=build_tup(self,width,game,storage)
                                
              domset_display=build(0,5,4,4,3,storage,domset_display)
              domset_display=build(5,10,9,4,3,storage,domset_display)
              domset_display=build(10,15,14,4,3,storage,domset_display)
              domset_display=build(15,20,19,4,3,storage,domset_display)
              domset_display=build(20,25,24,4,3,storage,domset_display)
              domset_display=build(25,28,27,4,3,storage,domset_display)
              
              return domset_display
    
def build(a,b,c,d,e,storage,domset_display):
        x=0
        for x in range(x,d):
            for i in range(a,b):
                tile = storage[i]
                domset_display+= tile[x]
                if i==c:
                   domset_display+='\n'
                   if x==e:
                       break
                   else:
                       x+=1
        
        return domset_display
    
def build_tup(self,width,game,storage):
    
    if game==1:
         b=self.hand
         i=14
    elif game==2:
         b=self.board
         i=width
    elif game==3:
         b=self.vertical
         i=width
    else:
        b=self.domset
        i=8
    for item in b:
        display =str(item)
        tdisplay = display.split('\n')
        if game==2 or game==3:
            disp1 = tdisplay[0]
            disp2 = tdisplay[1] 
            disp3 = tdisplay[2]
            disp4 = tdisplay[3]
            if game==3:
                disp5 = tdisplay[4]
                disp6 = tdisplay[5]
                disp7 = tdisplay[6]
        else:
            a = ' '*(width//i)
            disp1 = a + tdisplay[0]
            disp2 =a +' '+ tdisplay[1].strip() 
            disp3 = a +' '+tdisplay[2].strip()
            disp4 = a + tdisplay[3] 
        if game==3:
            tup = (disp1,disp2,disp3,disp4,disp5,disp6,disp7)
        else:
            tup = (disp1,disp2,disp3,disp4)
        storage.append(tup)
    return storage

def build_first(self,z,a,b,c,width,storage,board_display,play):
    x=0
    y=0
    rightv= z-a
    if rightv>=7:
        c-=(rightv-6)
        b = c+1
    if a==8:
        tile = self.board[0]
        self.set_left_vertical(tile)
    if rightv==7:
        tile = self.board[-1]
        self.set_right_vertical(tile)
        
    if a==0:
        fill = " "*((width//2)-5)
    if a<=7:
        fill = " "*(((width//2)-5)-(10*a))
    if a>=8:
        fill = "  "
        y=a-7

    for x in range(x,4):
        board_display+= fill
        for i in range(y,b):
            tile = storage[i]
            board_display+= tile[x]
            if i==c:
                board_display+='\n'
                if x==3:
                   break
                else:
                   x+=1
                   
    if a>=8 and rightv>=7:
        tile = self.get_left_vertical()
        tile1 = self.get_right_vertical()
        t=DominoTile.vertical(tile,width,right=False)
        t1=DominoTile.vertical(tile1,width,right=True,r3=((width//7)+1),r4=((width//7)-2))
        self.vertical.append(t)
        self.vertical.append(t1)
        theindex = self.board.index(tile)
        w=self.board.index(tile1)
        board_display =build_double_vertical(self,a,rightv,theindex,w,width,board_display,storage)
              
    if a==8 and rightv<7:
        tile =self.get_left_vertical()
        to_add=DominoTile.vertical(tile,width,right=False)
        board_display+=to_add
    
    if rightv==7 and a<8:
        tile =self.get_right_vertical()
        to_add=DominoTile.vertical(tile,width,right=True,r3=((width//10)+1),r4=((width//10)-1))
        board_display+=to_add+'\n'
        
    if a>8 and rightv<7:
        tile = self.get_left_vertical()
        theindex = self.board.index(tile)
        to_add=DominoTile.vertical(tile,width,right=False)
        board_display+=to_add+'\n'
        k = 0
        l = theindex
        fill = '  '
        board_display =loopyloop(self,k,l,storage,board_display,fill)
        
    if rightv>7 and a<8:
        tile = self.get_right_vertical()
        w=self.board.index(tile)
        to_add=DominoTile.vertical(tile,width,right=True,r3=((width//10)+1),r4=((width//10)-1))
        board_display+=to_add+'\n'
        fill= rightfill(width,rightv)
        k = w+1
        l = len(self.board)
        board_display =loopyloop(self,k,l,storage,board_display,fill)
    
    return board_display

def loopyloop(self,k,l,storage,board_display,fill):
         x=0
         for x in range(x,4):
            board_display+= fill
            x,board_display = runnyrun(self,k,l,x,board_display,storage)
                       
         return board_display

def runnyrun(self,k,l,x,board_display,storage):
    for i in reversed(range(k,l,1)):
        tile = storage[i]
        tile1=self.board[i]
        if x==2:
            a = f'{tile1.whole[1]}'.center(3,' ') + '|'
            b = f'{tile1.whole[0]}'.center(3,' ') + '|'
            fil = ' |' + a+ b
            board_display+= fil
        else:
            board_display+= tile[x]
        if i==k:
            board_display.rstrip()
            board_display+='\n'
            if x==3:
               break
            else:
               x+=1   
               
    return x,board_display

def dloopyloop(self,k,l,storage,board_display,fill,m,n,fill2):
         x=0
         for x in range(x,4):
            board_display+= fill
            for i in reversed(range(k,l,1)):
                tile = storage[i]
                tile1=self.board[i]
                if x==2:
                    a = f'{tile1.whole[1]}'.center(3,' ') + '|'
                    b = f'{tile1.whole[0]}'.center(3,' ') + '|'
                    fil = ' |' + a+ b
                    board_display+= fil
                else:
                    board_display+= tile[x]
                if i==k:
                    board_display+= fill2
                    x,board_display = runnyrun(self,m,n,x,board_display,storage)
                       
         return board_display
      
def build_double_vertical(self,a,rightv,theindex,w,width,board_display,storage1):
    game=3
    storage=[]
    storage =build_tup(self,width,game,storage)
    board_display=build(0,2,1,7,6,storage,board_display)
    d = rightv -7
    if a>8 and rightv==7:
        k = 0
        l = theindex
        fill = '  '
        board_display =loopyloop(self,k,l,storage1,board_display,fill)
    if rightv>7 and a==8:
        fill= rightfill(width,rightv)
        fill+="  "
        k = w+1
        l = len(self.board)
        board_display =loopyloop(self,k,l,storage1,board_display,fill)
    if a>8 and rightv>7:
        k = 0
        l = theindex
        e = a-8
        fill = '  '
        m = w+1
        n = len(self.board)
        fill2=' '* ((((15*9)+2) -(9*e + 9*d))-(rightv-9)-(a-9))
        board_display =dloopyloop(self,k,l,storage1,board_display,fill,m,n,fill2)
    return board_display

def rightfill(width,rightv):
    d = rightv -7
    f =(width-((width//10)+5))
    if d==1:
        fill = " "* f
    else:
        g = ((15*9)+3) -((9*d))-(rightv-9)
        fill = " "* g
    
    return fill