import numpy as np 
import random 
np.set_printoptions(threshold=np.inf)

#create actual maze and knowledge maze
trueMaze = np.zeros(shape = (50,50)).astype(int)
knowledgeMaze = np.zeros(shape = (50,50)).astype(int)
#populate actual maze
for x in np.nditer(trueMaze, op_flags=['readwrite']):
    if random.random() >= 0.7:
        x[...] = 1
    else:
        x[...] = 0
trueMaze[0,0] = 3
trueMaze[49,49] = 4

np.savetxt('test.txt', trueMaze, delimiter=',', fmt='%.0f')

print(trueMaze)


def repeatedAStar(maze, beginningCoordinates, endingCoordinates):
    plannedPath = []
    

    return plannedPath


def repeatedBackwardsAStar(maze, beginningCoordinates, endingCoordinates):
    plannedPath = []
    return plannedPath
