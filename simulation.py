# simulation.py
# Authors: Jasper Bingham and Chris Livingston
# 8/31/15
#
# This is the driver module for our project's simulation 
#
#
import simpy
import venue
from load_data import *
#
#
#
#
#
# display shortest paths taken for "dumb simulation"
def run_graphics_win(window, classrooms):
    
    for c in classrooms: 
        
        q = classrooms[c].departure_queue
        
        for j in range(0,1):
           
            q[j].goToLunch(classrooms[c].name, window)

    window.close()
    
def run_dumb_simulation():
    print "Welcome to the \"Lunchtime at Dartmouth!\" simulation!"
    print "This version of the simulation does NOT use the IoT."
    num_of_students = 0
    while True:
        try:
            num_of_students = int(raw_input("Please enter the number of students you wish to simulate (multiple of four): "))
        except ValueError:
            print "That's not an integer! Try again, please."
            continue
        if num_of_students % 4 == 0:
            break
        else:
            print "That's not a multiple of four! Try again, please."
    
    # create environment
    env = simpy.Environment()
   
    # create a graphics window for the simulation and for the objects to be drawn on   
    window = GraphWin("IoT Simulation", 858, 638)
    background_image = "./static/dart.gif"
    dartMap(background_image, window)
        
    # make all the objects
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")

    start_points = get_start_points("./static/start_points.txt")
    stud_id = 0
    index = 0
    inc = num_of_students / 4
    switch_point = inc

    all_students = []
    finished_students = []

    while stud_id < switch_point:
        s = make_student("./static/student.txt", stud_id, classrooms[start_points[index]], venues, env)
        s.smart = False
        all_students.append(s)
        classrooms[start_points[index]].departure_queue.append(s)
        stud_id = stud_id + 1
        if stud_id == num_of_students:
            break
        if stud_id == switch_point: # start populating next building
            index = index + 1
            switch_point = switch_point + inc


    
    # run the simulation for 75 (simulated) minutes
    env.run(until=4500)  # 75 minutes
    
    # run graphics demo
    print ""
    print "Running graphical simulation of path taken by first 2 students of each classroom..."
    
    run_graphics_win(window, classrooms)


    for student in all_students:
        if student.has_food:
            finished_students.append(student)

    averages = get_averages(finished_students)

    old_stdout = sys.stdout
    log_file = open("dumb.log","w")
    sys.stdout = log_file
    print "FINAL REPORT (NO IoT):"
    print "Average time before each student got their food:"
    print averages[0]
    print "Average time each student waited on lines at their venue of choice:"
    print averages[1]
    print "Average time each student had to eat before class:"
    print averages[2]
    print "Number of students who did not receive food:"
    print str(len(all_students) - len(finished_students))
    sys.stdout = old_stdout
    log_file.close()

def run_smart_simulation():
    print "Welcome to the \"Lunchtime at Dartmouth!\" simulation!"
    print "This version of the simulation DOES use the IoT."
    num_of_students = 0
    while True:
        try:
            num_of_students = int(raw_input("Please enter the number of students you wish to simulate (multiple of four): "))
        except ValueError:
            print "That's not an integer! Try again, please."
            continue
        if num_of_students % 4 == 0:
            break
        else:
            print "That's not a multiple of four! Try again, please."
    
    # create environment
    env = simpy.Environment()

    '''
    # create a graphics window for the simulation and for the objects to be drawn on   
    win = GraphWin("IoT Simulation", 858, 638)
    background_image = "./static/dart.gif"
    dartMap(background_image, win)
    '''

    # make all the objects
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")

    start_points = get_start_points("./static/start_points.txt")
    stud_id = 0
    index = 0
    inc = num_of_students / 4
    switch_point = inc

    all_students = []
    finished_students = []

    while stud_id < switch_point:
        s = make_student("./static/student.txt", stud_id, classrooms[start_points[index]], venues, env)
        s.smart = True
        all_students.append(s)
        classrooms[start_points[index]].departure_queue.append(s)
        stud_id = stud_id + 1
        if stud_id == num_of_students:
            break
        if stud_id == switch_point: # start populating next building
            index = index + 1
            switch_point = switch_point + inc

    env.run(until=4500)  # 75 minutes
    
    for student in all_students:
        if student.has_food:
            finished_students.append(student)

    averages = get_averages(finished_students)

    old_stdout = sys.stdout
    log_file = open("smart.log","w")
    sys.stdout = log_file
    print "FINAL REPORT (WITH IoT):"
    print "Average time before each student got their food:"
    print averages[0]
    print "Average time each student waited on lines at their venue of choice:"
    print averages[1]
    print "Average time each student had to eat before class:"
    print averages[2]
    print "Number of students who did not receive food:"
    print str(len(all_students) - len(finished_students))
    sys.stdout = old_stdout
    log_file.close()
    

def get_start_points(filepath):
    start_points = []
    in_file = open(filepath, 'r')
    l = in_file.readline()
    x = l.strip()
    s = x.split(',')
    for string in s:
        start_points.append(string)
    return start_points

def get_averages(students):
    averages = []
    num_of_students = len(students)

    # min to get food
    get_food_total = 0 
    get_food_avg = 0
    for student in students:
        get_food_total = get_food_total + student.times[0]
    get_food_avg = convertToMin(int(get_food_total / num_of_students))
    averages.append(get_food_avg)

    # wait time at venue
    wait_time_total = 0 
    wait_time_avg = 0
    for student in students:
        wait_time_total = wait_time_total + student.times[1]
    wait_time_avg = convertToMin(int(wait_time_total / num_of_students))
    averages.append(wait_time_avg)

    # time before class
    before_class_total = 0 
    before_class_avg = 0
    for student in students:
        before_class_total = before_class_total + student.times[2]
    before_class_avg = convertToMin(int(before_class_total / num_of_students))
    averages.append(before_class_avg)

    return averages


# start
run_dumb_simulation()
print ""
print "Starting new simulation..."
print ""
run_smart_simulation()
print ""
print "Simulation complete! Check out the logs to see the benefits of the IoT!"
print ""