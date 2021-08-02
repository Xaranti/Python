brandOnSale = 'Opel'

class Car:
   
    def __init__(self, brand, model, isairbag, ispaint, ismechanic, isOnSale):
        self.brand = brand
        self.model = model
        self.isairbag = isairbag
        self.ispaint = ispaint
        self.ismechanic = ismechanic
        self.__isOnSale = isOnSale

    def __GetIsOnSale(self):
        return self.__isOnSale

    @property   
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSale):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSale
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSale,self.brand))
        else:
            print("Cannot change, sale valid only for {}".format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {} ".format(self.brand,self.model).title() 

car_01 = Car('Seat','Ibiza',True,True,True,False)

print(car_01.IsOnSale)
car_01.IsOnSale=True
del car_01.IsOnSale
print(car_01.IsOnSale)
print(car_01.CarTitle)
