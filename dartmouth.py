# this is just for testing dartmouth-specific applications
# of the various classes

from venue import *
from station import *
from food import *
from student import *
import random
import math
import copy

def setup():

    # create foods first...
    eggs_chance = 0.35
    eggs = Food("Eggs", 0, eggs_chance)
    stirfry_chance = 0.35
    stirfry = Food("Stirfry", 0, stirfry_chance)
    grill_chance = 0.5
    grill = Food("Grill Item", 0, grill_chance)
    sandwich_chance = 0.3
    sandwich = Food("Sandwich", 0, sandwich_chance)

    # ...then create stations...
    egg_cook = 3
    egg_max = 4
    egg_station = Station("Eggs", egg_cook, egg_max, eggs)
    stirfry_cook = 5
    stirfry_max = 4
    stirfry_station = Station("Stirfry", stirfry_cook, stirfry_max, stirfry)
    grill_cook = 4
    grill_max = 10
    grill_station = Station("Grill", grill_cook, grill_max, grill)
    sandwich_cook = 4
    sandwich_max = 2
    sandwich_station = Station("Sandwich", sandwich_cook, sandwich_max, sandwich)

    # ...then create station arrays...
    hop_stations = []
    collis_stations = []
    novack_stations = [] # left empty
    hop_stations.append(grill_station)
    hop_stations.append(sandwich_station)
    collis_stations.append(egg_station)
    collis_stations.append(stirfry_station)

    # ...then create venues...
    hop_x = 0
    hop_y = 0
    collis_x = 0
    collis_y = 0
    novack_x = 0
    novack_y = 0
    hop_chance = 0.4
    hop_wait = 0.5 # minutes
    collis_chance = 0.4
    collis_wait = 0.5
    novack_chance = 0.2
    novack_wait = 1
    hop = Venue("The Hop", hop_x, hop_y, hop_chance, hop_wait, hop_stations)
    collis = Venue("Collis", collis_x, collis_y, collis_chance, collis_wait, collis_stations)
    novack = Venue("Novack", novack_x, novack_y, novack_chance, novack_wait, novack_stations)
    
    # ...then create students...
    students = 10
    stud_array = []
    venues = []
    venues.append(hop)
    venues.append(collis)
    venues.append(novack)
    curr_id = 1
    walk_speed = 3 # mph
    line_tolerance = 10
    start_x = 0
    start_y = 0
    while students > 0:
        preferences = make_prefs(venues, curr_id)
        stud = Student(curr_id, start_x, start_y, walk_speed, line_tolerance, preferences, 0, False)
        stud_array.append(stud)
        curr_id = curr_id + 1
        students = students - 1

    # ...and return the students.
    for student in stud_array:
        print "Student " + str(student.id)
        for preference in student.preferences:
            if preference[1] == 0:
                print preference[0].name, ":", "Prepared"
            else:
                print preference[0].name, ":", preference[1]
    return stud_array

def make_prefs(venues, idnum):

    # first we need to rank the student's venue choices
    ret = [[0 for x in range(2)] for x in range(len(venues))]
    curr_rank = 0  # keeps track of which rank we're dealing with
    venues_copy = copy.deepcopy(venues)
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

setup()
