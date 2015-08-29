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
    
    # load venue/classroom object data into appropriate dictionaries for later
    venues = give_me_venue_dict()
    classrooms = give_me_classroom_dict()
    
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
    
    
    
    # load graph data structure with nodes representing Dartmouth campus
    g = load_graph()
    start = g['baker east']
    end = g['carson']
    x = bfs(start, end)
    print "Shortest path from start to end: "
    for v in x:
        print v

    # print x and y of mouse click (for testing)         
    while True:
        w = win.getMouse()
        print "x: " + str(w.x) + " y: " + str(w.y) 
    
  
 
# draws Dartmouth map into provided graphics window
def dartMap(im, win):
    p = Point(434, 320)
    i = Image(p, im)
    i.draw(win)



main()

