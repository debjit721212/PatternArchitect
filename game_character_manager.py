from abc import ABC,abstractmethod


class Base(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def create_characters(self):
        pass
    
class Character:
    def __init__(self,name):
        self.name = name
    
    
class CharacterCreation(Base):
    _characters={}
    
    @classmethod
    def create_characters(cls,name):
        if name not in cls._characters:
            cls._characters[name] = Character(name=name)
        return cls._characters[name]
    @classmethod
    def show(cls):
        for name in cls._characters.keys():
            print("Name -----> ",name)
    

class Game:
    def __init__(self):
        self.character_creator = CharacterCreation()
        self.army = {}
    
    def createArmy(self,name,character_type, image, hit_points, abilities):
        character = CharacterCreation.create_characters(name=name)
        print("character ", character.name)
        if character_type not in self.army:
            self.army[character_type]= [character.name,character_type, image, hit_points, abilities]
    
    def showArmy(self,character_type):
        if character_type in self.army:
            print(self.army[character_type])
        
            
            
            
# a = CharacterCreation()
# a.create_characters("Alex")
# a.create_characters("Bob")
# a.create_characters("Alex")  # should not recreate
# a.show()
# print(id(a.create_characters("Alex")))
# print(id(a.create_characters("Alex")))

if __name__ == "__main__":
    game = Game()
    game.createArmy(name="Indian Fource",character_type="Airforce",image=None,hit_points=150,abilities="attack")
    game.showArmy("Airforce")
    
    