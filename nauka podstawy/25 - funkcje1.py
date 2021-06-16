def doaction(action, *parameter):#gwiazdka oznacza ze parametr przyjmuje wiecej wartosci (jako tuple)
    print(action)
    print(parameter)
    return

doaction('buy','shoes','socks') #podaje 2 wartosci dla 1 parametru "parametr"

def doaction2(action,what, **parameter): #teraz parameteer stal sie slownikiem
    print(action)
    print(what)
    print(parameter) #wyswietlanie all w lini
    for element in parameter:
        print(element,'=',parameter[element]) #wyswietlanie pod soba
    return

doaction2('buy','shoes',size=45,color='red',type='sport')