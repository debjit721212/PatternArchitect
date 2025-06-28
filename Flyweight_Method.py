from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def numberOfSit(self):
        pass 
    


def singletone(cls):
    _instance = {}
    def wraper(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return wraper

@singletone
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.car_dict = {}
    
    def add_car(self,name,price,numsit):
        if name not in self.car_dict:
            self.car_dict[name]=(name,price,numsit)
        else:
            print("Already added no require")
            
    def cost(self,name):
        if name in self.car_dict:
            return self.car_dict[name][1]
        else:
            print("Car model is not exits")
    
    def numberOfSit(self,name):
        if name in self.car_dict:
            return self.car_dict[name][2]
        else:
            print("Car model is not exits")
    
    def show_car_list(self):
        for key, val in self.car_dict.items():
            print("LIST IS -------> ", val)
    
    def display(self, name, license_plate):
        if name in self.car_dict:
            data = self.car_dict[name]
            print(f"License: {license_plate} → {data[0]} | ₹{data[1]}, Seats: {data[2]}")
        else:
            print("Car model does not exist")
    
    
def main():
    
    cars_dict = {}
    car_list = [("Audi",100000,4),("Maruti Suzuki",50000,5),("Tata",900000,4),("Honda",4000000,4),("Mahindra",66666666,2)]
    car_class = Car()
    for car in car_list:
        cars_dict[car[0]]=car_class.add_car(*car)
    car_class.show_car_list()
    car_class.display("Audi", "DL-8CAF-1234")  # DL-8CAF-1234 → Audi | ₹100000, Seats: 4


        
        
if __name__=="__main__":
    main()
    
        