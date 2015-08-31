## Student Class
##
##
from load_data import *
from graphics import *
from bfs import *
from dist import dist
import time
import simpy
import classroom

class Student(object):

    def __init__(self, idnum, x, y, speed, tolerance, classroom, preferences, env):
      
        self.id = idnum
        self.x = int(x)
        self.y = int(y)
        self.speed = float(speed)
        self.tolerance = int(tolerance)
        self.classroom = classroom
        self.preferences = preferences
        self.times = []
        self.env = env
        self.action = env.process(self.run())
        self.has_food = False
        self.smart = False
        
    def __str__(self): 
        return "Student " + str(self.id)

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
    
    # non-graphics option
    def findLunchPath(self, start_name):
        g = load_graph()
        
        start = g[start_name]
        # Jasper: maybe change below line to make random? 
        pref = self.preferences[0][0]
        
        end = g[str(pref)]
        path = bfs(start, end)
        
        # TRIP DISTANCE in pixels
        trip_dist = len(path)*39
        return trip_dist

    def findBFS(self, start_name):
        g = load_graph()
        
        start = g[start_name]
        # Jasper: maybe change below line to make random? 
        pref = self.preferences[0][0]
        
        end = g[str(pref)]
        path = bfs(start, end)
        return path

    def goToLunch(self, start_name, window):
         
        g = load_graph()
        
        start = g[start_name]
        # Jasper: maybe change below line to make random? 
        pref = self.preferences[0][0]
        
        end = g[str(pref)]
        path = bfs(start, end)
        
        # TRIP DISTANCE in pixels
        trip_dist = len(path)*39
        print str(trip_dist) + "is it in PIXS"
        
        
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

    def makeTravelDist(self, pixel_dist):
        # 39 px = 88 ft
        px = 39
        feet = 88
        ret = (pixel_dist * feet) / px
        return ret

    def run(self):
        # wait to leave the classroom
        class_wait_time = self.classroom.line_spot(self) * self.classroom.exit_time
        yield self.env.timeout(class_wait_time)
        print ("Student %d left %s at %s" % (self.id, self.classroom, convertToMin(self.env.now)))
        depart_time = self.env.now

        curr_pref = self.preferences[0]
        venue = curr_pref[0]
        station = curr_pref[1]
        arrival_time = 0
        if self.smart == False:
            # go to venue
            travel_dist = makeTravelDist(self.findLunchPath(self.classroom.name))
            travel_time = travel_dist / self.speed
            #self.goToLunch(self.classroom.name, win)
            yield self.env.timeout(travel_time)
            print ("Student %d arrived at %s at %s" % (self.id, venue.name, convertToMin(self.env.now)))
            arrival_time = self.env.now

        elif self.smart == True and station != 0:
            nodes = self.findBFS(self.classroom.name)
            curr_index = len(nodes) - 1
            reached_venue = False
            # keep going unless tolerance exceeds
            while len(station.food_line) < self.tolerance:
                self.x = nodes[curr_index].x
                self.y = nodes[curr_index].y
                if self.x == nodes[0].x and self.y == nodes[0].y:
                    reached_venue = True
                    print ("Student %d arrived at %s at %s" % (self.id, venue.name, convertToMin(self.env.now)))
                    arrival_time = self.env.now
                    break
                next_node_dist = makeTravelDist(39) # each node move is 39 px
                travel_time = next_node_dist / self.speed
                yield self.env.timeout(travel_time)
                curr_index = curr_index - 1
            if reached_venue == False:
                curr_pref = self.preferences[1]
                venue = curr_pref[0]
                station = curr_pref[1]
                print "Student %d is rerouting to %s" % (self.id, venue.name)
                # go to venue
                travel_dist = makeTravelDist(self.findLunchPath(nodes[curr_index].name))
                travel_time = travel_dist / self.speed
                #self.goToLunch(self.classroom.name, win)
                yield self.env.timeout(travel_time)
                print ("Student %d arrived at %s at %s" % (self.id, venue.name, convertToMin(self.env.now)))
                arrival_time = self.env.now

        # get on food line, then get on cashier line
        if venue.name != "novack" and station != 0: # made-to-order
            # get on line
            station.food_line.append(self)
            # find out how long to wait
            people_ahead = station.line_spot(self)
            print "Student %d joined the %s line at position %d at %s" % (self.id, station.name, people_ahead+1, convertToMin(self.env.now))
            line_wait_time = (people_ahead + 1) * station.place_order_time
            # and wait
            yield self.env.timeout(line_wait_time)
            # now we put the dish on the line of dishes waiting to go and cook
            print "Student %d has ordered their %s at %s" % (self.id, station.name, convertToMin(self.env.now))
            station.food_line.remove(self)  # get off the food line and onto the cook line
            station.cook_line.append(self)
            while station.cook_line.index(self) != 0:  # if we aren't about to go on the grill, wait
                yield self.env.timeout(station.place_order_time)
            while station.is_full():  # once they're at the front, wait until spot on grill opens up (and increment the time_full)
                station.time_full = station.time_full + station.place_order_time
                yield self.env.timeout(station.place_order_time)
            station.cook_line.remove(self)  # now we go off the cook line and begin cooking
            station.cook_surface.append(self)
            print "Student %d's food started cooking at %s" % (self.id, convertToMin(self.env.now))
            yield self.env.timeout(station.cook_time)
            station.cook_surface.remove(self)
            print "Student %d received %s at %s" % (self.id, station.name, convertToMin(self.env.now))
            
            # now time to pay
            venue.cashier_line.append(self)
            # find out how long to wait
            people_ahead = venue.line_spot(self)
            print "Student %d joined the %s checkout line at position %d at %s" % (self.id, venue.name, people_ahead+1, convertToMin(self.env.now))
            pay_wait_time = (people_ahead + 1) * venue.cashier_wait
            # and wait
            yield self.env.timeout(pay_wait_time)
            # now we record the wait time at venue and the time they have to eat
            pay_time = self.env.now
            total_time = pay_time
            venue_wait_time = pay_time - arrival_time
            remaining_time = 4500 - pay_time
            self.times.append(total_time)
            self.times.append(venue_wait_time)
            self.times.append(remaining_time)
            print "Student %d paid at %s" % (self.id, convertToMin(self.env.now))
            venue.cashier_line.remove(self)
            self.has_food = True
        
        # if it's novack or prepared food, just get on cashier line (after delay for hop/collis)
        else:
            if(venue.name != "novack"):
                prep_fetch_time = 60
                print "Student %d is fetching their prepared food" % self.id
                yield self.env.timeout(prep_fetch_time)
            # now time to pay
            venue.cashier_line.append(self)
            # find out how long to wait
            people_ahead = venue.line_spot(self)
            print "Student %d joined the checkout line at position %d at %s" % (self.id, people_ahead+1, convertToMin(self.env.now))
            pay_wait_time = (people_ahead + 1) * venue.cashier_wait
            # and wait
            yield self.env.timeout(pay_wait_time)
            venue.cashier_line.remove(self)
            self.has_food = True
            # now we record the wait time at venue and the time they have to eat
            pay_time = self.env.now
            total_time = pay_time
            wait_time = pay_time - arrival_time
            remaining_time = 4500 - pay_time
            self.times.append(total_time)
            self.times.append(wait_time)
            self.times.append(remaining_time)
            print "Student %d paid at %s" % (self.id, convertToMin(self.env.now))


def dartMap(im, win):
    p = Point(434, 320)
    i = Image(p, im)
    i.draw(win)

def convertToMin(seconds):
    m, s = divmod(seconds, 60)
    m = str(int(m))
    s = str(int(s)).zfill(2)
    return m + ":" + s

def makeTravelDist(pixel_dist):
    # 39 px = 88 ft
    px = 39
    feet = 88
    ret = (pixel_dist * feet) / px
    return ret

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
