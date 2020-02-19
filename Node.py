class Node:
    def __init__(self, coordinates, parent, gvalue, hvalue):
        self.coordinates = coordinates
        self.parent = parent
        self.gvalue = gvalue
        self.hvalue = hvalue
        self.fvalue = self.gvalue + self.hvalue


    def __lt__(self, other):
        return self.fvalue < other.fvalue or (self.fvalue == other.fvalue and self.gvalue > other.gvalue)



        