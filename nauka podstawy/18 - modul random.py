import random
print('one random number:', random.randint(1,100)) #zakres od 1 do 100 (1 i 100 wlacznie)
print('choosing random number from range',random.choice(range(1,100))) #dowolny zakres, tutaj 1-100, moze byc imiona,stringi etc, losowa wartosc z zakresu ogolem
print(random.randrange(1,100)) # to co wyzej w prostrzym zapisie
list = ['marek','monia','alex','wojtek']
random.shuffle(list) # lista dostaje losowa kolejnosc
print(random.random()) #losuje liczbe typu float w zakresie 0-1

x=0
counter=0
number1 = random.randint(1,100)
while x!=number1:
    x=random.randint(1,100)
    counter+=1
print(number1,x,counter)