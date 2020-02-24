import numpy as np
import random
import repeatedAStar
# import repeatedBackwardsAStar
import adaptiveAStar
import matplotlib.pyplot as plt
from matplotlib import colors

np.set_printoptions(threshold=np.inf)

# PARAMETERS ######
size = 101
probability = 0.7
method = "forwards"
###################

#create actual maze and knowledge maze
trueMaze = np.zeros(shape = (size,size)).astype(int)
knowledgeMaze = np.zeros(shape = (size,size)).astype(int)

#populate actual maze
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


# OPTIONAL EDGE CASES

# block corner - backwards
# trueMaze[0,1] = 1
# trueMaze[1,0] = 1


# give knowledge maze initial knowledge
if trueMaze[1,0] == 1:
    knowledgeMaze[1,0] = 1
if trueMaze[0,1] == 1:
    knowledgeMaze[0,1] = 1

np.savetxt('test.txt', trueMaze, delimiter=',', fmt='%.0f')

print("true maze: ")
print(trueMaze)


########## TESTING ##################

if(method == "forwards"):
    path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (0,0), (size-1,size-1), size) 
elif(method == "backwards"):
    path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (size-1, size-1), (0,0), size)
elif(method == "adaptive"):
    path = adaptiveAStar.adpativeAStar(knowledgeMaze, (0,0), (size-1,size-1))
else:
    print("invalid option")


print("answer: ")
print(path)