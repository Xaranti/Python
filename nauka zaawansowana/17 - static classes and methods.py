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

    @classmethod
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM*0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW*1.36

lineOfText = 'Renault:Megane:True:True:False:False'
car_03=Car.ReadFromText(lineOfText)
car_03.getinfo()

print('converting 120km to KW',car_03.Convert_KM_KW(120))
print('converting 90kw to KM',car_03.Convert_KW_KM(90))

print(car_03.getinfo())

