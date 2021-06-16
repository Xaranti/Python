import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

import calendar
print(calendar.month(2017,9,w=5,l=2)) #to i ponizsze generuje kalendarz
print(calendar.month(2017,9))
print(calendar.weekday(2017,9,29)) # 29.09.2017 to ktory dzien tugodnia
calendar.setfirstweekday(6) # niedziela bedzie traktowana jako 1 dzien tygodnia
calendar.isleap(2020) #czy rok przestemny true/false
calendar.leapdays(2017,2021) #ile jest dni przestepnych w latach 
print(calendar.calendar(2021)) # generuje kalendarz na caly rok