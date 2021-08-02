brandOnSale = 'Opel'

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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSale):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSale
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSale,self.brand))
        else:
            print("Cannot change, sale valid only for {}".format(brandOnSale))
       
    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is availe in sale')


car_01 = Car('Seat','Ibiza',True,True,True,False)
car_02 = Car('Opel','Corsa',True,False,True,True)

'''
print("status of cars:", car_01.__GetIsOnSale(), car_02.__GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("status of cars:", car_01.GetIsOnSale(), car_02.GetIsOnSale())'''
car_01.IsOnSale=True
car_02.IsOnSale=True
print("status of cars:", car_01.IsOnSale, car_02.IsOnSale)