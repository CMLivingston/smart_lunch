## Station class
## 

import Queue
import food

class Station:
    
    def __init__(self, name, cook_time, max_items, food):
        
        self.name = name
        self.cook_time = cook_time
        self.food_line = []
        self.cook_line = []
        self.cook_surface = []
        self.max_items = max_items
        self.place_order_time = 15 # constant for all stations, i.e. "can I have a _____"
        self.food = food
        self.time_full = 0
        
    def __str__(self):
        return str(self.name) 

    def line_spot(self, student):
        if student in self.food_line:
            return self.food_line.index(student)

    def is_full(self):
        if len(self.cook_surface) == self.max_items:
            return True
        return False

def test():
    f = Food("Eggs", 0, .35)
    s = Station("eggs", 3, 4, f)
    print s

if __name__ == "__main__":
    test()