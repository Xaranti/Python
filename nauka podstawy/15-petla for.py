persons = ['a','b','c','d']
domain = 'firma.com'

for person in persons:
    email = person+'@'+domain
    print(email)
###
data = ['Error:File cannot be open','Error:No free space on disk','Error:File missing','Warning:Internet connection lost','Error:Access denied']
for d in data:
    print(d.upper())

for d in data:
    x = d.split(':')
    print(x[0].upper())
    print(x[1])
##################
for number in range(1,21): #range(startowa liczba,koncowa,co ile skok)
    if number%2==0:
        print('Number %2d is %4s' % (number,'even'))
##############
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
for i in range(10):
    if i%2==0:
        print(string_A)
    else:
        print(string_B)
###########
for x in range(10):
    print ('x'*x)