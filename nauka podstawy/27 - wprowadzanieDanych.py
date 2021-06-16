x = input('podaj wartosc dla x') #bez definicji zmiennych zawsze widzi wpisane jako string

xint = input('podaj wartosc')
xint = int(xint)

while True:
    xstr = input ('dupa')
    if xstr.isdecimal():
        xstr = int(xstr)
        break



