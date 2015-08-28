## Venue class
## 



class Venue:
    
    def __init__(self, name, x, y, max_capacity_service, speed):
        
        self.name = name
        self.x = x
        self.y = y
        self.max_cap = max_capacity_service
        self.time_per_person = speed
        self.service_queue = []
        self.served = 0
        
    
    def __str__(self):
        return str(self.name) 
   

       
        
def test():
    v = Venue("hop", 40, 50, 5, 30)
    print v

if __name__ == "__main__":
    test()
       

