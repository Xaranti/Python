panstwa = ['FR','GB','ES']
panstwa[1] = 'GB'
panstwa.append('PL')
panstwa.insert(2,'DE')
panstwa.remove('FR')
panstwa.sort()
panstwa.reverse()
print(panstwa.pop[2]) #zwraca wartosc i usuwa z lsity
print(panstwa.index('PL')) # zwraca na ktorym miejscu jest wartsosc
print(panstwa.count('PL')) #ile razy na liscie
newlist = ['FI','SE']
panstwa.extend(newlist) #dodaje liste newlist do panstw
#panstwa.clear czysci liste
x=panstwa.copy # kopiuje lsite pod nowa zmienna

