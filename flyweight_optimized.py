
from dataclasses import dataclass
import weakref

# 🔹 Step 1: Immutable Character (Flyweight) with __slots__ via dataclass
@dataclass(frozen=True)
class Character:
    __slots__ = ("name", "hit_points", "abilities", "image")
    name: str
    hit_points: int
    abilities: str
    image: str = None


# 🔹 Step 2: Flyweight Factory using WeakValueDictionary
class CharacterFactory:
    _pool = weakref.WeakValueDictionary()

    @classmethod
    def get_character(cls, name, hit_points=100, abilities="defence", image=None):
        key = (name, hit_points, abilities, image)
        if key not in cls._pool:
            cls._pool[key] = Character(*key)
        return cls._pool[key]


# 🔹 Step 3: Game manages extrinsic state (e.g., unit type, position, context)
class Game:
    def __init__(self):
        self.army = {}

    def create_army(self, name, character_type, image=None, hit_points=100, abilities="defence"):
        character = CharacterFactory.get_character(name, hit_points, abilities, image)
        print(f"Character created: {character.name} (ID: {id(character)})")
        if character_type not in self.army:
            self.army[character_type] = [character]
        else:
            self.army[character_type].append(character)

    def show_army(self, character_type):
        if character_type in self.army:
            for char in self.army[character_type]:
                print(f"{character_type} -> {char.name}, HP: {char.hit_points}, Abilities: {char.abilities}")
