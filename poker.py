import random
global pula
global enemy
global me
enemy = 500
me = 500
pula = 0

global deck
global table
global mydeck
global enemydeck
   
def createdeck():
    global deck
    global table
    global mydeck
    global talia    
    global enemydeck
    table = []
    deck = []
    enemydeck = []
    mydeck = []
    kolors = [' pik',' karo',' kier',' trefl']
    symbols = ['J','Q','K','A']
    cyfry = [2,3,4,5,6,7,8,9,10]
    talia = cyfry+symbols
    for nr in cyfry:
        for kolor in kolors:
            karta = str(nr)+kolor
            deck.append(karta)
   
    for symbol in symbols:
        for kolor in kolors:
            karta=symbol+kolor
            deck.append(karta)
   
    enemycard1 = random.choice(deck)
    deck.remove(enemycard1)
    enemycard2 = random.choice(deck)
    deck.remove(enemycard2)
    enemydeck = [enemycard1,enemycard2]
   
    mycard1 = random.choice(deck)
    deck.remove(mycard1)
    mycard2 = random.choice(deck)
    deck.remove(mycard2)
    mydeck = [mycard1,mycard2]
   
    for i in range(0,3):
        deckcard = random.choice(deck)
        deck.remove(deckcard)
        table.append(deckcard)
       
    print('Table: ', table)
    print('My cards:', mydeck)
   
def points():
    global table
    global enemydeck
    global wynik
    zestaw = enemydeck+table
    zestaw.sort()
    literki = []
    wynik = 0
    for karta1 in zestaw:
        literki.append(karta1[0])
    for karta2 in str(talia):
        x=literki.count(karta2)
        if x==2: #para lub 2 pary
            wynik+=1
            if wynik==3:
                wynik-=1
        if x==3: #trojka
            wynik=3
        if x==4: #kareta
            wynik=7
    if wynik==4: #full
        wynik=6
    pik=trefl=karo=kier=0
    for karta3 in zestaw:
        if karta3.endswith(' pik'):
            pik+=1
        elif karta3.endswith(' kier'):
            kier+=1
        elif karta3.endswith(' karo'):
            karo+=1
        elif karta3.endswith(' trefl'):
            trefl+=1
    if trefl>=5 or karo>=5 or pik>=5 or kier>=5:
            wynik=5 #kolor
    stritlist = []
    for literka in literki:
        if literka.isnumeric():
            stritlist.append(int(literka))
        elif literka=='J':
                stritlist.append(11)
        elif literka=='Q':
                stritlist.append(12)
        elif literka=='K':
                stritlist.append(13)
        elif literka=='A':
                stritlist.append(14)
    if 1 in stritlist:
        stritlist.remove(1)
        stritlist.append(int(10))
    stritlist = list(dict.fromkeys(stritlist))
    stritlist.sort()
    for strit in range(0,len(stritlist)-4):
        if stritlist[strit]==stritlist[strit+1]-1==stritlist[strit+2]-2==stritlist[strit+3]-3==stritlist[strit+4]-4:
            wynik = 4


def statusgry():
    global raised
    global status1
    global pula
    global me
    global enemy
    global mydeck
    while len(table)<5:
        if status1 == "koniec":
            print("wygrales")
            me += pula
            pula =0
            print("Nowa partia")
            points()
            gra()
            statusgry() ###tutaj trzeba rozpoczac partie od nowa
        elif status1 == "raise":
            sprawdzasz = input("Sprawdzasz? (y/n)")
            if sprawdzasz=='n':
                print("You passed")
                enemy+=pula
                pula=0
                quit()
            else:
                me-=raised
                pula+=raised
                status1 = "check"
                statusgry()
           
        else:
            print ("Check, kolejna karta na stół")
            deckcard = random.choice(deck)
            deck.remove(deckcard)
            table.append(deckcard)
            # print('Enemy cards:', enemydeck)
            print('Table: ', table)
            print('My cards:', mydeck)        
            points()
            gra()
    else:
        print('koniec parti')
        pointsmoje()
        podsumuj()

def gra():
    global raised
    global pula
    global me
    global enemy
    print('Pula: ', pula)
    print('Stan konta: ',me," Stan konta przeciwnika: ",enemy)
    stawka = int(input("Ile chcesz postawić? Stan: "))
    pula += int(stawka)
    me -=int(stawka)
    global status1
    status1 = ""
    bluff = random.randint(1,100)
    if bluff>75:
        raised = random.randint(1,5)*10
        print('Enemy raise by ',raised)
        pula += raised
        enemy -= raised
        status1 = 'raise'
        statusgry()    
    else:
        if stawka<=50 and wynik<=2:
            print('Enemy Check')
            pula += int(stawka)
            enemy -= int(stawka)
            statusgry()
        elif stawka>50 and wynik<=2:
            los = random.randint(1,100)
            print(los)
            if los<25:
                print("Enemy Pass")
                status1 = "koniec"
                statusgry()
            else:
                print('Enemy Check')
                pula += int(stawka)
                enemy -= int(stawka)
                statusgry()
        elif stawka<=50 and wynik>2:
            los = random.randint(1,100)
            print(los)
            if los<25:
                print('Enemy Check')
                pula += int(stawka)
                enemy -= int(stawka)
                statusgry()
            else:
                raised = random.randint(1,5)*10
                print('Enemy raise by ',raised)
                pula += raised
                enemy -= raised
                status1 = 'raise'
                statusgry()
       
       
def pointsmoje():
    global wynikmoj
    zestaw1 = mydeck+table
    zestaw1.sort()
    literki1 = []
    wynikmoj = 0
    for karta1 in zestaw1:
        literki1.append(karta1[0])
    for karta2 in str(talia):
        x=literki1.count(karta2)
        if x==2: #para lub 2 pary
            wynikmoj+=1
            if wynikmoj==3:
                wynikmoj-=1
        if x==3: #trojka
            wynikmoj=3
        if x==4: #kareta
            wynikmoj=7
    if wynikmoj==4: #full
        wynikmoj=6
    pik=trefl=karo=kier=0
    for karta3 in zestaw1:
        if karta3.endswith(' pik'):
            pik+=1
        elif karta3.endswith(' kier'):
            kier+=1
        elif karta3.endswith(' karo'):
            karo+=1
        elif karta3.endswith(' trefl'):
            trefl+=1
    if trefl>=5 or karo>=5 or pik>=5 or kier>=5:
            wynikmoj=5 #kolor
    stritlist = []
    for literka in literki1:
        if literka.isnumeric():
            stritlist.append(int(literka))
        elif literka=='J':
                stritlist.append(11)
        elif literka=='Q':
                stritlist.append(12)
        elif literka=='K':
                stritlist.append(13)
        elif literka=='A':
                stritlist.append(14)
    if 1 in stritlist:
        stritlist.remove(1)
        stritlist.append(int(10))
    stritlist = list(dict.fromkeys(stritlist))
    stritlist.sort()
    for strit in range(0,len(stritlist)-4):
        if stritlist[strit]==stritlist[strit+1]-1==stritlist[strit+2]-2==stritlist[strit+3]-3==stritlist[strit+4]-4:
            wynikmoj = 4      
       

def podsumuj():
    global pula
    global enemy
    global me
    print("Przeciwnik ma:")
    print('Enemy cards:', enemydeck)
    print("Parę" if wynik==1 else "2 Pary" if wynik==2 else "Trójka" if wynik==3 else "Strit" if wynik==4 else "Kolor" if wynik==5 else "FUll" if wynik==6 else "Kareta" if wynik==7 else "High Card")
    print('Table: ', table)
    print('My cards:', mydeck)
    print("Ty masz: ")
    print("Parę" if wynikmoj==1 else "2 Pary" if wynikmoj==2 else "Trójka" if wynikmoj==3 else "Strit" if wynikmoj==4 else "Kolor" if wynikmoj==5 else "FUll" if wynikmoj==6 else "Kareta" if wynikmoj==7 else "High Card")

    if wynikmoj>wynik:
        print('wygrales')
        me+=pula
        pula=0
    elif wynikmoj==wynik:
        print('DRAW')
        me+=pula/2
        enemy+=pula/2
        pula=0
    else:
        print("Przegrales")
        enemy+=pula
        pula=0
       
    newOne = input("Kolejne rozdanie? (y/n)")

    if newOne == 'y':
        createdeck()
        points()
        pula +=20
        enemy-=20
        me-=20
        gra()
    else:
        quit()
           

createdeck()
points()
pula +=20
enemy-=20
me-=20
gra()