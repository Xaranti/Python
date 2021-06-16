dayType = 2
weekend = 1
workday = 2
holiday = 3

if dayType ==1:
    pass
elif dayType ==2:
    pass
else:
    print ("cos")

# skrócenie kodu (nie robić za często można się zgubić)
daydescritp = 'weekend' if dayType == 1 else 'workday' if dayType ==2 else 'Holiday'
print (daydescritp)
#lub
print ('weekend') if dayType ==1 else print('workday') if dayType == 2 else print ('Holiday')

#####LAB
price = 123
bonus = 23
bonus_granted = True

price = price-bonus if bonus_granted else price
print(price)