#switch w pythonie nie istnieje, wiec trzeba to obejsc
def nazwatyg(daynumber):
    names = {
        0:'Pon',
        1:'Wt',
        2:'Sr',
        3:'Czw',
        4:'Pt',
        5:'Sob',
        6:'Niedz'
    }
    return names.get(daynumber,"error")#dla slownika names pobierz daynumber
    # jak nie ma to wyswietli error


print(nazwatyg(4))