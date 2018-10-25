# A * Pathfinder Algorithm

class Node():
    def __init__(self, x, y, parent = None):
        self.x = x
        self.y = y

        self.parent = parent

        #Costs
        self.g = 0
        self.h = 0
        self.f = 0

#Algorithm
def pathfinder(matrix, s, e):                 #s,e -> tuple containing coordinates 
    start = Node(s[0], s[1])
    end = Node(e[0], e[1])
