i=1
while i<5:
    print(i)
    print(i**2)
    print(i**3)
    i+=1
else:
    print('pyklo')
###############################
value = [10,43,12,48,12,11,18,98,57,28,19,27,49]
i=0
max = len(value)
while i<max-2:
    print(i,value[i])
    if value[i+1]>value[i] and value[i+2]>value[i+1]:
        print('Kolejne liczby rosnace z listy to: ',value[i], value[i+1], value[i+2])
    i+=1
################################
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
boxcap = 90
box = []
i = 0
while i<len(cargo) and (boxcap - sum(box) >= min(cargo)):
    if (boxcap - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print ('W boxie jest ', sum(box))
print(box)