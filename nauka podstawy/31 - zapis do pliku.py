filename = 'C:\\Users\\Xaranti\\Desktop\\IT\\x.txt'
line = 'Europe'
cities = ['Londyn','Paryz','Gorzow','Tulce','Madrit']

file = open(filename,'w') #w bo write (do zapisu), #a bedzie dodawac do pliku zamiast nadpisywac
#w+ to zapis + odczyt, a+ to zapis+odczyt bez nadpisywania
file.write(line)
file.write("\n")
file.writelines(cities) #wrzuci wszystko w 1 lini
file.close()

for city in cities:
    file.write(city+'\n') #linijkami wrzuci