from Node import Node
import heapq
def forwardAStar(maze, beginningCoordinates, endingCoordinates):
    openList = [] #heap
    closedList = []
    beginningNode = Node(beginningCoordinates, None, 0, getManhattanDistance(beginningCoordinates, endingCoordinates))
    openList.append(beginningNode)
    print("first item on open list: ")
    print(openList[0].coordinates)

    while openList[0].coordinates != endingCoordinates: #while first priority node isnt the goal node
        poppedNode = heapq.heappop(openList) #remove first priority from open list and add to closed list and expand it
        closedList.append(poppedNode)
        #expand the popped node
        potentialCoordinates = []
        potentialCoordinates.append(generateLeftCoordinates(poppedNode.coordinates))
        potentialCoordinates.append(generateRightCoordinates(poppedNode.coordinates))
        potentialCoordinates.append(generateUpCoordinates(poppedNode.coordinates))
        potentialCoordinates.append(generateDownCoordinates(poppedNode.coordinates))
        for coordinate in potentialCoordinates:
            if isValidCoordinate(coordinate):
                print("is Valid")
                print(inClosed(coordinate, closedList))
                print(inOpen(coordinate,closedList))
                #if the neighbor has valid coordinates and is not in closed list or in the open list, add that node in the open list
                if not(inClosed(coordinate, closedList)) and inOpen(coordinate, openList) == -1:
                    print("is not in closed or open")
                    heapq.heappush(openList, Node(coordinate, poppedNode, poppedNode.gvalue + 1, getManhattanDistance(coordinate, endingCoordinates)))
                #if the neighbor has valid cooridnates and is not in closed list but is in open list
                elif not(inClosed(coordinate, closedList)) and inOpen(coordinate, openList) != -1:
                    #check if current distance can be improved
                    if openList[inOpen(coordinate, openList)].fvalue > (poppedNode.gvalue + 1 + getManhattanDistance(coordinate, endingCoordinates)):
                        #change fvalue, g value, h value, change parent
                        openList[inOpen(coordinate, openList)].gvalue = poppedNode.gvalue + 1 
                        openList[inOpen(coordinate, openList)].hvalue = getManhattanDistance(coordinate, endingCoordinates)
                        openList[inOpen(coordinate, openList)].fvalue = poppedNode.gvalue + 1 + getManhattanDistance(coordinate, endingCoordinates)
                        openList[inOpen(coordinate, openList)].parent = poppedNode
        print("next item on open list: ")
        print(openList[0].coordinates)
    plannedPath = []
    goalNode = heapq.heappop(openList)
    currentNode = goalNode
    while currentNode !=  None:
        plannedPath.append(currentNode.coordinates)
        currentNode = currentNode.parent
    #return planned path
    return plannedPath
def generateLeftCoordinates(currentCoordinates):
    return (currentCoordinates[0]-1, currentCoordinates[1])
def generateRightCoordinates(currentCoordinates):
    return (currentCoordinates[0]+1, currentCoordinates[1])
def generateUpCoordinates(currentCoordinates):
    return (currentCoordinates[0], currentCoordinates[1]+1)
def generateDownCoordinates(currentCoordinates):
    return (currentCoordinates[0], currentCoordinates[1]-1)

def getManhattanDistance(currentCoordinates, endingCoordinates):
    return (endingCoordinates[0] - currentCoordinates[0]) + (endingCoordinates[1] - currentCoordinates[1])

def isValidCoordinate(currentCoordinates):
    return 0<=currentCoordinates[0]<=49 and 0<=currentCoordinates[1]<=49 and currentCoordinates != 1

def inClosed(currentCoordinates, closedList):
    for node in closedList:
        if node.coordinates == currentCoordinates:
            return True

    return False

def inOpen(currentCoordinates, openList):
    for index, w in enumerate(openList):
        if w.coordinates == currentCoordinates:
            return index

    return -1
