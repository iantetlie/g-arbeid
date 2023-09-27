def min_funk(liste):
    teller= 0
    max_teller=0  
    
    for tall in liste:
        if tall == 0:
            teller += 1
        else:
            teller = 0
        if teller > max_teller:
            max_teller = teller
    return max_teller

liste = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
result = min_funk(liste)
print(f"den lengste perioden uten regn er {result} dager")


