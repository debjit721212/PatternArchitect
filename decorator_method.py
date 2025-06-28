from abc import ABC,abstractmethod

class Coffe(ABC):
    
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    

class SimpleCoffe(Coffe):
    def __init__(self):
        super().__init__()
    
    def cost(self):
        return 2
    
    def description(self):
        return "This is very basic coffe"


class CoffeDecorator(Coffe):
    def __init__(self,coffe:Coffe):
        self._coffe = coffe
    
    def cost(self):
        return self._coffe.cost()
    
    def description(self):
        return self._coffe.description()
    

class MilkwithCoffe(Coffe):
    def __init__(self,coffe:Coffe,type_of_milk:str ="whole milk",milk_amount_ml: int = 50):
        # super().__init__(coffe)
        self._coffe = coffe
        self.type_of_milk = type_of_milk
        self.milk_amount_ml = milk_amount_ml
    
    def cost(self):
        return self._coffe.cost() +2
    def description(self):
        return f"IN this coffe you have {self.type_of_milk} and the amount is {self.milk_amount_ml} ml"
    
    
coffe_cup = SimpleCoffe()
print(coffe_cup.description())

condense_milk_coffe = MilkwithCoffe(coffe_cup,"condence milk")

print(condense_milk_coffe.cost())
print(condense_milk_coffe.description())
        
    
    