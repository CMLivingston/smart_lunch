## Classroom Class
## 
##

class Classroom:
    def __init__(self, name, x, y):
        
        self.name = name
        self.x = x
        self.y = y
        self.departure_queue = []
        self.exit_time = 5 # seconds 
  
    def __str__(self):
        return str(self.name) 
   
    def line_spot(self, student):
        if student in self.departure_queue:
            return self.departure_queue.index(student)

       
        
def test():
    c = Classroom("hop", 40, 50, 5, 30)
    print c

if __name__ == "__main__":
    test()