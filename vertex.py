## Vertex class for BFS graph in simulation
## Chris Livingston


VERTEX_RADIUS = 12
STROKE_WIDTH = 3

class Vertex:
    
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None
        self.adj_list = []
        self.adj_str = []
    
    def __str__(self):
        return str(self.name) + '; ' + "Location: " + str(self.x) + ',' + str(self.y) + '; ' + "Adjacent vertices: " + ', '.join(self.adj_str)
    
    # returns string of name for a list of names of adjacent vertices
    def name(self):
        return str(self.name)
    

    # check to see if the mouse is on a vertex
    def pos_check(self, x, y):
        if (int(x) <= int(self.x) + VERTEX_RADIUS and int(x) >= int(self.x) - VERTEX_RADIUS) and (int(y) <= int(self.y) + VERTEX_RADIUS and int(y) >= int(self.y) - VERTEX_RADIUS):
            return True
        
        
       
        
       