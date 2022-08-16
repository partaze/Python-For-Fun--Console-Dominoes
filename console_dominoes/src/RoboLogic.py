
from src.DominoTile import DominoTile,DominoSet
import copy,random,time
"""
Created on Wed Jul 27 23:38:31 2022

@author: Cheryl Vadivello
Docstrings to come
"""
def robo_first(first,robo_hand,width,gameboard):#GET RID OF WIDTH SOON
    from src.Game import Board,Game,board
    from src.Rules import clear
    
    double=[]
    playable =[]
    gamedict ={}
    k = len(robo_hand.hand)
    for i in range(k):
        tile= robo_hand.hand[i]
        a=int(tile.get_left())
        b=int(tile.get_right())
        c = a+b
        if a==b:
            double.append(i)
            w=str(i)
            gamedict[w]=a
        
        if i!=6:
            for j in range((i+1),k):
                tile2 =robo_hand.hand[j]
                if a in tile2.whole or b in tile2.whole:
                    d=int(tile.get_left())
                    e=int(tile.get_right())
                    f=d+e
                    #heavy = max(c,f)
                    if c>f:
                        playable.append(i)
                    else:
                        playable.append(j)
                else:
                    continue
    double1=set(double)
    playable1=set(playable)
    
    if len(double)>0:
        if len(double)==1:
            j=double[0]
            toplay=copy.deepcopy(robo_hand.hand[j])
            del robo_hand.hand[j]
        else:
            its = playable1.intersection(double1)
            if len(its)!=0:
                anIndex = int 
                anIndex = midrun(its,gamedict)
            else:
                anIndex = int 
                anIndex = midrun(double,gamedict) 
            toplay=copy.deepcopy(robo_hand.hand[anIndex])
            del robo_hand.hand[anIndex]
            print(toplay.whole)
    else:
        i = random.randint(0,len(playable)-1)
        j=playable[i]
        toplay=copy.deepcopy(robo_hand.hand[j])
        del robo_hand.hand[j]
        print(toplay.whole)
        
    gameboard.board.append(toplay)       
    return gameboard

def midrun(abc,gamedict):
    b=[]
    for i in abc:
        a=str(i)
        b.append(gamedict.get(a))
        bigger = max(b)
        a=b.index(bigger)
    return a 

def robo_normal(robo_hand,gameboard,remaining,play,width,height,player_hand,player,gamescore):
    from src.Game import board

    tile= gameboard.board[0]
    if len(gameboard.board)==1:
        tile1= gameboard.board[0]
    else:
        tile1= gameboard.board[-1]
    left=(int(tile.get_left()))
    right=(int(tile1.get_right()))
    anIndex ={}
    playable =[]
    LCount =0
    RCount = 0
    k = len(robo_hand.hand)
    for i in range(k):
        tile= robo_hand.hand[i]
        inIt(i,tile,left,right,anIndex)

    if len(anIndex) ==0 and remaining>0:
        remaining,anIndex=robo_pickup(robo_hand,remaining,play,left,right,anIndex,width)
    if len(anIndex)==1:
        key1=list(anIndex.keys())
        key=key1[0]
        gameboard = toplay(anIndex,robo_hand,gameboard,key)
    if len(anIndex) >1:
        playable=[]
        k = anIndex.keys()
        for key in k:
            tile= robo_hand.hand[int(key)]
            side = anIndex.get(key)
            playable,LCount,RCount=analyse(side,tile,robo_hand,key,playable,LCount,RCount)
            
        a=[]
        if len(playable)>=1:
            if LCount>RCount:
                for tup in playable:
                    if 'left' in tup or 'both' in tup:
                        a.append(tup)
            elif RCount>LCount:
                for tup in playable:
                    if 'right' in tup:
                        a.append(tup)
        else:
            key = random.choice(list(anIndex))
            
        if len(a)==1:
            key1 = [x[0] for x in a]
            key = key1[0]
        if len(a)>1:
            match = [x[1]for x in a]
            time.sleep(4)
            bigger = max(match)
            i = match.index(bigger)
            j = a[i]
            key = j[0]
        gameboard = toplay(anIndex,robo_hand,gameboard,key)
        
    if len(anIndex) ==0 and remaining==0: 
        robo_pass(width,height,player_hand,robo_hand,left,right,player,gamescore)
        gameboard=copy.deepcopy(gameboard)
        remaining = len(play.domset)
        player=True
        first=False
        board(height,width,player,first,gameboard,remaining,play,gamescore)
    
    time.sleep(2) 
    return gameboard,remaining

def analyse(side,tile,robo_hand,key,playable,LCount,RCount):
    match=0
    s=0
    if "right" in side:
        RCount+=1
    else:
        LCount+=1      #Takes care of 'left' and 'both'
    if side=='right 0':
        s=tile.get_right()
    if side=='right 1':
        s=tile.get_left()
    if side=='left 0':
        s=tile.get_right()
    if side=='left 1':
        s=tile.get_left()
    if side=='both 0':
        s=tile.get_right()
    if side=='both 1':
        s=tile.get_left()
        
    for item in robo_hand.hand:
        if item is not tile:
            j=item.whole.count(s)
            if j>0:
                match+=1
    side1 = side.split()
    if match>0:
        playable.append((key,match,side1[0]))
    return playable,LCount,RCount



def inIt(i,tile,left,right,anIndex):
    w=str(i)
    if left==right:
        Bcount=tile.whole.count(left)
        if Bcount>0:
            j=tile.whole.index(left)
            anIndex[w]= "both "+ str(j)
    else:
        Lcount = tile.whole.count(left)
        if Lcount>0:
            j=tile.whole.index(left)
            anIndex[w]= "left "+ str(j)

        Rcount = tile.whole.count(right)
        if Rcount>0:
            j=tile.whole.index(right)
            anIndex[w]= "right "+ str(j)

    return anIndex
            
def toplay(anIndex,robo_hand,gameboard,key):
        tile=robo_hand.hand[int(key)]
        val=anIndex.get(key)
        if val=='right 1'or val=='left 0' or val=='both 0':
            del tile.whole
            tile.whole = tile.reversed
        if 'right'in val:
            gameboard.board.append(copy.deepcopy(tile))
        else:
            gameboard.board.insert(0,copy.deepcopy(tile))
        del robo_hand.hand[int(key)]

    
        return gameboard

def robo_pass(width,height,player_hand,robo_hand,left,right,player,gamescore):
    from src.Game import noMoreMoves
    anIndex = []
    for i in range(len(player_hand.hand)):
        tile= player_hand.hand[i]
        anIndex = inIt(i,tile,left,right,anIndex) 
        if len(anIndex)>0:
            break
    print("Computer cannot make a valid move. Computer passed.".center(width,' ')+ '\n')    
    if len(anIndex)>0:
        print("You cannot make a valid move.".center(width,' ')+ '\n') 
        time.sleep(2.5)
        noMoreMoves(player,width,height,player_hand,robo_hand,gamescore)
    else:
        time.sleep(2.5)
    
def robo_pickup(robo_hand,remaining,play,left,right,anIndex,width):
    count=0
    while True:
        remaining=len(play.domset)
        if remaining==0:
            break
        if remaining==1:
            i=0
        else:
            i= random.randint(0,remaining-1)
        r = play.domset[i]
        robotile = copy.deepcopy(r)
        play.domset.remove(r)
        robo_hand.hand.append(robotile)
        count+=1
        i=robo_hand.hand.index(robotile)
        remaining-=1
        anIndex=inIt(i,robotile,left,right,anIndex)
        if len(anIndex)>0:
            break
    if count>0:
        if count==1:
            print("Computer picked up a tile".center(width,' ')+ '\n')
        else:
            c=str(count)
            print(("Computer picked up "+ c+" tiles").center(width,' ')+ '\n')
        time.sleep(0.5) 

    return remaining,anIndex
    
