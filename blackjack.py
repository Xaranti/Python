#BlackJack GAME
import random
#tworzenie talli kart
deck = []
kolors = [' pik',' karo',' kier',' trefl']
for nr in range(2,11):
    for kolor in kolors:
        karta = str(nr)+kolor
        deck.append(karta)
symbols = ['J','Q','K','A']
for symbol in symbols:
    for kolor in kolors:
        karta=symbol+kolor
        deck.append(karta)

# losowanie 2 kart krupiera
wylosowanaE1 = random.choice(deck)
deck.remove(wylosowanaE1)
wylosowanaE2 = random.choice(deck)
deck.remove(wylosowanaE2)
enemydeck = [wylosowanaE1,wylosowanaE2]

# liczenie wstepnej punktacji krupiera
pkte = 0
print ('Karty przeciwnika: \n',wylosowanaE1, ', karta zakryta')
if wylosowanaE1[0] == 'A':
    pkte = 11
elif wylosowanaE1[0] in symbols:
    pkte = 10
elif int(wylosowanaE1[0]) >=2:
    pkte = int(wylosowanaE1[0])
else:
    pkte = 10
print('Punkty przeciwnika: ',pkte,'+ ?')
# dobieranie kart gracza
twojakarta1 = random.choice(deck)
deck.remove(twojakarta1)
twojakarta2 = random.choice(deck)
deck.remove(twojakarta2)
reka = [twojakarta1,twojakarta2]
#liczenie punktów gracza
def liczenie():
    global pkt
    pkt = 0
    print ('Twoje karty: \n', reka)
    for x in range(0,len(reka)):
        if (reka[x])[0] == 'A':
            pkt += 11
        elif (reka[x])[0] in symbols:
            pkt += 10
        elif int((reka[x])[0]) >=2:
            pkt += int((reka[x])[0])
        else:
            pkt += 10
    print('Twoje pkt: ', pkt)
    if pkt>21:
        print("Przebiles 21, PRZEGRANA")
        quit()
    
   
liczenie()

#dobór kart gracza
wybor = ""
while wybor!= 'n':
    if wybor == 'y':
        twojakarta3 = random.choice(deck)
        deck.remove(twojakarta3)
        reka.append(twojakarta3)
        liczenie()
    wybor = input('Czy dobierasz karte? (y/n)')

#liczenie punktacji krupiera
if wylosowanaE2[0] == 'A':
    pkte += 11
elif wylosowanaE2[0] in symbols:
    pkte += 10
elif int(wylosowanaE2[0]) >=2:
    pkte += int(wylosowanaE2[0])
else:
    pkte += 10
   
#dobieranie kart przez krupiera + doliczanie ich do puli, w sumie mogłem to też zrobić jako funkcja
while pkte<=16:
    wylosowanaE3 = random.choice(deck)
    if wylosowanaE3[0] == 'A':
        pkte += 11
    elif wylosowanaE3[0] in symbols:
        pkte += 10
    elif int(wylosowanaE3[0]) >=2:
        pkte += int(wylosowanaE3[0])
    else:
        pkte += 10
    enemydeck.append(wylosowanaE3)
   
# wyświetlanie wyników
print ('Karty przeciwnika: \n',enemydeck)
if pkte>=22:
    print('Punkty przeciwnika: ',pkte)
    print ('Twoje karty: \n', reka)
    print('Twoje punkty: ',pkt)
    print('Przeciwnik przebil, Wygrales')
    quit()
print('Punkty przeciwnika: ',pkte)
print ('Twoje karty: \n', reka)
print('Twoje punkty: ',pkt)
print( 'Przegrales' if pkt>21 or pkt<pkte else 'Wygrales')