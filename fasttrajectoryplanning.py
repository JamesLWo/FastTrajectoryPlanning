import numpy as np 

#create actual maze and knowledge maze
trueMaze = np.zeros(shape = (50,50))
knowledgeMaze = np.zeros(shape = (50,50))

#populate actual maze
for x in np.nditer(trueMaze):
    randNum = random.randint(1,101)
    if randNum >= 1 and randNum <= 30:
        x = 1
    else:
        x = 0 

trueMaze[0,0] = S 
trueMaze[49,49] = G 

print(trueMaze)


def repeatedAStar(maze, beginningCoordinates, endingCoordinates):
    plannedPath = []
    return plannedPath


def repeatedBackwardsAStar(maze, beginningCoordinates, endingCoordinates):
    plannedPath = []
    return plannedPath
