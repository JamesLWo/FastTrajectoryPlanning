import os
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import colors

def generate_mazes(size, probability, method):
    directory = os.getcwd() + "\\maze_repo\\"
    np.set_printoptions(threshold=np.inf)

    for i in range(50):
        maze = np.zeros(shape = (size,size)).astype(int)
        for x in np.nditer(maze, op_flags=['readwrite']):
            if random.random() >= probability:
                x[...] = 1
            else:
                x[...] = 0

        if method == "forwards":
            maze[0,0] = 3
            maze[size-1, size-1] = 4
        elif method == "backwards":
            maze[0,0] = 4
            maze[size-1, size-1] = 3

        np.savetxt(directory+'test{}.txt'.format(i+1), maze, delimiter=',', fmt='%.0f')


def text_to_array():
    filename = os.getcwd() + "\\test.txt"
    
    with open(filename) as file:
        array2d = np.array([[int(digit) for digit in line.split(",")] for line in file])

    print(array2d)

    cmap = colors.ListedColormap(['white', 'black', 'yellow', 'red', 'green'])
    bounds=[0,1,2,3,4,5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(array2d, cmap=cmap, norm=norm)
    plt.show()

    return array2d

def clear_dir(folder):
    if folder == "logs":
        subdir = "\\logs\\"
    elif folder == "mazes":
        subdir = "\\maze_repo\\"
    elif folder == "cache":
        subdir = "\\__pycache__\\"
    else:
        print("invalid option")
        return
        
        
    directory = os.getcwd() + subdir
    
    list(map(os.unlink, (os.path.join(directory,f) for f in os.listdir(directory))))

if __name__ == "__main__":
    # clear_dir("cache")
    # text_to_array()
    # generate_mazes(10, 0.7, "forwards")
    pass