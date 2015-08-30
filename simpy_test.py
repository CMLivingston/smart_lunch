# sandbox for simpy stuff
import simpy
from load_data import *

def test():
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    classrooms = make_classrooms("./static/classrooms.txt")

    env = simpy.Environment()
    stud_id = 0

    while stud_id < 10:
        s = make_student("./static/student.txt", stud_id, classrooms["wilder hall"], venues, env)
        classrooms["wilder hall"].departure_queue.append(s)
        stud_id = stud_id + 1

    while stud_id < 20:
        s = make_student("./static/student.txt", stud_id, classrooms["dartmouth hall"], venues, env)
        classrooms["dartmouth hall"].departure_queue.append(s)
        stud_id = stud_id + 1

    env.run(until=5000)

test()