#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:15:09 2023

@author: Danielkyllingstad

øving 4 oppgave h og l
siste versjon
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
    total_vekst = 0
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
        total_vekst += vekst
        print()
    if total_vekst > 0:
        print(f"Plantens totale vekst er {total_vekst} etter alle temperaturene")
        print()
    else:
        print("Planten døde")

        
liste_med_temp = [5, 7, 15, 10, -12, -1]

regn_vekst (liste_med_temp)

regn_vekst_bruker(5)



