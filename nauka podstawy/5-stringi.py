text='This is a text.'
text.endswith('ext') # false bo jest kropka na koncu
text.islower() #false bo duze T
text.upper() #zmienia na duze
text.upper().isupper # true bo najpierw zwiekszamy litery
text.find('is',3) # szuka wyrazenia is od 3 znaku
text.replace('a',4) # błąd bo nie da sie zastapic strina intem
text.replace('a','4') # teraz zadziała
text.split(' ')
innytext = '1000'
innytext.isdigit() # true bo sa tam liczby
innytext.isdecimal()
innytext.isalpha() # czy som same literki
