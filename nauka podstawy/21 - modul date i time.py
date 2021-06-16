import datetime
print(datetime.MINYEAR, datetime.MAXYEAR) # zakres lat na ktorych mozna dzialac
roznica = datetime.timedelta(days=1,hours=2,minutes=30)
print(roznica)
today = (datetime.date.today()) # today is
daystopay = datetime.timedelta(days=7)
print("zaplac rachunki w ciagu", daystopay.days,'days')
print('zaplac rachunki do ',today+daystopay)
endofworld = datetime.date.max #max data pythona
print(endofworld.weekday()) # jaki to bedzie dzien wzgledem lini wyzej
###
borndate = datetime.date(1993,10,12)
print(today-borndate)

################
print('now',datetime.datetime.now())
print('today',datetime.datetime.today())
print('utcnow',datetime.datetime.utcnow())
print('weekday',datetime.datetime.today().weekday())
####### konwersja czasu do napisu
print('%a',datetime.datetime.now().strftime('%a')) #skrocony dzien tyg
print('%A',datetime.datetime.now().strftime('%A')) # pelny dzien tyg
print('%w',datetime.datetime.now().strftime('%w')) #nr dnia tyg
print(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))
#year,month,day,hour,minut,sec,milisec----------------^