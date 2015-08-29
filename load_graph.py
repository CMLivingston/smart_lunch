## load_graph.py
## 
## This module contains the function load_graph, which constructs a dictionary of 
## verticies to represent our graph structure of the Dartmouth campus
##
## To modify graph layout (where verticies are on map), edit verticies.txt in static folder and run load_graph to return an updated dict
##
## Adjacency lists are used to maintain graph relationships
##
##
from vertex import *



# load data from verticies.txt and return a vertex dictionary to represent our graph
def load_graph():
    
    file = "./static/verticies.txt"
    
    vertex_dict = {}
    
    # for each vertex pull out its name, x, and y information and assign it to an instance variable within an instance of a vertex object
    
    in_file = open(file, 'r')
    i = 0
    for line in in_file:
      
        vertex = Vertex()
        x = line.strip()
        s = x.split(';')
        
        # handy error reporting so i know which line in 'verticies.txt' is bad and is causing any errors
        try:
            d = s[2].strip()
        except IndexError:
            print "error on: " + str(s)
        
        f = d.split(',')
        # handy error reporting so i know which line in 'verticies.txt' is bad and is causing any errors
        try:
            vertex.name = s[0]
            vertex.x = f[0]
            vertex.y = f[1]
            vertex_dict[vertex.name] = vertex       
        except IndexError:
            print "error on: " + str(s)
            
    
    in_file.close()
    
    # open the same file and create a list of adjacent vertices by seperating elements by semi colons and then commas
    
    in_file2 = open(file, 'r')
    
    for line2 in in_file2:
        
        t = line2.strip()
        m = t.split(';')
        current = vertex_dict[m[0]]
        z = m[1].strip()
        p = z.split(', ')
        for i in range(0, len(p)):
            current.adj_list.append(vertex_dict[p[i]])
        for i in range(0, len(p)):
            current.adj_str.append(vertex_dict[p[i]].name)
    
    
    in_file2.close()   
  
    return vertex_dict


def test():
    v = load_graph()
    print v['sae']

if __name__ == "__main__":
    test()
       

