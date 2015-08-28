## Station class
## 

import Queue

class Station:
    
    def __init__(self, name, cook_time, max_items):
        
        self.name = name
        self.cook_time = cook_time
        self.food_line = Queue.Queue(maxsize=0)
        self.cook_surface = Queue.Queue(maxsize=max_items)
        
    def __str__(self):
        return str(self.name) 
     
def test():
    s = Station("eggs", 3, 4)
    print s

if __name__ == "__main__":
    test()