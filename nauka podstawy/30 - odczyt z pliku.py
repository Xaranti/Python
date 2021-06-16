#sposoby na dzialania, 3 najlepszy
file = open("C:\\Users\\Xaranti\\Desktop\\IT\\x.txt","r") #r bo do odczytu
content = file.read() # wczytuje caly plik na raz
print(content)
file.close()

with open('C:\\Users\\Xaranti\\Desktop\\IT\\x.txt','r') as file:
    content = file.read()
    print(content)

with open('C:\\Users\\Xaranti\\Desktop\\IT\\x.txt','r') as file:
    for line in file: # wczytuje liniami
        print(line)

file = open("C:\\Users\\Xaranti\\Desktop\\IT\\x.txt","r")
fragment =  file.read(10) #wczytanie po 10 bajtow, jak nie bedzie czego czytac sie wylaczy
while fragment:
    print(file.tell(),fragment) #file.tell informuje na jakiej ilosci bajtow jestesmy
    fragment = file.read(10)
file.close()