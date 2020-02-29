import forwardAStar
import numpy as np
def repeatedAStar(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates, sizeOfGrid, console, backwards):
    plannedPaths = []
    knowledgeMazes = []
    totalNumberExpanded = 0

    currentKnowledgeMaze = knowledgeMaze
    beginning = beginningCoordinates
    ending = endingCoordinates
    while True:
        #planning
        knowledgeMazes.append(currentKnowledgeMaze)
        currentPath,_ = forwardAStar.forwardAStar(currentKnowledgeMaze, beginning, ending, sizeOfGrid, console, backwards)
        _,numberOfExpandedNodes = forwardAStar.forwardAStar(currentKnowledgeMaze, beginning, ending, sizeOfGrid, console, backwards)
        totalNumberExpanded = totalNumberExpanded + numberOfExpandedNodes

        # print(currentPath)
        if(console):
            print("current path")
            print(currentPath)
        plannedPaths.append(currentPath)
        if currentPath == []:
            return [[], knowledgeMazes]
        #execute
        #step through planned path
        #if current node is actually an obstacle, stop there and save that coordinate as the beginning coordinate for next iteration
        #if current node is the end node, stop there and return all needed info
        #otherwise, look at neighbors of the current node and see if they are obstacles in true maze. if so, plot these obstacles in the knowledge maze and insert updated knowledge maze
        currentKnowledgeMaze = np.copy(knowledgeMazes[-1])

        print("path found")
        print(currentPath)
        print("number expanded nodes this iteration:")
        print(numberOfExpandedNodes)
        print()

        for index, w in enumerate(currentPath):
            if trueMaze[w[0]][w[1]] == 1:
                #update beginning to coordinates right before obstacle bump
                if backwards:
                    ending = currentPath[index-1]
                else:
                    beginning = currentPath[index-1]
                break
            if w == (sizeOfGrid-1,sizeOfGrid-1): #if the path executed actually makes it to the end, we're done
                return [plannedPaths,knowledgeMazes], totalNumberExpanded
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
def repeatedAStarAdaptive(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates, sizeOfGrid, console):
    plannedPaths = []
    knowledgeMazes = []
    totalNumberExpanded = 0
    closedList = []
    goalDistance = 0
    currentKnowledgeMaze = knowledgeMaze
    beginning = beginningCoordinates
    ending = endingCoordinates
    while True:
        #planning
        knowledgeMazes.append(currentKnowledgeMaze)
        currentPath,numberOfExpandedNodes,closedList,goalDistance = forwardAStar.forwardAStarAdaptive(currentKnowledgeMaze, beginning, ending, sizeOfGrid, console,closedList, goalDistance)
        print("Goal distance: ", goalDistance)
        totalNumberExpanded = totalNumberExpanded + numberOfExpandedNodes

        # print(currentPath)
        if(console):
            print("current path")
            print(currentPath)
        plannedPaths.append(currentPath)
        if currentPath == []:
            return [[], knowledgeMazes]
        #execute
        #step through planned path
        #if current node is actually an obstacle, stop there and save that coordinate as the beginning coordinate for next iteration
        #if current node is the end node, stop there and return all needed info
        #otherwise, look at neighbors of the current node and see if they are obstacles in true maze. if so, plot these obstacles in the knowledge maze and insert updated knowledge maze
        currentKnowledgeMaze = np.copy(knowledgeMazes[-1])

        print("path found")
        print(currentPath)
        print("number expanded nodes this iteration:")
        print(numberOfExpandedNodes)
        print()

        for index, w in enumerate(currentPath):
            if trueMaze[w[0]][w[1]] == 1:
                #update beginning to coordinates right before obstacle bump
                beginning = currentPath[index-1]
                break
            if w == (sizeOfGrid-1,sizeOfGrid-1): #if the path executed actually makes it to the end, we're done
                return [plannedPaths,knowledgeMazes], totalNumberExpanded
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
