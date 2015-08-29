# # Main Driver Module for Simulation of Dartmouth Lunch Hour
# # WITH and WITHOUT the INTERNET OF THINGS
# #
# # Created by Chris Livingston and Jasper Bingham
# #
# # 8/28/15
# #
# #
# # IMPORTS
from graphics import *
from load_data import *
from load_graph import load_graph
from venue import *
from classroom import *
from student import *
from bfs import *
# #
# #
# # MACROS
DEBUG_GRAPH = True


def main():
    
    # create a graphics window for the simulation and for the objects to be drawn on   
    win = GraphWin("IoT Simulation", 858, 638)
    background_image = "./static/dart.gif"
    dartMap(background_image, win)
    
    # load data from dictionary populating functions in 'load_data'
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")
    
    
    if (DEBUG_GRAPH == True):
        # draw grid on background so we can see nodes of map
        inc = 39
        i = 0
        px = 0    
        while (i < 22):
            px = px + inc
            l = Line(Point(px, 0), Point(px, 638))
            l.draw(win)
            i = i + 1
        inc = 39
        i = 0
        py = 0
        while (i < 16):
            py = py + inc
            l = Line(Point(0, py), Point(858, py))
            l.draw(win)
            i = i + 1
    
    if (DEBUG_GRAPH == True):
        # change this around to any of the vertex names found in 'vertices.txt'
        graphTest('reed hall', 'wentworth')
    
    if (DEBUG_GRAPH == True):
        # print x and y of mouse click (for testing)        
        while True:
            w = win.getMouse()
            print "x: " + str(w.x) + " y: " + str(w.y) 
    
  


## helper functions 
#
#
#
#
# draws Dartmouth map into provided graphics window
def dartMap(im, win):
    p = Point(434, 320)
    i = Image(p, im)
    i.draw(win)


# to test shortest pathfinding in graph
def graphTest(start, end):
  # load graph data structure with nodes representing Dartmouth campus
    g = load_graph()
    s = g[start]
    e = g[end]
    x = bfs(s, e)
    print "Shortest path from start to end (reverse order): "
    for v in x:
        print v
#
#
#
#
#
#
main()

