class Car:
    carnumbers = 0
    ListOfCars = []
   
    def __init__(self, brand, model, isairbag, ispaint, ismechanic):
        self.brand = brand
        self.model = model
        self.isairbag = isairbag
        self.ispaint = ispaint
        self.ismechanic = ismechanic
        Car.carnumbers+=1
        Car.ListOfCars.append(self)
   
    def isdemaged(self):
        return not (self.ismechanic and self.ispaint and self.isairbag)
       
    def getinfo(self):
        print('{} {}'.format(self.brand,self.model).upper())
        print('AB - ok - {}'.format(self.isairbag))
        print('Paint - ok - {}'.format(self.ispaint))
        print('Mech - ok - {}'.format(self.ismechanic))
        print('-'*10)

print(Car.carnumbers,Car.ListOfCars)
       
car_01 = Car('Seat','Ibiza',True,True,True)
car_02 = Car('Opel','Corsa',True,False,True)
   
print(Car.carnumbers,Car.ListOfCars)
print(vars(car_02))
print(isinstance(car_02,Car))
print(type(car_02) is Car)
print(car_02.__class__)
print(dir(Car))
print(dir(car_02))