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

def PredictSafeDirection(Position, CreaturesAround, InitialVelocity):
    '''
    Changes the Direction to the net resultant of the pos vectors of all visible predators 
    '''
    vectorlist = []

    for animal in CreaturesAround:
        # vectorlist.append([animal.position[0] - Position[0] , animal.position[1] - Position[1]])
        vectorlist.append([animal[0] - Position[0] , animal[1] - Position[1]]) # :: Testing
    
    vectors = np.array(vectorlist)
    resultant = np.sum(vectors, axis = 0)

    resultant *= -1

    return resultant.tolist()


ans = PredictSafeDirection((0,0),[(1,1)],0)

print(ans)