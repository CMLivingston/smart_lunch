# this is just for testing dartmouth-specific applications
# of the various classes

from venue import *
from station import *
from food import *
from student import *

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
    while students > 0:
        preferences = make_prefs(venues)
        stud = Student(curr_id, walk_speed, line_tolerance, preferences, 0, False)
        stud_array.append(stud)
        curr_id = curr_id + 1
        students = students - 1

    # ...and return the students.
    return stud_array

def make_prefs(venues):
    # first we need to rank the student's venue choices
    ret = [[0 for x in range(2)] for x in range(len(venues))]
    curr_prob = 1
    for x in range(0, len(venues)):
        if x != len(venues) - 1: # first two cycles
            

        else: # remaining is third choice by default
            ret[len(ret) - 1] = venues[0]







setup()
