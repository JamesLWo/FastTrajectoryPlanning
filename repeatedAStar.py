import forwardAStar
import numpy as np
def repeatedAStar(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates, sizeOfGrid):
    plannedPaths = []
    knowledgeMazes = []
    numberOfExpandedNodes = 0

    currentKnowledgeMaze = knowledgeMaze
    beginning = beginningCoordinates
    ending = endingCoordinates
    while True:
        #planning
        knowledgeMazes.append(currentKnowledgeMaze)
        currentPath = forwardAStar.forwardAStar(currentKnowledgeMaze, beginning, ending, sizeOfGrid, numberOfExpandedNodes)
        print("current path")
        print(currentPath)
        plannedPaths.append(currentPath)
        if currentPath == []:
            return [plannedPaths, knowledgeMazes]
        #execute
        #step through planned path
        #if current node is actually an obstacle, stop there and save that coordinate as the beginning coordinate for next iteration
        #if current node is the end node, stop there and return all needed info
        #otherwise, look at neighbors of the current node and see if they are obstacles in true maze. if so, plot these obstacles in the knowledge maze and insert updated knowledge maze
        currentKnowledgeMaze = np.copy(knowledgeMazes[-1])

        for index, w in enumerate(currentPath):
            if trueMaze[w[0]][w[1]] == 1:
                #update beginning to coordinates right before obstacle bump
                beginning = currentPath[index-1]
                break
            if w == endingCoordinates: #if the path executed actually makes it to the end, we're done
                return [plannedPaths,knowledgeMazes]
            neighbors = [] #generate all neighbors
            currentCoordinate = currentPath[index]
            neighbors.append(generateLeftCoordinates(currentCoordinate))
            neighbors.append(generateRightCoordinates(currentCoordinate))
            neighbors.append(generateUpCoordinates(currentCoordinate))
            neighbors.append(generateDownCoordinates(currentCoordinate))
            #check if each neighbor is valid and is an obstacle --> if it is, update the knowledge maze
            for neighbor in neighbors:
                if isValidCoordinate(neighbor, sizeOfGrid) and trueMaze[neighbor[0]][neighbor[1]] == 1:
                    currentKnowledgeMaze[neighbor[0]][neighbor[1]] = 1 #without assigning 1, it is an infinite loop?
            



def generateLeftCoordinates(currentCoordinates):
    return (currentCoordinates[0]-1, currentCoordinates[1])
def generateRightCoordinates(currentCoordinates):
    return (currentCoordinates[0]+1, currentCoordinates[1])
def generateUpCoordinates(currentCoordinates):
    return (currentCoordinates[0], currentCoordinates[1]+1)
def generateDownCoordinates(currentCoordinates):
    return (currentCoordinates[0], currentCoordinates[1]-1)


def isValidCoordinate(currentCoordinates, sizeOfGrid):
    return 0<=currentCoordinates[0]<=sizeOfGrid-1 and 0<=currentCoordinates[1]<=sizeOfGrid-1

    
    
    
