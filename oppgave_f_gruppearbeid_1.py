

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

liste = [0, 0, 0, 0, 0, 0, 5, 56, 7, 8, 9, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0]
result = min_funk(liste)
print(result)

