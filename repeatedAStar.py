import forwardAStar

def repeatedAStar(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates, sizeOfGrid):
    plannedPaths = []
    knowledgeMazes = []

    currentKnowledgeMaze = knowledgeMaze
    beginning = beginningCoordinates
    ending = endingCoordinates
    while True:
        #planning
        knowledgeMazes.append(currentKnowledgeMaze)
        currentPath = forwardAStar.forwardAStar(knowledgeMaze, beginning, ending, sizeOfGrid)
        plannedPaths.append(currentPath)
        #execute
        #step through planned path
        #if current node is actually an obstacle, stop there and save that coordinate as the beginning coordinate for next iteration
        #if current node is the end node, stop there and return all needed info
        #otherwise, look at neighbors of the current node and see if they are obstacles in true maze. if so, plot these obstacles in the knowledge maze and insert updated knowledge maze
        for index, w in enumerate(currentPath):
            if trueMaze[w.coordinates[0]][w.coordinates[1]] == 1:
                #update beginning to coordinates right before obstacle bump
                beginning = currentPath[index-1].coordinates
                break
            if w.coordinates == endingCoordinates:
                return [plannedPaths,knowledgeMazes]
            neighbors = []
            currentCoordinate = currentPath[index].coordinates
            neighbors.append(generateLeftCoordinates(currentCoordinate))
            neighbors.append(generateRightCoordinates(currentCoordinate))
            neighbors.append(generateUpCoordinates(currentCoordinate))
            neighbors.append(generateDownCoordinates(currentCoordinate))
            for neighbor in neighbors:
                if isValidCoordinate(neighbor, sizeOfGrid):
                    if trueMaze[neighbor[0]][neighbor[1]] == 1:
                        currentKnowledgeMaze[neighbor[0]][neighbor[1]] = 1 
                        knowledgeMazes.append(currentKnowledgeMaze)




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

    
    
    
