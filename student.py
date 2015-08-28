## Student Class
##
##

class Student:

    def __init__(self, id, speed = 3, tolerance = 10, preferences = [], times = [], has_food = False):
        
        self.id = id
        self.speed = speed
        self.tolerance = tolerance
        self.preferences = preferences
        self.times = times    
        self.has_food_bool = has_food
    
    def __str__(self):     
        return str(self.id)

    def hasFood(self):
        return self.has_food_bool






def test():
   
    s = Student(2,5,3)
    print s.hasFood()

if __name__ == "__main__":
    test()



