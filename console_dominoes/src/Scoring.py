#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:40:53 2022

@author: Cheryl Vadivello
Keeps track of game rounds and scores
"""

class Scores():
    
    def __init__(self):
        self.round = []
        self.playerpoints = []
        self.robopoints = []
        self.wintype=[]
        self.winner = []
        
    def set_round(self,a):
        self.round.append(a)
        
    def get_round(self,a):
        return self.round[a]
    
    def set_playerpoints(self,b):
        self.playerpoints.append(b)
        
    def get_playerpoints(self,b):
        return self.playerpoints[b]
    
    def set_robopoints(self,c):
        self.robopoints.append(c)
        
    def get_robopoints(self,c):
        return self.robopoints[c]
    
    def set_wintype(self,a):
        self.wintype.append(a)
        
    def get_wintype(self,a):
        return self.wintype[a]
    
    def set_winner(self,a):
        self.winner.append(a)
        
    def get_winner(self,a):
        return self.winner[a]
    
    def showScores(self,width):
        import time
        j=len(self.round)
        ptotal=0
        rtotal=0
        for i in range(j):
            a= self.get_round(i)
            b= self.get_winner(i)
            c= self.get_wintype(i)
            d= self.get_playerpoints(i)
            ptotal+=d
            e= self.get_robopoints(i)
            rtotal+=e
            print("   ",end="*")
            print(f"ROUND : {a}  WINNER : {b}        WINTYPE : {c}     PLAYERPOINTS : {d}  COMPUTERPOINTS : {e}")
        print('\n'+"   ",end="*")
        print(f"TOTAL PLAYERPOINTS : {ptotal}   TOTAL COMPUTERPOINTS : {rtotal}")
        time.sleep(4)