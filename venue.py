## Venue class
## 

import Queue

class Venue:
    
    def __init__(self, name, x, y, chance, cashier_wait, stations):
        
        self.name = name
        self.x = x
        self.y = y
        self.chance = chance
        self.cashier_line = Queue.Queue(maxsize=0)
        self.cashier_wait = cashier_wait
        self.stations = stations
        self.served = 0
        
    def __str__(self):
        return str(self.name) + ", located at: (" + str(self.x) + ", " + str(self.y) + ")."
     
def test():
    v = Venue("The Hop", 40, 50, 40, 30)
    print v

if __name__ == "__main__":
    test()