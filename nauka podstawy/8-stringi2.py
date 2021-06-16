drive = 'c:\\'
folder = 'scod\\pyrhon\\'
file = ' skrypt.py'
path = drive + folder + file
txt = " text with \nnewline" # po \n wrzuci reszte do nowej lini
text = r"text with \nnewline" # dzieki "r" wszystko potraktuje jako ciag znakow
firstname = "Kasia"
familyname = "Sowa"
lastname = "wilk"
newname = firstname+" "+familyname+" "+lastname
print (newname)
music = """Universal Fanfare" \n Jerry Goldsmith "Happy Together" \nGarry Bonner "I'm a Man" Steve Winwood"""
print (music)
#-------------------lekcja 3-------------------
number = '1000' # w nawiasie wiec to ciag znakow a nie cyfra
# numer + 1 wywali blad bo nie da sie dodac liczby do wyrazu
int(number)+1 # potraktuj "number" jako inta i dodaj 1
type(number) #wyswietli typ zmiennej
###############################
messgae = 'proccesing file %s'
print (messgae % ('file1.txt')) # %s oznacza ze co innego moze potem dokleic do pritna
mess1 = 'file %s has size %d KB' # %s dla stringow %d dla liczb
print (mess1 % ('kupka.txt',256))
# gdyby zrobic %20s to znaczy ze dla stringa s zarezerwowane bedzie 20 znakow
