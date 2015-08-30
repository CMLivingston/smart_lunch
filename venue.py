## Venue class
## 

class Venue:
    
    def __init__(self, name, x, y, chance, cashier_wait, stations):
        
        self.name = name
        self.x = x
        self.y = y
        self.chance = chance
        self.cashier_line = []
        self.cashier_wait = cashier_wait
        self.stations = stations
        self.served = 0
        
    def __str__(self):
        return str(self.name)

    def line_spot(self, student):
        if student in self.cashier_line:
            return self.cashier_line.index(student)

def test():
    v = Venue("The Hop", 40, 50, 40, 30)
    print v

if __name__ == "__main__":
    test()