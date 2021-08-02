import csv
import types

def exportToFile_Static(path,header,data):
    with open(path,mode="w") as file:
        writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('>>> This function exportToFile - static method')

def exportToFile_Class(cls,path):
    with open(path,mode="w") as file:
        writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        for c in cls.ListOfCars:
            writer.writerow([c.brand,c.model,c.IsOnSale])
    print('>>> This function exportToFile - class method')

def exportToFile_Instance(self,path):
    with open(path,mode="w") as file:
        writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        writer.writerow([self.brand,self.model,self.IsOnSale])
    print('>>> This function exportToFile - instance method')

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

print('Static-----'*10)
Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r'C:\pyt\export_statis.csv',['Brand','Model','IsOnSale'],[car_01.brand,car_01.model,car_01.IsOnSale])
Car.ExportToFile_Static(r'C:\pyt\export_statis.csv',['Brand','Model','IsOnSale'],[car_01.brand,car_01.model,car_01.IsOnSale])
print(dir(Car))

print('Class-----'*10)
#Car.ExportToFile_Class = exportToFile_Class
Car.ExportToFile_Class = types.MethodType(exportToFile_Class,Car)
Car.ExportToFile_Class(path=r'C:\pyt\export_class.csv')

print('Instance-----'*10)
#Car.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance,car_01)
car_01.ExportToFile_Instance(path=r'C:\pyt\export_instance.csv')