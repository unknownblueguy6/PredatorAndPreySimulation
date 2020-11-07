from creature import *
import constants
import utils

MAX_HEALTH   = constants.PredatorMAX_HEALTH
VIEW_RADIUS  = constants.PredatorVIEW_RADIUS
MAX_VELOCITY = constants.PredatorMAX_VELOCITY

SIZE = constants.PredatorSIZE
COLOR = constants.PredatorCOLOR

HEALTH_GAIN = constants.PredatorHEALTH_GAIN
HEALTH_LOSS = constants.PredatorHEALTH_LOSS

MAX_DETECTION_OF_PREY  = constants.MAX_DETECTION_OF_PREY
MAX_ATTRACTION_TO_PREY = constants.MAX_ATTRACTION_TO_PREY

class Predator(Creature):
    def __init__(self,creatureFields,detection,attraction):
        super(Predator,self).__init__(*creatureFields)
        self.detectionOfPrey = detection
        self.attractionOfPrey = attraction
        self.velocity.scale_to_length(self.maxVelocity)

    def getTarget(self, CounterCreatures):
        FilteredPrey = utils.PreyFilterUsingEuclideanDistances((self.rect.centerx,self.rect.centery) ,CounterCreatures ,self.fieldRadius)
        return utils.PredictPredatorDirection((self.rect.centerx,self.rect.centery) ,FilteredPrey, self.attractionOfPrey)

    def move(self, width, height, CounterCreatures):
        targetVelocity = self.getTarget(CounterCreatures)

        if targetVelocity.magnitude() != 0:
            targetVelocity.scale_to_length(self.maxVelocity)
            steer = targetVelocity - self.velocity
            if steer.magnitude() > constants.maxForce:
                steer.scale_to_length(constants.maxForce)
        
            self.velocity = self.velocity + steer
        
        super().move(width, height);

    def details(self):
        if(self.alive):
            super().details("Predator")
            print(f"The Predator's detection capability is {self.detectionOfPrey}")
            print(f"The Predator's attraction capability is {self.attractionOfPrey}")
        else:
            print("The Predator is dead. Sorry :(")