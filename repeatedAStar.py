import forwardAStar

def repeatedAStar(knowledgeMaze, trueMaze, beginningCoordinates, endingCoordinates, sizeOfGrid):
    #plannedPaths = []
    #knowledgeMazes = []

    #currentKnowledgeMaze = knowledgeMaze
    #beginning = beginningCoordinates
    #ending = endingCoordinates
    #while True:
        #planning
        #knowledgeMazes.append(currentKnowledgeMaze)
        #currentPath = forwardAStar.forwardAStar(knowledgeMaze, beginning, ending)
        #plannedPaths.append(currentPath)
        #execute
        #for each node in current path, step through and create updated knowledge maze
        #if fails, update beginning coordinates
        #call a star again with updated values
        #if finishes, break
    return forwardAStar.forwardAStar(knowledgeMaze, beginningCoordinates, endingCoordinates, sizeOfGrid)



    
    
    
