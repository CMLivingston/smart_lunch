## Venue class
## 

from queue import *

class Venue:
    
    def __init__(self, name, x, y, chance):
        
        self.name = name
        self.x = x
        self.y = y
        self.chance = chance
        self.cashier_line = queue.Queue(maxsize=0)
        self.served = 0
        
    def __str__(self):
        return str(self.name) 
     
def test():
    v = Venue("hop", 40, 50, 40)
    print v

if __name__ == "__main__":
    test()