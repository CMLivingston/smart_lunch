## Classroom Class
## 
##


class Classroom:
    def __init__(self, name, x, y):
        
        self.name = name
        self.x = x
        self.y = y
        self.departure_queue = []
        
  
    def __str__(self):
        return str(self.name) 
   

       
        
def test():
    c = Classroom("hop", 40, 50, 5, 30)
    print c

if __name__ == "__main__":
    test()
       

