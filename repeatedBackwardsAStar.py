import math
import numpy as np
import random
import heapq
import Node
import matplotlib.pyplot as plt


def repeatedBackwardsAStar(maze , start, end):
    openList = []
    closedList = []
    heapq.heapify(openList)

    cursor = Node.Node(start, None, 0, heuristic(start, end))

    openList.append(cursor)

    while(cursor.coordinates != end):
        cursor = heapq.heappop(openList)
        neighbors = get_neighbors(maze, cursor.coordinates[0], cursor.coordinates[1])
        closedList.append(cursor)

        for neighbor in neighbors:
            if neighbor not in closedList and neighbor not in openList:
                newNode = Node.Node(neighbor, cursor, cursor.gvalue + 1, heuristic(neighbor, end))
                heapq.heappush(openList, newNode)
            elif neighbor not in closedList and neighbor in openList:
                current_node = get_node(openList, neighbor) 

                if current_node.fvalue > cursor.gvalue + 1 + heuristic(neighbor, end):
                    current_node.gvalue = cursor.gvalue + 1
                    current_node.hvalue = heuristic(neighbor, end)
                    current_node.fvalue = current_node.gvalue + current_node.hvalue
                    current_node.parent = cursor

        print(len(openList))
        if len(openList) == 0:
            return []

        cursor = openList[0]


    return backtrack(heapq.heappop(openList))



def backtrack(cursor):
    path = []
    while cursor:
        path.append(cursor.coordinates)
        cursor = cursor.parent
    return path

def heuristic(start, goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def get_neighbors(maze, x, y):
    neighbors = []
    valid_x = [-1, 0, 0, 1]
    valid_y = [0, -1, 1, 0]

    for k in range(4):
        if valid_neighbor(maze, x + valid_x[k], y + valid_y[k]):
            neighbors.append((x + valid_x[k], y + valid_y[k]))

    return neighbors

def valid_neighbor(maze, x, y):
    return (x >= 0 and x < maze.shape[0] and y >= 0 and y < maze.shape[1]) and maze[x,y] != 1


def get_node(openList, coordinate):
    for node in openList:
        if node.coordinates == coordinate: 
            return node
    return None

if __name__ == "__main__":
    maze = np.zeros(shape = (10,10)).astype(int)
    unknown = np.zeros(shape = (10,10)).astype(int)
    for x in np.nditer(maze, op_flags=['readwrite']):
        if random.random() >= 0.8:
            x[...] = 1
        else:
            x[...] = 0

    maze[0,0] = 3
    maze[9,9] = 4
    unknown[0,0] = 3
    unknown[9,9] = 4

    # print(maze)

    start = unknown[9,9]
    end = unknown[0,0]

    # print(get_neighbors(maze, 1, 1))
    plannedPath = repeatedBackwardsAStar(maze, (9, 9), (0,0))

    print(plannedPath)

    img = plt.imshow(maze)
    plt.savefig("reg.jpg")
    plt.show()


    for coordinate in plannedPath:
        maze[coordinate[0], coordinate[1]] = 5
    
    img2 = plt.imshow(maze)
    plt.savefig("path.jpg")
    plt.show()


    print(maze)