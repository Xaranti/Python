import sys
try:
    #tutaj calosc kodu etc, jak cos sie wywali to odapal sie except
    x = input("podaj wyraz: ")
    y = int(x) #nie da sie zrobic wyrazu na inta wiec wywali blad
    print (10/x)
#except:
#    print ('sorki, miala byc liczba')
#mozna zrobic tez dokladniej
except ValueError as e: 
    print ("podales zla wartosc", e) #to e wyrzuci wiecej danych
except ZeroDivisionError:
    print ('nie da sie dzielic przez 0', sys.exc_info()[0]) #tutaj dokladne dane o bledzie

#mozna tez zrobic ze jak instrukcja ladnie przejdzie to wtedy else
else:
    print('wszystko ladnie podane')

#tutaj instrukcja beda wykonane i przy bledach i bez bledow
finally:
    print('skonczylismy instrukcje')