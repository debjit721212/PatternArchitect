class house:
    def __init__(self):
        self.add_itemlist = []
    
    def add_item(self,item):
        self.add_itemlist.append(item)
    
    def __str__(self):
        return f"The house is made by {','.join(self.add_itemlist)}"

class HouseBuilder:
    def __init__(self):
        self.house = house()
    
    def build_walls(self,item):
        self.house.add_item(item=f"wall-> {item}")
        return self
    
    def build_window(self,item):
        self.house.add_item(item=f"window-> {item}")
        return self

    def build_door(self,item):
        self.house.add_item(item=f"door-> {item}")
        return self
    
    def build_garage(self,item):
        self.house.add_item(item=f"garage-> {item}")
        return self
    
    def build_garden(self,item):
        self.house.add_item(item=f"garden-> {item}")
        return self
    
    def build_roof(self,item):
        self.house.add_item(item=f"roof-> {item}")
        return self
    
    def build_pool(self,item):
        self.house.add_item(item=f"pool-> {item}")
        return self
    
    def build_floors(self,item):
        self.house.add_item(item=f"floor-> {item}")
        return self
            
def main():
    housebuilder = HouseBuilder()
    while True:
        print("\n--- 🏠 HouseBuilder Menu ---")
        print("1. add walls")
        print("2. add windows")
        print("3. add doors")
        print("4. add garage")
        print("5. add garden")
        print("6. add roof")
        print("7. add pool")
        print("8. add floors")
        print("9. finish & show house")
        print("0. exit")

        user_choice = input("Choose option: ")

        if user_choice == "1":
            wall = input("Which kind of wall? (brick/glass/wood): ")
            housebuilder.build_walls(wall)
        elif user_choice == "2":
            window = input("Which kind of window? (glass/wood/steel): ")
            housebuilder.build_window(window)
        elif user_choice == "3":
            door = input("Which kind of door? (glass/wood/steel): ")
            housebuilder.build_door(door)
        elif user_choice == "4":
            garage = input("Garage size? (big/medium/small): ")
            housebuilder.build_garage(garage)
        elif user_choice == "5":
            garden = input("Garden type? (flower/veg/mixed): ")
            housebuilder.build_garden(garden)
        elif user_choice == "6":
            roof = input("Which roof? (open/shaded/solar): ")
            housebuilder.build_roof(roof)
        elif user_choice == "7":
            pool = input("Pool location? (roof/beside garden/none): ")
            housebuilder.build_pool(pool)
        elif user_choice == "8":
            floor = input("Flooring type? (tile/wood/marble/stone): ")
            housebuilder.build_floors(floor)
        elif user_choice == "9":
            print("\n✅ Your Final House:")
            print(housebuilder.house)
        elif user_choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Please choose a valid option!")

if __name__=="__main__":
    main()
    
