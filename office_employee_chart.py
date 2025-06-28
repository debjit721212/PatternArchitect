from abc import ABC,abstractmethod


class OfficeEmployeeEntity(ABC):
    @abstractmethod
    def show(self):
        pass
    
    @abstractmethod
    def removeEmp(self):
        pass


class Emplyee(OfficeEmployeeEntity):
    def __init__(self,name,degicnation):
        super().__init__()
        self.name = name
        self.degicnation = degicnation
        
    
    def show(self,interval=0):
        print(" "*interval,self.name," ------> ",self.degicnation)
    
    
    def removeEmp(self, name):
        for child in self.childed[:]:  # iterate over a copy
            if isinstance(child, Emplyee) and child.name == name:
                self.childed.remove(child)
                print(f"✅ Removed {name} from {self.name}")
            elif isinstance(child, OfficeTeam):
                child.removeEmp(name)


class OfficeTeam(OfficeEmployeeEntity):
    def __init__(self,name):
        super().__init__()
        self.childed = []
        self.name = name
        
    
    
    def add(self,component):
        self.childed.append(component)
        
    def show(self,interval=0):
        print(" "*interval,self.name)
        for child in self.childed:
            child.show(interval+1)
        
    def removeEmp(self, name):
        for child in self.childed[:]:  # iterate over a copy
            if isinstance(child, Emplyee) and child.name == name:
                self.childed.remove(child)
                print(f"✅ Removed {name} from {self.name}")
            elif isinstance(child, OfficeTeam):
                child.removeEmp(name)
    def count(self):
        total = 0
        for child in self.childed:
            if isinstance(child, OfficeTeam):
                total += child.count()
            else:
                total += 1
        return total
        
                
root = OfficeTeam("CEO")
managment = OfficeTeam("Managment")
vision = OfficeTeam("vision")

emp1 = Emplyee("Humba","Software lead Engineer")
emp2 = Emplyee("Hola","Senior Software Engineer")
emp3 = Emplyee("Ram","Senior Manager")

managment.add(emp1)
vision.add(emp2)
managment.add(emp3)

root.add(managment)
root.add(vision)


# Test
root.show()
print("\nTotal employees:", root.count())

print("\n--- Removing 'Ram' ---")
root.removeEmp("Ram")

print("\nUpdated Org Chart:")
root.show()
print("\nUpdated count:", root.count())
    