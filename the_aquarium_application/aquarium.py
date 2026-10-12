from fish import Fish
from plant import Plant

class Aquarium:
    def __init__(self):
        self.fish = []
        self.plants = []

    def add_fish(self, fish):
        self.fish.append(fish)

    def add_plant(self, plant):
        self.plants.append(plant)

    def get_fish(self):
        return self.fish

    def get_plants(self):
        return self.plants

    def get_creature_number(self):
        return len(self.fish) + len(self.plants)

    def get_hungry_creature_number(self):
        hungry_fish = [fish for fish in self.fish if fish.is_hungry()]
        hungry_plants = [plant for plant in self.plants if plant.is_hungry()]
        return len(hungry_fish) + len(hungry_plants)

    def food_levels(self):
        fishes = self.get_fish()
        plants = self.get_plants()
        for fish in fishes:
            if fish.is_hungry():
                print(f"{fish.name} is hungry.")
            else:
                print(f"{fish.name} is not hungry.")
        for plant in plants:
            if plant.is_hungry():
                print(f"{plant.name} is hungry.")
            else:
                print(f"{plant.name} is not hungry.")

    def feed_tank(self, food):
        food = food / self.get_hungry_creature_number()
        for fish in self.fish:
            if fish.is_hungry():
                print(fish.eat(food))
        for plant in self.plants:
            if plant.is_hungry():
                print(plant.eat(food))
    

aquarium = Aquarium()

aquarium.add_fish(Fish("Nemo", 12))
aquarium.add_fish(Fish("Dory", 5))
aquarium.add_plant(Plant("Seaweed", 2))
aquarium.add_plant(Plant("Kelp", 6))
aquarium.food_levels()

print("--- Feeding the tank ---")
aquarium.feed_tank(51)

print("--- After feeding ---")
aquarium.food_levels()