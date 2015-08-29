## Student Class
##
##

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
        return "Student " + str(self.idnum)

    def hasFood(self):
        return self.has_food

def test():
   
    s = Student()
    print s

if __name__ == "__main__":
    test()
