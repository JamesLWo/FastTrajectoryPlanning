def adpativeAStar(maze, beginningCoordinates, endingCoordinates, console):
    plannedPath = []

    #call regular forwardAStar
    #need to get distance of plannedpath and popped nodes (expanded nodes)
    #go through each popped node and update h value to: distance - g value
    #update f value as well
    #keep track of these poppped nodes?
    #for the next run, if encounter popped nodes, use those h values 
    #then get distance again
    return plannedPath