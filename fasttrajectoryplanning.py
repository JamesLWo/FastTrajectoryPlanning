import numpy as np 
import repeatedAStar
import repeatedBackwardsAStar
import adaptiveAStar
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

path = repeatedAStar.repeatedAStar(knowledgeMaze, (0,0), (49,49)) 
path2 = repeatedBackwardsAStar.repeatedBackwardsAStar(knowledgeMaze, (0,0), (49,40))
path3 = adaptiveAStar.adpativeAStar(knowledgeMaze, (0,0), (49,49))

