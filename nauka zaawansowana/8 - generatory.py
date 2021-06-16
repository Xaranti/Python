list1 = range(0,6)
list2 = range(0,6)

list3 = []
for a in list1:
    for b in list2:
        list3.append((a,b))
print(list3)

list4 = [(a,b) for a in list1 for b in list2]
print(list4)

list5 = [(a,b) for a in list1 for b in list2 if a%2==1 and b%2==0]
print(list5)

slownik = {a:b for a in list1 for b in list2 if a%2==1 and b%2==0}
print(slownik)

gen = ((a,b) for a in list1 for b in list2 if a%2==1 and b%2==0)
print(gen)

print(next(gen))
print(next(gen))

for x in gen: #kolejna peta for nic nie wyswietli bo w generatorze sie wszystko skonczyli
    print(x)
print('*'*20)
gen = ((a,b) for a in list1 for b in list2 if a%2==1 and b%2==0)
while True:
    try:
     print(next(gen))
    except StopIteration:
        print('all values has been printed')
        break