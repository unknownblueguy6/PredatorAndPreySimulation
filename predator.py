from creature import *

PREDATOR_SIZE = 20
PREDATOR_COLOR = (255, 0, 0, 100)

class Predator(Creature):
    def __init__(self,creatureFields,detection,attraction):
        super(Predator,self).__init__(self,creatureFields)
        self.detectionOfPrey = detection
        self.attractionOfPrey = attraction
    def details(self):
        if(self.alive):
            print(f"The Creatures max health is {self.maxHealth}")
            print(f"The Creatures field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The Creatures max velocity is {self.maxVelocity}")
            print(f"The Predator's detection capability is {self.detectionOfPrey}")
            print(f"The Predator's attraction capability is {self.attractionOfPrey}")
        else:
            print("The Creature is dead. Sorry :(")