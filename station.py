## Station class
## 

import Queue
import food

class Station:
    
    def __init__(self, name, cook_time, max_items, food):
        
        self.name = name
        self.cook_time = cook_time
        self.food_line = []
        self.cook_surface = Queue.Queue(maxsize=max_items)
        self.food = food
        
    def __str__(self):
        return str(self.name) 
     
def test():
    f = Food("Eggs", 0, .35)
    s = Station("eggs", 3, 4, f)
    print s

if __name__ == "__main__":
    test()