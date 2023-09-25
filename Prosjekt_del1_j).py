#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:37:03 2023

@author: torfinn
Oppgave j) 
"""

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

temperaturer_tidspunkter = list()

for i in range(len(temperaturer)):
    temperaturer_tidspunkter.append(i)

def liste_diff(input_liste):
    differanser = []
    
    for i in range(len(input_liste) - 1):
        diff = input_liste[i + 1] - input_liste[i]
        differanser.append(diff)
        
    return differanser
    

differanser = liste_diff(temperaturer[:-1])

for i in range(len(differanser)):
    if differanser[i] > 0 :
        trend = "stigende"
        
    elif differanser[i] < 0 :
        trend = "synkende"
        
    else:
        trend = "uforandret"
    
    print(f"\nI {i} til {i+1} er temperatur {trend}")