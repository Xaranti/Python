liders={'PL':'Duda','US':'Trump'}
print(liders['US'])
liders['DE'] = 'Merkel' #dodawanie
print(liders.keys()) #klucze (pl,us,de)
print(liders.values()) #Duda,trump,merkel
print(liders.items()) # calosci

print(liders.popitem()) # jak w listach, wyrzuca na ekan i usuwa
print(liders.setdefault('FR','Macron')) #wyrzuc wartosc dla FR, 
#jezeli jej nie ma to wrzycuc Marcon i dodaj pozycje do slownika

print(liders.get('RU'))

newliders = {'RU':'Putin','DE':'Schulz'}
liders.update(newliders) # nowe wartości są dodane
# a jeżeli powtórzył się klucz to przypisana do niego jest nowa wartość


print(liders.pop('PL'))
print(liders)
