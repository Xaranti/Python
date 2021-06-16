def giveworkingdays(year,month,day): #mozna zrobic (year,month,day=1) i jezeli nie podam dnia to domyslnie bedzie 1, 
    # ale jzeli podam przy wywołaniu funkcji to wezmia podana ilosc
    from datetime import date
    from datetime import timedelta
    from time import time
    day= date(year,month,day)
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print(day, workingday)
    return workingday #zostanie zwrocona wyliczona 

x = giveworkingdays(2021,6,12) #przypisanie wartosci do zmiennej

print (giveworkingdays(2021,6,19)) #wyswietlenie wartosci funkcji bez zmiennej(dla parametrow podanych w funkcji)

giveworkingdays(2021,2,17)
giveworkingdays(2016,10,10)
giveworkingdays(day=6,month=12,year=2021) # mozna ustalic kolejnosc podajac parametr