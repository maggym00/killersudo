#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:50:26 2018

@author: magnushall
"""

#Killer sudoku assistant
        

# Functions dedicated to initialising the sequence and setting up the first one (defined by max on lhs)
# check if a duplicated number exists in the sequence
def dup_check(*_list):
    duplicate=False
    for i in range(len(_list)):
        temp=_list[:]
        if _list[i] in temp.pop(i):
            duplicate=True
    return duplicate
            
# if duplicated numbers exist in the sequence - change the sequence until they no longer exist
def dup_fix(*_list):
    while dup_check(*_list):
        for i in range(len(_list)):
            temp=_list[:]
            if _list[i] in temp.pop(i):
                _list[i]+=1
                _list[i-1]-=1
    return _list

#create a list defining the initial sequence, containing numbers between 1-9 with the only duplicated number being 1 on the far rhs   
def initialise(*_list,n):
    current=0
    maximum=9
    while sum(_list)<n:
        if _list[current]<maximum:
            _list[current]+=1
        else:
            current+=1
            maximum-=1
    _list=dup_fix(_list)
    return _list
        
# check that the sum and length combination is valid
def seq_exists(n,l):
    j=9
    maximum=0
    for i in range(l):
        maximum+=j
        j-=1
    if maximum>n:
        return True
    else:
        return False
        
def give_combo(n,l):
    
    if seq_exists(n,l):
        print("invalid input")
        exit(0)
        
    templist=[]
    for i in range(l):
        templist.append(1) 
    

