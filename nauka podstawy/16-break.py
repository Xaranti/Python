for liczba in range (2,31):
    isprime = True
    for x in range(2,liczba):
        if liczba%x==0:
            isprime=False
            print(liczba, 'nie jest liczba pierwsza')
            break
    if isprime:
        print('%d to liczba pierwsza' % (liczba))
#####################
for liczba in range (2,31):
    for x in range(2,liczba):
        if liczba%x==0:
            isprime=False
            print(liczba, 'nie jest liczba pierwsza')
            break
    else: #!!!! ELSE NIE BEDZIE WYKONYWANE JEZELI PETLA ZOSTALA PRZERWANA PRZEZ BREAK
        print('%d to liczba pierwsza' % (liczba))