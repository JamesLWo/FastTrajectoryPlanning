import numpy as np
import random
import repeatedAStar
# import repeatedBackwardsAStar
import adaptiveAStar
import matplotlib.pyplot as plt
from matplotlib import colors
import os


def tracePath(maze, path):
    for coordinate in path:
        maze[coordinate] = 5
    return maze


#### CONFIGURATION ####
# random.seed(2)
np.set_printoptions(threshold=np.inf)

color_set = ['white', 'black', 'green', 'red', 'yellow']
range_set = np.array([-0.5,0.5,2.5,3.5,4.5,5.5])

cmap = colors.ListedColormap(color_set)
norm = colors.BoundaryNorm(range_set, len(color_set))

#### PARAMETERS #####
size = 101
probability = 0.7
method = "backwards"

#create actual maze and knowledge maze
trueMaze = np.zeros(shape = (size,size)).astype(int)
knowledgeMaze = np.zeros(shape = (size,size)).astype(int)

# populate actual maze
for x in np.nditer(trueMaze, op_flags=['readwrite']):
    if random.random() >= probability:
        x[...] = 1
    else:
        x[...] = 0

# set start and end points
trueMaze[0,0] = 3
trueMaze[size-1,size-1] = 4
knowledgeMaze[0,0] = 3
knowledgeMaze[size-1,size-1] = 4


########## TESTING ##################

if(method == "forwards"):
    # give knowledge maze initial knowledge
    if trueMaze[1,0] == 1:
        knowledgeMaze[1,0] = 1
    if trueMaze[0,1] == 1:
        knowledgeMaze[0,1] = 1
    path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (0,0), (size-1,size-1), size)

elif(method == "backwards"):
    trueMaze[0,0] = 4
    trueMaze[size-1,size-1] = 3
    knowledgeMaze[0,0] = 4
    knowledgeMaze[size-1,size-1] = 3

    if trueMaze[size-2,size-1] == 1:
        knowledgeMaze[size-2,size-1] = 1
    if trueMaze[size-1,size-2] == 1:
        knowledgeMaze[size-1,size-2] = 1
    path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (size-1, size-1), (0,0), size)

elif(method == "adaptive"):
    path = adaptiveAStar.adpativeAStar(knowledgeMaze, (0,0), (size-1,size-1))
else:
    print("invalid option")


directory = os.getcwd() + "\\logs\\"

np.savetxt(directory + '_maze.txt', trueMaze, delimiter=',', fmt='%.0f')

print("true maze: ")
print(trueMaze)


plt.imshow(trueMaze, cmap=cmap, norm=norm)
plt.savefig(directory + "true_maze.jpg")
plt.show()


print("answer: ")
print(path)

plt.imshow(knowledgeMaze, cmap=cmap, norm=norm)
plt.savefig(directory + "blank.jpg")
plt.show()

# DISPLAY PARTIAL PATHS
for index, partial in enumerate(path[0]):
    pathMaze = tracePath(path[1][index], partial)
    plt.imshow(pathMaze, cmap=cmap, norm=norm)
    plt.savefig(directory + "partial_maze_" + str(index+1) + ".jpg")
    plt.show()

