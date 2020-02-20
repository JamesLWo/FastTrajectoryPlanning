import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


def generate_maze():
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

if __name__ == "__main__":
    generate_maze()