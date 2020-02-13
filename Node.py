class Node:
    def __init__(self, x, y, parent, gvalue, hvalue):
        self.x = x
        self.y = y
        self.parent = parent
        self.gvalue = gvalue
        self.hvalue = hvalue
        self.fvalue = self.gvalue + self.hvalue


    


        