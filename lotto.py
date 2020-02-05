import random

game = "tak";
given = []

while game == "tak":
    for l in range(6):

        while 1==1:
            give = int(input("Podaj liczbę (" + str(l+1) + "): "))
            if give < 1 or give > 49:
                print("Podaj liczbę z przedziału 1 - 49.")
            elif give in given:
                print("Już podałeś taką liczbę, podaj inną.")
            else:
                break
            
        given.append(give)
            
    draw = random.sample(range(1,50),6)
    hit = 0

    for i in draw:
        for j in given:
            if i == j:
                hit = hit+1

    print("Skreślone: "+str(given))
    print("Wylosowane: "+str(draw))

    if hit < 3:
        print("Przegrałeś.")
    else:
        print("Wygrałeś: "+str(hit)+".")

    given.clear()
    draw.clear()

    game = input("Chcesz zagrać jeszcze raz? (tak/nie): ")
