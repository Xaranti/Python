number = 10
print (number,id(number))
number +=2
print (number,id(number))
text = 'Africa'
print(text, id(text))
text+= ' is hot'
print(text, id(text))

list=[1,2,3]
print(list,id(list))
list.append(4)
print(list,id(list))

list2 = list
print (list2, id(list2))

##LAB
days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days.copy()
workdays.remove('sat')
workdays.pop(5)
print (days)
print (workdays)