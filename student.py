## Student Class
##
##
from load_data import *
from graphics import *
from bfs import *
# NOTE : (CHIRS) Attempting to make a function that draws animaton of avatar going form one node to next

class Student:

    def __init__(self, idnum, x, y, speed, tolerance, preferences, times, has_food):
      
        self.id = idnum
        self.x = x
        self.y = y
        self.speed = speed
        self.tolerance = tolerance
        self.preferences = preferences
        self.times = times
        self.has_food = False

    def __str__(self): 
        return "Student " + str(self.id)

    def hasFood(self):
        return self.has_food
    
    def goToLunch(self, start_name):
        g = load_graph()
        
        start = g[start_name]
        pref = self.preferences[0][0]
        end = g[str(pref)]
        path = bfs(start, end)
        
        i = len(path) - 1
        print "Path for student: " + str(self)
        while (i >= 0):
            
            print path[i]
            i = i-1
        print "done"
                


def test():
    
    
    # testing student go to lunch function
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")
    
    preferences = make_prefs(venues, 1)
    
    # make the student and send him to lunch
    s = make_student("./static/student.txt", 1, classrooms["silsby hall"], venues)
    s.goToLunch("silsby hall")

if __name__ == "__main__":
    test()
