## Breadth-First Search Function
## Created By Chris Livingston 
##
##
from collections import deque
from load_graph import *


def bfs(start, end):
   
    # create a dictionary of back pointers
    backpointers ={}
    backpointers[start] = None
    x = start
    
    # create a frontier queue
    q = deque()
    q.append(start)
    
    while len(q) != 0 and not end in backpointers:
        
        x = q.popleft()
        if x != None:
            for i in x.adj_list:
                if i not in backpointers:
                    backpointers[i] = x
                    q.append(i)
    
    # make a path from the start to the end and return it
    path = []
    current_vertex = end
    
    while backpointers[current_vertex]!= None:
        path.append(current_vertex)
        current_vertex = backpointers[current_vertex]
    path.append(current_vertex)
    
    return path 
    
        