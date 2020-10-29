from creature import *
import constants
import utils

MAX_HEALTH   = constants.PredatorMAX_HEALTH
VIEW_RADIUS  = constants.PredatorVIEW_RADIUS
MAX_VELOCITY = constants.PredatorMAX_VELOCITY

SIZE = constants.PredatorSIZE
COLOR = constants.PredatorCOLOR

MAX_DETECTION_OF_PREY  = constants.MAX_DETECTION_OF_PREY
MAX_ATTRACTION_TO_PREY = constants.MAX_ATTRACTION_TO_PREY

class Predator(Creature):
    def __init__(self,creatureFields,detection,attraction):
        super(Predator,self).__init__(*creatureFields)
        self.detectionOfPrey = detection
        self.attractionOfPrey = attraction

    def detect(self, preys):
        creaturesAround = utils.FilterUsingEuclideanDistances((self.rect.x,self.rect.y), preys, self.fieldRadius)
        if len(creaturesAround) == 0:
            pass
        else:
            newDirection = utils.PredictSafeDirection((self.rect.x,self.rect.y), creaturesAround)
            self.changeDirection(newDirection)

    def details(self):
        if(self.alive):
            super().details("Predator")
            print(f"The Predator's detection capability is {self.detectionOfPrey}")
            print(f"The Predator's attraction capability is {self.attractionOfPrey}")
        else:
            print("The Predator is dead. Sorry :(")