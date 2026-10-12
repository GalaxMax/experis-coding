class Plant:
    def __init__(self, name, hunger_level):
        self.name = name
        self.hunger_level = hunger_level

    def is_hungry(self):
        return self.hunger_level < 15

    def eat(self, food):
        self.hunger_level += (food * 0.5)
        return f"{self.name} is eating {food} units of food, and absorbs {food * 0.5} units of nutrients."