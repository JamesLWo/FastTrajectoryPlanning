import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import random
import os
import time
import repeatedAStar
import adaptiveAStar

def tracePath(maze, path):
    first = True
    for coordinate in path:
        if first:
            maze[coordinate] = 6
            first = False
        else:
            maze[coordinate] = 5
        
    return maze

#### CONFIGURATION ####
random.seed(900)
np.set_printoptions(threshold=np.inf)

color_set = ['white', 'black', 'green', 'red', 'yellow', 'orange']
range_set = np.array([-0.5,0.5,2.5,3.5,4.5,5.5,6.5])

cmap = colors.ListedColormap(color_set)
norm = colors.BoundaryNorm(range_set, len(color_set))

console = False

#### PARAMETERS #####
size = 101
probability = 0.7
method = "forwards"

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


if trueMaze[1,0] == 1:
    knowledgeMaze[1,0] = 1
if trueMaze[0,1] == 1:
    knowledgeMaze[0,1] = 1
########## TESTING ##################

start_time = time.time()

if trueMaze[1,0] == 1:
        knowledgeMaze[1,0] = 1
if trueMaze[0,1] == 1:
    knowledgeMaze[0,1] = 1

if(method == "forwards"):
    path,numexpanded = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (0,0), (size-1,size-1), size, console, False)
    print(numexpanded)
elif(method == "backwards"):
    path,numexpanded= repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (size-1, size-1), (0,0), size, console, True)
    print(numexpanded)

elif(method == "adaptive"):
    path,numexpanded= repeatedAStar.repeatedAStarAdaptive(knowledgeMaze, trueMaze, (0,0), (size-1,size-1), size, console)
    print(numexpanded)  
else:
    print("invalid option")

end_time = time.time()

directory = os.getcwd() + "//logs//"

# delete all files in log directory
list(map(os.unlink, (os.path.join(directory,f) for f in os.listdir(directory))))

np.savetxt(directory + '_maze.txt', trueMaze, delimiter=',', fmt='%.0f')

if console:
    print("true maze: ")
    print(trueMaze)

plt.imshow(trueMaze, cmap=cmap, norm=norm)
plt.savefig(directory + "true_maze.png")
# plt.show()
plt.close()

if console:
    print("answer: ")
    print(path)

#for path2 in path[0]:
 #   print(path2)

print(len(path[0]))


plt.imshow(knowledgeMaze, cmap=cmap, norm=norm)
plt.savefig(directory + "blank.png")
# plt.show()
plt.close()

# DISPLAY PARTIAL PATHS
for index, partial in enumerate(path[0]):
    pathMaze = tracePath(path[1][index], partial)
    plt.imshow(pathMaze, cmap=cmap, norm=norm)
    plt.savefig(directory + "partial_maze_{}".format(index+1) + ".png")
    # plt.show()
    plt.close()

final_time = time.time()
print(end_time-start_time)
print(final_time - start_time)