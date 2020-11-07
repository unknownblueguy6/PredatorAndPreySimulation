import numpy as np
import pygame
import math
import predator

# Position               => a tuple of 2D coordinates
# ListOfCounterCreatures => The list which is to be used to get creatures in the field of view
# Upperbound             => the field of view

def PreyFilterUsingEuclideanDistances(Position, ListOfCounterCreatures, Upperbound):
    response = []
    
    for animal in ListOfCounterCreatures:
        x,y = animal.rect.centerx, animal.rect.centery
        distance = ((x-Position[0])**2 + (y-Position[1])**2)**(0.5)
        if distance < Upperbound:
            if distance != 0:
                response.append((animal,(1/distance)))
            else:
                response.append((animal, float('inf')))

    return response

def PredictPredatorDirection(Position, CreaturesAround, behaviourRate):
    if len(CreaturesAround)==0:
        return pygame.math.Vector2(0, 0)

    desiredVelocitylist = []

    for details in CreaturesAround:
        animal, factor = details
        desiredVelocitylist.append([behaviourRate*factor*(animal.rect.x - Position[0]) , behaviourRate*factor*(animal.rect.y - Position[1])])

    desiredVelocities = np.array(desiredVelocitylist)
    resultant = np.sum(desiredVelocities, axis = 0)
    resultantVector2 = pygame.math.Vector2(resultant[0], resultant[1])
    
    target = CreaturesAround[0][0]
    maxFactor = CreaturesAround[0][1]
    for vel, details in zip(desiredVelocities, CreaturesAround):
        animal, factor = details
        currVector = pygame.math.Vector2(vel[0], vel[1])
        if abs(resultantVector2.angle_to(currVector)) <= 45 and maxFactor < factor:
            maxFactor = factor
            target = animal   

    desired = (pygame.math.Vector2(target.rect.x, target.rect.y) - pygame.math.Vector2(Position))*behaviourRate
    return desired

def FoodAndPredatorFilterUsingEuclideanDistances(Position, ListOfCounterCreatures, ListOfFood, Upperbound):
    preds = []
    foods = []

    for creature in ListOfCounterCreatures:
        x,y = creature.rect.centerx, creature.rect.centery
        distance = ((x-Position[0])**2 + (y-Position[1])**2)**(0.5)
        if distance < Upperbound:
            if distance != 0:
                preds.append((creature, (1/distance)))
            else:
                preds.append((creature, float('inf')))
    
    for food in ListOfFood:
        x, y = food.x, food.y
        distance = ((x-Position[0])**2 + (y-Position[1])**2)**(0.5)
        if distance < Upperbound:
            if distance != 0:
                foods.append((food,(1/distance)))
            else:
                foods.append((food, float('inf')))
    
    return foods, preds

def PredictPreyDirection(Position, CreaturesAround, FoodAround, foodBehaviour, creatureBehaviour):
    if len(CreaturesAround) == 0 and len(FoodAround) == 0:
        return pygame.math.Vector2(0, 0)

    desiredVelocityCreaturelist = [[0,0]]
    for details in CreaturesAround:
        animal, factor = details
        desiredVelocityCreaturelist.append([creatureBehaviour*factor*(animal.rect.x - Position[0]) , creatureBehaviour*factor*(animal.rect.y - Position[1])])
    
    desiredVelocityFoodlist = [[0, 0]]
    for details in FoodAround:
        food, factor = details
        desiredVelocityFoodlist.append([foodBehaviour*factor*(food.x - Position[0]), foodBehaviour*factor*(food.y - Position[1])])

    desiredVelocitiesCreature = np.array(desiredVelocityCreaturelist)
    desiredVelocitiesFood = np.array(desiredVelocityFoodlist)
    resultant1 = np.sum(desiredVelocitiesCreature, axis = 0)
    resultant2 = np.sum(desiredVelocitiesFood, axis = 0)

    resultantVector2 = pygame.math.Vector2(resultant1[0] + resultant2[0], resultant1[1] + resultant2[1])

    if(len(CreaturesAround) != 0):
        target = CreaturesAround[0][0]
        maxFactor = CreaturesAround[0][1]
    else:
        target = FoodAround[0][0]
        maxFactor = FoodAround[0][1]

    for vel, details in zip(desiredVelocitiesCreature, CreaturesAround):
        animal, factor = details
        currVector = pygame.math.Vector2(vel[0], vel[1])
        if abs(resultantVector2.angle_to(currVector)) <= 45 and maxFactor < factor:
            maxFactor = factor
            target = animal
    
    for vel, details in zip(desiredVelocitiesFood, FoodAround):
        food, factor = details
        currVector = pygame.math.Vector2(vel[0], vel[1])
        if abs(resultantVector2.angle_to(currVector)) <= 45 and maxFactor < factor:
            maxFactor = factor
            target = food

    if type(target) == predator.Predator:
        return (pygame.math.Vector2(target.rect.x, target.rect.y) - pygame.math.Vector2(Position))*creatureBehaviour
    
    else:
        return (pygame.math.Vector2(target.x, target.y) - pygame.math.Vector2(Position))*foodBehaviour