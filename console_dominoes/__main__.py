#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 18:00:55 2022

@author: Cheryl Vadivello
I will get some docstrings happening soon.
"""

import time
import os,sys
from colorama import Fore,Back,Style,init
from src.DominoTile import DominoSet,DominoTile
from src.Rules import rules,clear,goes_first,about
from src.Scoring import Scores
init()

def intro():
    for i in range(3):
        print(Back.BLACK+'\n'*(height//2))
        print(Fore.YELLOW+Back.RED+"FOR BETTER GAMING EXPERIENCE MAXIMIZE THE TERMINAL WINDOW".center(width,' '))
        time.sleep(0.5)
        if i == 2: time.sleep(1.5)
        print(Style.RESET_ALL)
        clear()
        time.sleep(0.5)
    screen_size()
    print('\n'*(height//2))
    print("CONSOLE DOMINOES".center(width,' '))
    time.sleep(2)
    clear()
    
def menu():
    print((Fore.YELLOW + Back.BLACK +'*'*width)*3)
    for i in range(height-9):
        if i==(3):
            print('*'*6 + (' '*((width-12)//2)) + Fore.RED+"MENU"+ Fore.YELLOW+(' '*(((width-12)//2)-4))+'*'*6)
        if i==(5):
            print('*'*6 + (' '*((width-12)//3)) + "1. NEW GAME"+ (' '*((((width-12)//3))*2-11))+'*'*6)
        if i==(7):
            print('*'*6 + (' '*((width-12)//3)) + "2. RULES"+ (' '*((((width-12)//3))*2-8))+'*'*6)
        if i==(9):
            print('*'*6 + (' '*((width-12)//3)) + "3. ABOUT"+ (' '*((((width-12)//3))*2-8))+'*'*6)
        if i==(11):
            print('*'*6 + (' '*((width-12)//3)) + "4. QUIT"+ (' '*((((width-12)//3))*2-7))+'*'*6)
        else:
            print('*'*6 + (' '*(width-12)) +'*'*6)
        
    print(('*'*width)*3)
    
    choice = input(Fore.RED+ '''CHOOSE A FUNCTION "1 - 3":''')
    if choice==str(1):
        play = DominoSet()
        gamescore = Scores()
        clear()
        DominoSet.shuffle(play,width,height)
        goes_first(play,width,height,gamescore)
        
    elif choice==str(2):
        rules(width,height)
    elif choice==str(3):
        about(width,height)
    elif choice==str(4):
        Quit(width)
    else:
        clear()
        menu()
            
    print(Style.RESET_ALL)

def Quit(width):
    clear()
    print(Fore.YELLOW+'*'*6 + (' '*((width-12)//2)) + Fore.RED+"BYE!!"+ Fore.YELLOW+(' '*(((width-12)//2)-4))+'*'*6)
    print(Style.RESET_ALL)
    sys.exit()

def screen_size():
    size = os.get_terminal_size()
    global width
    width =int(size[0])
    global height
    height =int(size[1])
    
def main():
    screen_size()
    time.sleep(5)
    clear()
    intro()
    show = DominoSet()
    print(DominoSet.__str__(show,width))
    time.sleep(3)
    clear()
    menu()

main()