# Simulator
WIDTH  = 900 
HEIGHT = 900
MAX_FOOD_SUPPLY = 100
initialPreyPopulation = 30
initialPredatorPopulation = 10
INIT_VELOCITY = 10
FPS = 30

# Food
FoodCOLOR = (0, 255, 0, 100)
FoodSIZE = 5

# Predator
PredatorMAX_HEALTH   = 100
PredatorVIEW_RADIUS  = 200
PredatorMAX_VELOCITY = 15
PredatorSIZE = 15
PredatorCOLOR = (255, 0, 0, 100)
MAX_DETECTION_OF_PREY  = 10
MAX_ATTRACTION_TO_PREY = 10

# Prey
PreyMAX_HEALTH   = 100
PreyVIEW_RADIUS  = 200
PreyMAX_VELOCITY = 15
PreySIZE = 15
PreyCOLOR = (0, 0, 255, 100)
PreyMAX_DETECTION_OF_FOOD       = 10
PreyMAX_ATTRACTION_TO_FOOD      = 10
PreyMAX_DETECTION_OF_PREDATOR   = 10
PreyMAX_REPULSION_FROM_PREDATOR = 10

#Detection
maxForce = 1.5