nummer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_nummer = int(input("Skriv inn et tall:"))

def teller():
    count = 0
    for num in nummer:
        if num >= input_nummer:
            count += 1
            print("input_nummer:", num)
    
    print()
    print("Antall tall større/lik enn:", count)

teller()

