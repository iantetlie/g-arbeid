#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:00:43 2023

@author: Danielkyllingstad
"""

import csv
import matplotlib.pyplot as plt

class Vermaling:
    def __init__(self, navn, stasjon, str_dato, snodybde, nedbor, temperatur, skydekke, vindhastighet):
        self.navn = navn
        self.stasjon = stasjon
        self.dato = str_dato
        self.snodybde = snodybde
        self.nedbor = nedbor
        self.temperatur = temperatur
        self.skydekke = skydekke
        self.vindhastighet = vindhastighet

def function(listen, maalepunkt):
    teller = 0
    for verdi in listen:
        if verdi >= maalepunkt:
            teller += 1
    return teller

vermalinger = []

with open("snoedybder_vaer_en_stasjon_dogn.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    data = list(csvreader)

header = data[0]
data = data[1:]

data_obj = []
for rad in data:
    data_obj.append(Vermaling(rad[0], rad[1], rad[2], rad[3], rad[4], rad[5], rad[6], rad[7]))

aarstall = 1980
aarene = []
skiføre_dager_periode = []

for j in range(41):
    skiføre_dager_per_dag = []

    for i in range(len(data_obj)):
        try:
            year = int(data_obj[i].dato[6:10])
            month = int(data_obj[i].dato[3:5])
            
            
            if (year == aarstall and 10 <= month <= 12) or (year == aarstall + 1 and 1 <= month <= 6):
                sn = float(data_obj[i].snodybde)
                
                
                if sn >= 20:
                    skiføre_dager_per_dag.append(sn)
                    
        except (ValueError, IndexError):
            continue

    if len(skiføre_dager_per_dag) >= 1:  
        skiføre_dager_periode.append(len(skiføre_dager_per_dag))
        aarene.append(aarstall)

    aarstall += 1
sesong = []


for i in range(len(aarene)):
    sesong.append({f"{aarene[i]}-{aarene[i]+1}": skiføre_dager_periode[i]})


"Oppgave c):"
#Denne funksjonen beregner trenden for skidager per år
def trend_data(x_liste, y_liste):
    x_snitt = sum(x_liste) / len(x_liste)
    y_snitt = sum(y_liste) / len(y_liste)  # Bruk len(y_liste) for antall elementer i y-listen
    
    sum_teller = 0.0
    sum_nevner = 0.0

    for i in range(len(x_liste)):
        sum_teller += (x_liste[i] - x_snitt) * (y_liste[i] - y_snitt)
        sum_nevner += (x_liste[i] - x_snitt) ** 2

    a = sum_teller / sum_nevner
    b = y_snitt - a * x_snitt

    return a, b

resultat = trend_data(aarene, skiføre_dager_periode)
print("Trendkoeffisienter (stigningstall og konstantledd):", resultat)

#Denne koden lager en scatter plot med en trendlinje for skiføre dager per år
a, b = trend_data(aarene, skiføre_dager_periode)

plt.scatter(aarene, skiføre_dager_periode, label="Data")

trend_linje = [a * x + b for x in aarene]
plt.plot(aarene, trend_linje, color="red", label="Trendlinje")

plt.xlabel("År")
plt.ylabel("Skiføre dager")
plt.title("Trenden til skiføre dager per år")
plt.legend()
plt.grid(True)
plt.show()



plt.figure(figsize=(10, 6)) 

#Denne kode lager ett linje diagram over antall ski dager per år.
plt.plot(aarene, skiføre_dager_periode, marker="o", linestyle="-")

plt.xlabel("Årstall for skisesongen")
plt.ylabel("Antall dager med skiføre (20cm snø eller mer)")
plt.title("Antall dager med skiføre per skisesong")


plt.grid(True)  
plt.xticks(aarene)  
plt.tight_layout()  
plt.show()

"Oppgave g):"
from collections import defaultdict

for obj in data_obj:
    skydekke_val = obj.skydekke.replace(",", ".")
    obj.skydekke = float(skydekke_val) if skydekke_val not in ("-", "") else None


measurements_per_year = defaultdict(list)


for measurement in data_obj:
    if measurement.skydekke is not None:
        year = measurement.dato[-4:]  # Hent år fra dato
        measurements_per_year[year].append(measurement.skydekke)

# Beregner antall penværsdager per år
penvaersdager_per_ar = {}
for year, skydekke_list in measurements_per_year.items():
    if len(skydekke_list) >= 300:  # Gyldig årskrav (minst 300 dager med data)
        valid_values = [sky for sky in skydekke_list if sky is not None]
        gjennomsnitt_skydekke = sum(valid_values) / len(valid_values) if valid_values else 0
        penvaersdager = sum(1 for sky in valid_values if sky <= 3)
        penvaersdager_per_ar[year] = penvaersdager

#Koden lager et diagram med antall penværsdager per år
plt.figure(figsize=(10, 6))
plt.bar(penvaersdager_per_ar.keys(), penvaersdager_per_ar.values(), color="skyblue")
plt.xlabel("År")
plt.ylabel("Antall penværsdager")
plt.title("Antall penværsdager per år")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"oppgave e"
    
#funksjon for å beregne plantens totale vekst
def beregn_plantevekst(temperaturliste):
    min_temperatur = 5
    vekstfaktor = 2  #dette tallet er hvor mye raskere planten vokser per grad over 5

    total_vekst = 0

    for temperatur in temperaturliste:
        if temperatur > min_temperatur:
            vekst = (temperatur - min_temperatur) * vekstfaktor
            total_vekst += vekst

    return total_vekst

# Funksjon for å beregne plantens vekst for hvert år
def beregn_vekst_for_hvert_ar(vearmalinger):
    vekst_for_hvert_ar = {}

    for vermaling in vearmalinger:
        try:
            aar = int(vermaling.dato.split(".")[2])

            if aar not in vekst_for_hvert_ar:
                vekst_for_hvert_ar[aar] = []

            # Fjern NaN-verdier altså verdier som mangler før den legger til temperatur i listen
            if vermaling.temperatur != '' and vermaling.temperatur != '-':
                # Erstatt komma med punktum og konverter til flyttall
                temperatur = float(vermaling.temperatur.replace(',', '.'))
                vekst_for_hvert_ar[aar].append(temperatur)
        except (ValueError, IndexError):
            continue
    
    #liste med gyldige år
    gyldige_aar = []
    #liste med vekstresultatene for hver år
    vekstresultater = []

    for aar, temperaturliste in vekst_for_hvert_ar.items():
        if len(temperaturliste) >= 300:  # Sjekker om det er data for mesteparten av året
            gyldige_aar.append(aar)
            total_vekst = beregn_plantevekst(temperaturliste)
            vekstresultater.append(total_vekst)

    return gyldige_aar, vekstresultater


#kaller på funksjonen og bregner plantens vekst for hvert år
gyldige_aar, vekstresultater = beregn_vekst_for_hvert_ar(data_obj)


#plotter resultatene
plt.figure()
plt.plot(gyldige_aar, vekstresultater, marker='o', color='green')
plt.xlabel('År')
plt.ylabel('Plantevekst')
plt.title('Plantevekst for hvert år')
plt.tight_layout()
plt.show()


"oppgave h"

import statistics

# Funksjonen for å beregne høyeste middelvind og medianvind for hvert år
def beregn_vinddata_for_hvert_ar(vearmalinger):
    vinddata_for_hvert_ar = {}

    for vermaling in vearmalinger:
        try:
            aar = int(vermaling.dato.split(".")[2])

            if aar not in vinddata_for_hvert_ar:
                vinddata_for_hvert_ar[aar] = {'vindhastigheter': []}

            # Fjern NaN-verdier altså manglende data før du legger til vindhastighet i listen
            if vermaling.vindhastighet != '' and vermaling.vindhastighet != '-':
                # Erstatt komma med punktum og konverter til flyttall
                vindhastighet = float(vermaling.vindhastighet.replace(',', '.'))
                vinddata_for_hvert_ar[aar]['vindhastigheter'].append(vindhastighet)
        except (ValueError, IndexError):
            continue

    #liste med gyldige år
    gyldige_aar = []
    #liste med høyeste middelvind for hver år
    hoyeste_middelvind = []
    #liste med medianvind for hvert år
    medianvind = []

    for aar, data in vinddata_for_hvert_ar.items():
        if len(data['vindhastigheter']) >= 300:  # Sjekker om det er data for vindhastighet for mesteparten av året
            gyldige_aar.append(aar)
            hoyeste_middelvind.append(max(data['vindhastigheter']))
            #bruker statitic for å finne medianen
            medianvind.append(statistics.median(data['vindhastigheter']))

    return gyldige_aar, hoyeste_middelvind, medianvind


# Beregner vinddata for hvert år
gyldige_aar_vind, hoyeste_middelvind, medianvind = beregn_vinddata_for_hvert_ar(data_obj)

# Plotter resultatene
plt.figure()

# Plotter høyeste middelvind
plt.plot(gyldige_aar_vind, hoyeste_middelvind, marker='o', color='blue', label='Høyeste Middelvind')

# Plotter medianvind
plt.plot(gyldige_aar_vind, medianvind, marker='o', color='orange', label='Medianvind')

plt.xlabel('År')
plt.ylabel('Vindhastighet')
plt.title('Høyeste Middelvind og Medianvind for hvert år')
plt.legend()
plt.tight_layout()
plt.show()