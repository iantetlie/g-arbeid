# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:48:27 2023

@author: benja
"""



def trend_data(x_liste, y_liste):
    x_snitt = sum(x_liste)/len(x_liste) 
    y_snitt = sum(y_liste)/len(x_liste)
    sum_teller = 0.0
    sum_nevner = 0.0
    
    for i in range(len(x_liste)):
        sum_teller += (x_liste[i]-x_snitt)*(y_liste[i]-y_snitt)
        sum_nevner += (x_liste[i]-x_snitt)**2
        
    a = sum_teller/sum_nevner
    b = y_snitt - a * x_snitt
        
    return a, b



temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)
print(f'temperaturer_tidspunkter: {temperaturer_tidspunkter}')

print(trend_data(temperaturer_tidspunkter, temperaturer))





    
