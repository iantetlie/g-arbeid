#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:57:40 2023

@author: Danielkyllingstad

oppgave h
"""

def regn_vekst_bruker (temp):
    planten = 1
    while planten > 0:
        temp = input("Skriv en temperatur for å finne ut hvor fort en plante vokser: ")
        temp = int(temp)
        if temp >5:
            vekst = temp-5
            planten += vekst
        elif 0<= temp <=5:
            vekst = 0
            planten = planten
        elif temp < 0:
            vekst = temp
            planten +=vekst
        print(f"Temperaturen er {temp} og planten er {planten} stor og har vokst {vekst}")
        print()
    print("Planten døde")
        
def regn_vekst (temperaturer):
    for temp in temperaturer:
        planten = 1
        if temp >5:
            vekst = temp-5
            planten += vekst
        elif 0<= temp <=5:
            vekst = 0
            planten = planten
        elif temp < 0:
            vekst = temp
            planten +=vekst
        print(f"Temperaturen er {temp} og planten er {planten} stor og har vokst {vekst}")
        print()

        
liste_med_temp = [5, 7, 15]

regn_vekst (liste_med_temp)

regn_vekst_bruker(5)