## Main Driver Module for Simulation of Dartmouth Lunch Hour
## WITH and WITHOUT the INTERNET OF THINGS
##
## Created by Chris Livingston and Jasper Bingham
##
##
##
## IMPORTS
from graphics import *
##
##
##


def main():
    
    # create a graphics window for the simulation and for the objects to be drawn on   
    win = GraphWin("IoT Simulation", 858, 638)
    background_image = "./static/dart.gif"
    dartMap(background_image, win)
            
    while True:
        w = win.getMouse()
        print "x: " + str(w.x) + " y: " + str(w.y) 
    
    # to end sim
    win.getMouse()
    win.close()
    
 
# draws Dartmouth map into provided graphics window
def dartMap(im, win):
    p = Point(434, 320)
    i = Image(p,im)
    i.draw(win)



main()

