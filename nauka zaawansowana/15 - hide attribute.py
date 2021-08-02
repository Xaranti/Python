class Car:
    carnumbers = 0
    ListOfCars = []
   
    def __init__(self, brand, model, isairbag, ispaint, ismechanic, isOnSale):
        self.brand = brand
        self.model = model
        self.isairbag = isairbag
        self.ispaint = ispaint
        self.ismechanic = ismechanic
        self.__isOnSale = isOnSale
        Car.carnumbers+=1
        Car.ListOfCars.append(self)
   
    def isdemaged(self):
        return not (self.ismechanic and self.ispaint and self.isairbag)
       
    def getinfo(self):
        print('{} {}'.format(self.brand,self.model).upper())
        print('AB - ok - {}'.format(self.isairbag))
        print('Paint - ok - {}'.format(self.ispaint))
        print('Mech - ok - {}'.format(self.ismechanic))
        print('IS ON SALE - {}'.format(self.__isOnSale))
        print('-'*10)
       
car_01 = Car('Seat','Ibiza',True,True,True,False)
car_02 = Car('Opel','Corsa',True,False,True,True)

car_02.__isOnSale = False
car_02.YearOfProd = 2005 #dodanie atrybutu do klasy
#del car_02.YearOfProd - usunięcie dodanego atrybutu

setattr(car_02, "Taxi", False)
print(hasattr(car_02,'Taxi'))

car_02.getinfo()
print(vars(car_02))