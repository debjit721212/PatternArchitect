from abc import ABC , abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class CharacterPrototype(Prototype):
    def __init__(self,name, health, mana, attack_power, defense):
        super().__init__()
        self.name = name
        self.health = health
        self.mana = mana
        self.attack_power = attack_power
        self.defense = defense
    
    
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"The character name is {self.name}, it's health is {self.health},attack power is {self.attack_power}, sefensiveness is {self.defense}"

# Subclass:Mage 
class Mage(CharacterPrototype):
    def __init__(self, name):
        super().__init__(name, health=150, mana=10, attack_power=500, defense=12)

# Subclass: Knight
class Knight(CharacterPrototype):
    def __init__(self, name):
        super().__init__(name, health=120, mana=30, attack_power=70, defense=90)

# Subclass: Elf
class Elf(CharacterPrototype):
    def __init__(self, name):
        super().__init__(name, health=80, mana=100, attack_power=100, defense=50)


# Clone + Modify Function
def clone_and_customize(prototype: CharacterPrototype):
    clone = prototype.clone()
    print("\nDo you want to customize this character? (yes/no)")
    if input().strip().lower() == "yes":
        print("Which attribute do you want to change?")
        print("1. Name\n2. Health\n3. Mana\n4. Attack Power\n5. Defense")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            clone.name = input("Enter new name: ")
        elif choice == "2":
            clone.health = int(input("New health: "))
        elif choice == "3":
            clone.mana = int(input("New mana: "))
        elif choice == "4":
            clone.attack_power = int(input("New attack power: "))
        elif choice == "5":
            clone.defense = int(input("New defense: "))

    print("\n✅ Your Cloned Character:")
    print(clone)
        
        
def main():
    characters = {
        "1": Mage("Gandalf"),
        "2": Knight("Lancelot"),
        "3": Elf("Legolas")
    }

    print("--- Character Prototype Cloner ---")
    print("1. Mage\n2. Knight\n3. Elf")
    choice = input("Choose a base character to clone (1-3): ").strip()

    if choice in characters:
        print("\n👤 Original Character:")
        print(characters[choice])
        clone_and_customize(characters[choice])
    else:
        print("Invalid choice.")   

if __name__ == "__main__":
    main()
        