list1 = range(1,6)
list2 = range(1,6)

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