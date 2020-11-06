import numpy as np
import math

# Position               => a tuple of 2D coordinates
# ListOfCounterCreatures => The list which is to be used to get creatures in the field of view
# Upperbound             => the field of view

def FilterUsingEuclideanDistances(Position, ListOfCounterCreatures, Upperbound):
    response = []

    for animal in ListOfCounterCreatures:
        x,y = animal.rect.centerx, animal.rect.centery
        distance = ((x-Position[0])**2 + (y-Position[1])**2)**(0.5)
        if distance < Upperbound:
            response.append((animal,(1 - distance/Upperbound)))

    return response

def PredictSafeDirection(Position, CreaturesAround, behaviourRate):
    if len(CreaturesAround)==0:
        return [0,0]

    refactoredVectorlist = []
    vectorlist = []

    for details in CreaturesAround:
        animal, factor = details
        refactoredVectorlist.append([factor*(animal.rect.x - Position[0]) ,factor*(animal.rect.y - Position[1])])
        vectorlist.append([(animal.rect.x - Position[0]) ,(animal.rect.y - Position[1])])

    vectors = np.array(vectorlist)
    refactoredVectors = np.array(refactoredVectorlist)
    resultant = np.sum(vectors, axis = 0)
    refactoredResultant = np.sum(refactoredVectors, axis = 0)

    # if len(vectors) == 0 or len(refactoredVectors == 0):
    #     print("Vector ki galti thi")
    #     return [0,0]
    if resultant[0] == 0:
        resX = 0
    else:
        resX = (behaviourRate*refactoredResultant[0])/resultant[0]
    if math.isnan(resX):
        resX = 0
    if resultant[1] == 0:
        resY = 0
    else:
        resY = (behaviourRate*refactoredResultant[1])/resultant[1]
    if math.isnan(resY):
        resY = 0

    response = [resX, resY]

    # if response:
    #     print(response)
    #     print(vectors)
    #     print(refactoredVectors)
    #     print("***********************")
    return response