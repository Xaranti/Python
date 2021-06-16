import os

fileIsOk = False

while not fileIsOk:
    filename = input ('podaj sciezke pliku: ')
    if os.path.isfile(filename):
        fileIsOk = True
    

    ############# inna metoda
while True:
    filename = input ('podaj sciezke pliku: ')
    if os.path.isfile(filename):
        break
    else:
        print ('zle podana sciezkax')