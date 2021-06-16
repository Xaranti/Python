import random
for i in range (32,127): #generator tablicy asci
  print(i,chr(i))

#generator hasla

password = ""
dlugosc = 8
for i in range(0,dlugosc):
  password+=(chr(random.randint(33,127)))
print (password)