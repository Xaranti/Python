import os
import time

print("current directory: ", os.getcwd())

currentDir = os.getcwd()
filename = 'result.txt'
fullpath = os.path.join(currentDir,filename)
print ('Full path to file is: ', fullpath)

relativepath = 'output.txt'
print ("absolut path is: ", os.path.abspath(relativepath))

filepath = r'c:\temp\results.txt'
print ("File name is: ", os.path.basename(filepath)) #wyswietlanie nazwy pliku na podstawie sciezki
print("Directory is: ",os.path.dirname(filepath)) #wyswietalnie lokalicacji

print( "do file exist? ", os.path.exists(filepath))

if os.path.exists(filepath):
    print ("last modify date is: ", os.path.getmtime(filepath))
    print ("last mofify date is: ", time.localtime(os.path.getmtime(filepath)))
    #1 wywali z dupy wartosc od poczatku kompow
    #2 bedzie w miare ok

rozmiar = os.path.getsize(filepath) #rozmiar w bajtach

