#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:50:28 2023

@author: torfinn
Oppgave e) liste med diff
"""

def liste_diff(input_liste):
    differanser = []
    
    for i in range(len(input_liste) - 1):
        diff = input_liste[i + 1] - input_liste[i]
        differanser.append(diff)
        
    return differanser
    
str_liste = input("Skriv inn liste-verdier separert med komma: ")
bruker_liste = str_liste.split(",")
bruker_liste = [int(verdi) for verdi in bruker_liste]

differanser = liste_diff(bruker_liste[:-1])

print(f"\nDifferansen mellom verdiene du har gitt er: {differanser}")