## load_data.py
## the methods of this module parse comma-seperated value files and return a dictionary of 
## objects that have been instantiated with the data from the CSV
from venue import *
from classroom import *
from station import *
from food import *
from student import *
import random
import math
import copy

def make_foods(filepath):

    in_file = open(filepath, 'r')
    foods = []

    for line in in_file:
        # make an array of strings seperated by ,
        x = line.strip()
        s = x.split(',')
        f = Food(s[0], float(s[1]))
        foods.append(f)

    return foods

def make_stations(filepath, foods):

    in_file = open(filepath, 'r')
    stations = {}
    hop_stations = []
    collis_stations = []
    novack_stations = []
    
    for line in in_file:
        # make an array of strings separated by ,
        x = line.strip()
        s = x.split(',')
        station_name = s[0]
        for food in foods:
            if station_name == food.name:
                station = Station(s[0], int(s[1]), int(s[2]), food)
                if s[3] == "hop":
                    hop_stations.append(station)
                elif s[3] == "collis":
                    collis_stations.append(station)
                break

    stations["hop_stations"] = hop_stations
    stations["collis_stations"] = collis_stations
    stations["novack_stations"] = novack_stations

    return stations

def make_venues(filepath, stations):
    
    venues = {}
    
    # for each venue in data file, extract its attributes and populate venue dictionary for use in driver.py
    in_file = open(filepath, 'r')
    
    for line in in_file:
        # make an array of strings seperated by ,
        x = line.strip()
        s = x.split(',')
        # construct a veune for placement into dict
        v = Venue(s[0],int(s[1]),int(s[2]),float(s[3]),int(s[4]),stations[s[5]])
      
        # put name string as index of dict
        venues[s[0]] = v
    
    in_file.close()
    
    return venues

def make_classrooms(filepath):
    
    classrooms = {}
    
    # for each classroom in data file, extract its attributes and populate classroom dictionary for use in driver.py
    in_file = open(filepath, 'r')
    for line in in_file:
        x = line.strip()
        s = x.split(',')
        c = Classroom(s[0],int(s[1]),int(s[2]))
        classrooms[s[0]] = c
    in_file.close()
    
    return classrooms

def make_student(filepath, idnum, classroom, venues):
    in_file = open(filepath, 'r')
    l = in_file.readline()
    x = l.strip()
    s = x.split(',')
    preferences = make_prefs(venues, idnum)
    times = []
    stud = Student(idnum, classroom.x, classroom.y, int(s[0]), int(s[1]), preferences, times, False)
    return stud

def make_prefs(venues, idnum):
    # first we need to rank the student's venue choices
    ret = [[0 for x in range(2)] for x in range(len(venues))]
    curr_rank = 0  # keeps track of which rank we're dealing with
    venues_copy = []
    for venue in venues:
        venues_copy.append(venues[venue])
    for y in range(0, len(venues_copy)):
        total_prob = 0  # will be upper range of our random num generation
        for venue in venues_copy:
            total_prob = total_prob + venue.chance
        bound_matrix = [[0 for z in range(2)] for z in range(len(venues_copy))]
        curr_bound = 0  # keeps track of which boundary we're making
        for a in range(0, len(venues_copy)):
            curr_bound = curr_bound + venues_copy[a].chance
            bound_matrix[a][0] = venues_copy[a]
            bound_matrix[a][1] = curr_bound
        pref = random.uniform(0, total_prob)  # randomly generated number
        bottom_bound = 0
        for b in range(0, len(venues_copy)):
            if pref >= bottom_bound and pref <= bound_matrix[b][1]:
                ret[curr_rank][0] = venues_copy[b]
                venues_copy.remove(venues_copy[b])
                curr_rank = curr_rank + 1
                break
            else:
                bottom_bound = bound_matrix[b][1]

    # then we need to figure out what food they will want at each place
    for z in range(0, len(venues)):
        if len(ret[z][0].stations) > 0:  # i.e., not novack
            curr_bound = 0
            pref = random.random()
            for station in ret[z][0].stations:
                if pref >= curr_bound and pref <= curr_bound + station.food.chance:
                    ret[z][1] = station
                    break
                else:
                    curr_bound = curr_bound + station.food.chance
        else:
            continue
    return ret

def test():
   
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")
    stud_id = 0
    students = []
    # make ten sample students
    while stud_id < 10:
        s = make_student("./static/student.txt", stud_id, classrooms["wilder hall"], venues)
        students.append(s)
        stud_id = stud_id + 1
    print "FOODS:"
    for food in foods:
        print food.name, food.chance
    print "STATIONS:"
    for station in stations:
        for s in stations[station]:
            print s.name
    print "VENUES:"
    for venue in venues:
        print venues[venue].name
        for station in venues[venue].stations:
            print station
    print "CLASSROOMS:"
    for classroom in classrooms:
        print classrooms[classroom], classrooms[classroom].x, classrooms[classroom].y
    for student in students:
        print "Student " + str(student.id) + ", located at: (" + str(student.x) + ", " + str(student.y) + ")"
        for preference in student.preferences:
            if preference[1] == 0:
                print preference[0].name, ":", "prepared"
            else:
                print preference[0].name, ":", preference[1]
            
if __name__ == "__main__":
    test()
