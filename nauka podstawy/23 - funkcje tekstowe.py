line = 'this IS a very STRANGE text'
line. capitalize() #1 litera bedzie duza
line.title() # kazda 1 litera bedzie duza
line.upper() #obvious
line.lower() # to tez
line.swapcase() #zamienia duze z malymi i na odwrot
line.casefold() #nie rozumiem
line.replace('IS','WAS')
line.count('e') # ile razy wystepuje "e"
line.find('e') # pozycja litery e
line.rfind('e') # pozycja litery e od prawej
line.index('e')
line.rindex('e')
line.startswith('this') #true/false
line.endswith('text')

import string
string.ascii_letters
string.digits
list = line.split(' ') # dzieli
' '.join(list) # laczy