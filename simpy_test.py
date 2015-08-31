# sandbox for simpy stuff
import simpy
import venue
from load_data import *

def run_simulation():
    print "Welcome to the \"Lunchtime at Dartmouth!\" simulation!"
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
    
    env = simpy.Environment()
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

    print "FINAL REPORT:"
    print "Average time before each student got their food:"
    print averages[0]
    print "Average time each student waited on lines at their venue of choice:"
    print averages[1]
    print "Average time each student had to eat before class:"
    print averages[2]
    print "Number of students who did not receive food:"
    print str(len(all_students) - len(finished_students))



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

run_simulation()