from creature import *

MAX_HEALTH   = 100
VIEW_RADIUS  = 20
MAX_VELOCITY = 15

SIZE = 15
COLOR = (0, 0, 255, 100)

MAX_DETECTION_OF_FOOD       = 10
MAX_ATTRACTION_TO_FOOD      = 10
MAX_DETECTION_OF_PREDATOR   = 10
MAX_REPULSION_FROM_PREDATOR = 10

class Prey(Creature):
    def __init__(self,creatureFields,detectionOfFood,attractionToFood,detectionOfPredator,repulsionToPredator):
        super(Prey,self).__init__(*creatureFields)
        self.detectionOfFood = detectionOfFood
        self.attractionToFood = attractionToFood
        self.detectionOfPredator = detectionOfPredator
        self.repulsionToPredator = repulsionToPredator
    def details(self):
        if(self.alive):
            super().details("Prey")
            print(f"The Prey's detection of Food capability is {self.detectionOfFood}")
            print(f"The Prey's attraction to Food capability is {self.attractionToFood}")
            print(f"The Prey's detection of Predator capability is {self.detectionOfPredator}")
            print(f"The Prey's repulsion to Predator capability is {self.repulsionToPredator}")
        else:
            print("The Prey is dead. Sorry :(")