## Student Class
##
##

class Student:

    def __init__(self, idnum, speed, tolerance, preferences, times, has_food):
      
        self.id = idnum
        self.speed = speed
        self.tolerance = tolerance
        self.preferences = [[0 for x in range(1)] for x in range(3)]
        setPrefs(preferences)
        self.times = times
        self.has_food = False

    def __str__(self): 
        return str(self.idnum)

    def hasFood(self):
        return self.has_food

    def setPrefs(self, preferences):







def test():
   
    s = Student()
    print s.hasFood()

if __name__ == "__main__":
    test()



