import numpy as np 
# import repeatedAStar
# import repeatedBackwardsAStar
# import adaptiveAStar
import random 
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)

sizeOfGrid = 10
#create actual maze and knowledge maze
trueMaze = np.zeros(shape = (sizeOfGrid,sizeOfGrid)).astype(int)
knowledgeMaze = np.zeros(shape = (sizeOfGrid,sizeOfGrid)).astype(int)
#populate actual maze
for x in np.nditer(trueMaze, op_flags=['readwrite']):
    if random.random() >= 0.7:
        x[...] = 1
    else:
        x[...] = 0
trueMaze[0,0] = 3
trueMaze[sizeOfGrid-1,sizeOfGrid-1] = 4
knowledgeMaze[0,0] = 3
knowledgeMaze[sizeOfGrid-1,sizeOfGrid-1] = 4

#give knowledge maze initial knowledge
if trueMaze[1,0] == 1:
    knowledgeMaze[1,0] = 1
if trueMaze[0,1] == 1:
    knowledgeMaze[0,1] = 1

np.savetxt('test.txt', trueMaze, delimiter=',', fmt='%.0f')

print("true maze: ")
print(trueMaze)

path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (0,0), (sizeOfGrid-1,sizeOfGrid-1), sizeOfGrid) 
print("answer: ")
print(path)
#path2 = repeatedBackwardsAStar.repeatedBackwardsAStar(knowledgeMaze, (0,0), (49,40))
#path3 = adaptiveAStar.adpativeAStar(knowledgeMaze, (0,0), (49,49))
plt.imshow(trueMaze)
plt.show()

print(trueMaze)

# path = repeatedAStar.repeatedAStar(knowledgeMaze, trueMaze, (0,0), (49,49)) 
# path2 = repeatedBackwardsAStar.repeatedBackwardsAStar(knowledgeMaze, (0,0), (49,40))
# path3 = adaptiveAStar.adpativeAStar(knowledgeMaze, (0,0), (49,49))

