from creature import *

PREY_SIZE = 20
PREY_COLOR = (0, 0, 255, 100)

class Prey(Creature):
    def __init__(self,creatureFields,detectionOfFood,attractionToFood,detectionOfPredator,repulsionToPredator):
        super(Prey,self).__init__(self,creatureFields)
        self.detectionOfFood = detectionOfFood
        self.attractionToFood = attractionToFood
        self.detectionOfPredator = detectionOfPredator
        self.repulsionToPredator = repulsionToPredator
    def details(self):
        if(self.alive):
            print(f"The Creatures max health is {self.maxHealth}")
            print(f"The Creatures field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The Creatures max velocity is {self.maxVelocity}")
            print(f"The Prey's detection of Food capability is {self.detectionOfFood}")
            print(f"The Prey's attraction to Food capability is {self.attractionToFood}")
            print(f"The Prey's detection of Predator capability is {self.detectionOfPredator}")
            print(f"The Prey's repulsion to Predator capability is {self.repulsionToPredator}")
        else:
            print("The Creature is dead. Sorry :(")