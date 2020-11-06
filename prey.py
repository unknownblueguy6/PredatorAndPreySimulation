from creature import *
import constants
import utils

MAX_HEALTH   = constants.PreyMAX_HEALTH
VIEW_RADIUS  = constants.PreyVIEW_RADIUS
MAX_VELOCITY = constants.PreyMAX_VELOCITY

SIZE = constants.PreySIZE
COLOR = constants.PreyCOLOR

MAX_DETECTION_OF_FOOD       = constants.PreyMAX_DETECTION_OF_FOOD
MAX_ATTRACTION_TO_FOOD      = constants.PreyMAX_ATTRACTION_TO_FOOD
MAX_DETECTION_OF_PREDATOR   = constants.PreyMAX_DETECTION_OF_PREDATOR
MAX_REPULSION_FROM_PREDATOR = constants.PreyMAX_REPULSION_FROM_PREDATOR

class Prey(Creature):
    def __init__(self,creatureFields,detectionOfFood,attractionToFood,detectionOfPredator,repulsionToPredator):
        super(Prey,self).__init__(*creatureFields)
        self.detectionOfFood = detectionOfFood
        self.attractionToFood = attractionToFood
        self.detectionOfPredator = detectionOfPredator
        self.repulsionToPredator = repulsionToPredator

    def detect(self, CounterCreatures):
        FilteredList = utils.FilterUsingEuclideanDistances((self.rect.centerx,self.rect.centery) ,CounterCreatures ,self.fieldRadius)
        response = utils.PredictSafeDirection((self.rect.centerx,self.rect.centery) ,FilteredList, self.repulsionToPredator)
        return response

    def details(self):
        if(self.alive):
            super().details("Prey")
            print(f"The Prey's detection of Food capability is {self.detectionOfFood}")
            print(f"The Prey's attraction to Food capability is {self.attractionToFood}")
            print(f"The Prey's detection of Predator capability is {self.detectionOfPredator}")
            print(f"The Prey's repulsion to Predator capability is {self.repulsionToPredator}")
        else:
            print("The Prey is dead. Sorry :(")