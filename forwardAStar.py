from Node import Node
import heapq
def forwardAStar(maze, beginningCoordinates, endingCoordinates):
    openList = [] #heap
    closedList = []
    hValue = (endingCoordinates[0] - beginningCoordinates[0]) + (endingCoordinates[1] - beginningCoordinates[1])
    beginningNode = Node(beginningCoordinates, None, 0, hValue)
    openList.append(beginningNode)

    while()


    plannedPath = []


    return plannedPath