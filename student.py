## Student Class
##
##
from load_data import *
from graphics import *
from bfs import *
from dist import dist
import time
import simpy

class Student:

    def __init__(self, idnum, x, y, speed, tolerance, preferences, times, env):
      
        self.id = idnum
        self.x = int(x)
        self.y = int(y)
        self.speed = int(speed)
        self.tolerance = int(tolerance)
        self.preferences = preferences
        self.times = times
        self.env = env
        self.action = env.process(self.run())
        self.has_food = False
        self.moving = False

    def __str__(self): 
        return "Student " + str(self.id)

    def run(self):
        pass
    
    def wait(self, duration):
        pass
    # draw movement of a point from one vertex to the next
    def makeMove(self, start, end, window, is_final_dest):
        
        # how fast the graphics will be drawn..manipulate with simpy?
        # .1 is very slow
        # 0.5 is close to actual walking speed
        # .01 is a good sped up version, and possibly max speed (from extensive testing)
        SIMULATION_SPEED = 0.01
        # pixels to move per step
        MOVE_INCREMENT = 1
        
        
        #print "Moving from " + str(start) + " to " + str(end) 
        #print "My current pos: " + str(self.x) + "," + str(self.y)
        
        self.x = start.x
        self.y = start.y
        
        p = Point(start.x,start.y)

        i = 0
        
        # each cell of the map is 39x39 and this draws one pixel at a time 
        # at a given SIMULATION speed until you draw all 39 ( you made it to end node )
        while (i != 39):
       
            i = i+1
            p.undraw()
            
            
            if (end.x == start.x):
                self.x = start.x
            elif (end.x < start.x):
                self.x = self.x - MOVE_INCREMENT
            else:
                self.x = int(self.x) + MOVE_INCREMENT
              
            if (end.y == start.y):
                self.y = start.y
            elif (end.y < start.y):
                self.y = self.y - MOVE_INCREMENT
            else:
                self.y = int(self.y) + MOVE_INCREMENT
            
           
            p = Point(self.x,self.y)
            p.draw(window)
            
            # wait
            time.sleep(SIMULATION_SPEED)
        
        # undraw for next call of makeMove, unless it is the last in the studnets path    
        p.undraw()
        self.x = end.x
        self.y = end.y 
        
        # if this is the last move until the food destination
        if (is_final_dest == True):
            
            self.x = end.x
            self.y = end.y    
            p = Point(self.x,self.y)
            p.draw(window)
        
        # done with this move
   
      
    def goToLunch(self, start_name, window):
         
        g = load_graph()
        
        start = g[start_name]
        # Jasper: maybe change below line to make random? 
        pref = self.preferences[0][0]
        
        end = g[str(pref)]
        path = bfs(start, end)
        
        # TRIP DISTANCE in pixels
        trip_dist = len(path)*39
        
        
        # print the shortest path to students preference
        i = len(path) - 1
        print "Path for student: " + str(self)
        while (i >= 0):
            print path[i]
            i = i-1
        
        print " "
        print "Student heading to lunch from " + "(" + str(start_name) + ")"
        
        # important! index path BACKWARDS (shortest path is dict of BACKPOINTERS)
        i = len(path) - 1
        while (i > 0):
           
            print path[i].name
            
            if (i == 1):
                is_final = True
            else:
                is_final = False
                
            self.makeMove(path[i], path[i-1], window, is_final) 
            i = i-1
      
        print "Student arrived at destination "  + str(path[i].name)    



def dartMap(im, win):
    p = Point(434, 320)
    i = Image(p, im)
    i.draw(win)


def test():
    
    # create a graphics window for the simulation and for the objects to be drawn on   
    win = GraphWin("IoT Simulation", 858, 638)
    background_image = "./static/dart.gif"
    dartMap(background_image, win)
    
    # testing student go to lunch function
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")
    # make preferences
    preferences = make_prefs(venues, 1)
    
    env = simpy.Environment()
    # make the student and send him to lunch
    s = make_student("./static/student.txt", 1, classrooms["silsby hall"], venues, env)
    # can be any name in classrooms.txt
    s.goToLunch("dartmouth hall", win)
    
    
    # close on click 
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()
