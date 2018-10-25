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

# Algorithm
def pathfinder(matrix, start, end):                 # s,e -> tuple containing coordinates

    # Set start node and end node
    startnode = Node(start[0], start[1])
    endnode = Node(end[0], end[1])

    # Initialize open and closed list
    open_list = []
    closed_list = []

    open_list.append(startnode)

    # Loop until endnode
    while len(open_list) > 0:

        # Current node
        current_node = open_list[0]
        current_index = 0
        # Find the smallest f value
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        # Pop current from open and add to closed
        open_list.pop(current_index)
        closed_list.append(current_node)

        # If current == end
        if current_node == endnode:
            path = []
            current = current_node
            while current is not None:               # backtrack the path
                path.append((current.x,current.y))
                current = current.parent
            return path[::-1]

        # Generate children or adjacent nodes
        children = []
        adjacent = [(0,1), (0,-1), (-1,0), (1,0)]
        for node in adjacent:
            new_x = current_node.x + node[0]
            new_y = current_node.y + node[1]

            # Check range
            if new_x > (len(matrix) - 1) or new_x < 0 or new_y > (len(matrix[0]) - 1) or new_y < 0:
                continue

            # Not a wall
            if matrix[new_x][new_y] == 'X':
                continue

            # Create a new node
            new_node = Node(new_x, new_y, current_node)

            children.append(new_node)

        # loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create g, h and f
            child.g = current_node.g + 1
            child.h = abs(end[0] - child.x) + abs(end[1] - child.y)
            child.f = child.g + child.h

            # Child is in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# DRIVER FUNCTION

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (7, 6)

path = pathfinder(maze, start, end)
print(path)
