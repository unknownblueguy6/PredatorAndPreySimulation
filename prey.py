from creature import *
import constants
import utils

MAX_HEALTH   = constants.PreyMAX_HEALTH
VIEW_RADIUS  = constants.PreyVIEW_RADIUS
MAX_VELOCITY = constants.PreyMAX_VELOCITY

SIZE = constants.PreySIZE
COLOR = constants.PreyCOLOR

HEALTH_GAIN = constants.PreyHEALTH_GAIN
HEALTH_LOSS = constants.PreyHEALTH_LOSS

MAX_DETECTION_OF_FOOD       = constants.MAX_DETECTION_OF_FOOD
MAX_ATTRACTION_TO_FOOD      = constants.MAX_ATTRACTION_TO_FOOD
MAX_DETECTION_OF_PREDATOR   = constants.MAX_DETECTION_OF_PREDATOR
MAX_REPULSION_FROM_PREDATOR = constants.MAX_REPULSION_FROM_PREDATOR

MUTATION_AMOUNT = constants.PreyMUTATION_AMOUNT

class Prey(Creature):
    def __init__(self,creatureFields,detectionOfFood,attractionToFood,detectionOfPredator,repulsionToPredator):
        super(Prey,self).__init__(*creatureFields)
        self.detectionOfFood = detectionOfFood
        self.attractionToFood = attractionToFood
        self.detectionOfPredator = detectionOfPredator
        self.repulsionToPredator = repulsionToPredator
        self.velocity.scale_to_length(self.maxVelocity)

    def getTarget(self, CounterCreatures, Food):
        FilteredFood, FilteredPredators = utils.FoodAndPredatorFilterUsingEuclideanDistances((self.rect.centerx,self.rect.centery), CounterCreatures, Food, self.fieldRadius)
        return utils.PredictPreyDirection((self.rect.centerx,self.rect.centery), FilteredPredators, FilteredFood, self.attractionToFood, self.repulsionToPredator)

    def move(self, width, height, CounterCreatures, Food):
        targetVelocity = self.getTarget(CounterCreatures, Food)

        if targetVelocity.magnitude() != 0:
            targetVelocity.scale_to_length(self.maxVelocity)
            steer = targetVelocity - self.velocity
            if steer.magnitude() > constants.maxForce:
                steer.scale_to_length(constants.maxForce)
        
            self.velocity = self.velocity + steer
        
        super().move(width, height)

    def details(self):
        if(self.alive):
            super().details("Prey")
            print(f"The Prey's detection of Food capability is {self.detectionOfFood}")
            print(f"The Prey's attraction to Food capability is {self.attractionToFood}")
            print(f"The Prey's detection of Predator capability is {self.detectionOfPredator}")
            print(f"The Prey's repulsion to Predator capability is {self.repulsionToPredator}")
        else:
            print("The Prey is dead. Sorry :(")
    
    def crossbreed(self, other):
        childDetectionOfFood     = (self.detectionOfFood  + other.detectionOfFood)  / 2
        childAttractionToFood    = (self.attractionToFood + other.attractionToFood) / 2
        childDetectionOfPredator = (self.detectionOfPredator  + other.detectionOfPredator) / 2
        childRepulsionToPredator = (self.repulsionToPredator  + other.repulsionToPredator) / 2
        return Prey(
            (
                MAX_HEALTH, 
                VIEW_RADIUS,
                MAX_VELOCITY,
                (random.randint(0, constants.WIDTH), random.randint(0, constants.HEIGHT)),
                (random.uniform(-1, 1) * constants.INIT_VELOCITY, random.uniform(-1, 1) * constants.INIT_VELOCITY),
                COLOR,
                SIZE,
            ),
            childDetectionOfFood,
            childAttractionToFood,
            childDetectionOfPredator,
            childRepulsionToPredator
        )
    def mutate(self):
        self.detectionOfFood     += random.uniform(-1, 1) * MUTATION_AMOUNT * MAX_DETECTION_OF_FOOD
        self.attractionToFood    += random.uniform(-1, 1) * MUTATION_AMOUNT * MAX_ATTRACTION_TO_FOOD
        self.detectionOfPredator += random.uniform(-1, 1) * MUTATION_AMOUNT * MAX_DETECTION_OF_PREDATOR
        self.repulsionToPredator += random.uniform(-1, 1) * MUTATION_AMOUNT * MAX_REPULSION_FROM_PREDATOR