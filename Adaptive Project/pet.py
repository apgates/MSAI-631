class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.energy = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 10
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):
        self.energy += 20

    def mood(self):
        if self.happiness > 70:
            return f"{self.name} is very happy!"
        elif self.happiness < 30:
            return f"{self.name} is feeling sad."
        else:
            return f"{self.name} is doing okay."
