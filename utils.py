import numpy as np

# Position               => a tuple of 2D coordinates
# ListOfCounterCreatures => The list which is to be used to get creatures in the field of view
# Upperbound             => the field of view

def FilterUsingEuclideanDistances(Position, ListOfCounterCreatures, Upperbound):
    response = []

    for animal in ListOfCounterCreatures:
        x,y = animal.position
        # x,y = animal #:: Testing
        distance = ((x-Position[0])**2 + (y-Position[1])**2)**(0.5)
        if distance < Upperbound:
            response.append(animal)

    return response
