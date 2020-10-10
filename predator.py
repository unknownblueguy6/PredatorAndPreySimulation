from creature import *

MAX_HEALTH   = 100
VIEW_RADIUS  = 20
MAX_VELOCITY = 15

SIZE = 15
COLOR = (255, 0, 0, 100)

MAX_DETECTION_OF_PREY  = 10
MAX_ATTRACTION_TO_PREY = 10

class Predator(Creature):
    def __init__(self,creatureFields,detection,attraction):
        super(Predator,self).__init__(*creatureFields)
        self.detectionOfPrey = detection
        self.attractionOfPrey = attraction
    def details(self):
        if(self.alive):
            super().details("Predator")
            print(f"The Predator's detection capability is {self.detectionOfPrey}")
            print(f"The Predator's attraction capability is {self.attractionOfPrey}")
        else:
            print("The Predator is dead. Sorry :(")