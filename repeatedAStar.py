import forwardAStar


def repeatedAStar(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates):
    plannedPaths = []
    beginning = beginningCoordinates
    ending = endingCoordinates
    while(true):
        #planning
        currentPath = forwardAStar.forwardAStar(knowledgeMaze, beginning, ending)
        plannedPaths.append(currentPath)
        #execute
        #for each node in current path, step through and create updated knowledge maze
        #if fails, update beginning coordinates
        #call a star again with updated values
        #if finishes, break




    
    
    
    plannedPaths = []
    knowledgeMazes = []
