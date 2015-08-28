## Food class
## 

class Food:
    
    def __init__(self, name, idnum, chance):
        
        self.name = name
        self.idnum = idnum
        self.chance = chance

    def __str__(self):
        return "Student " + str(self.idnum) + "'s " + self.name
     
def test():
    f = Food("eggs", 1, .35)
    print f

if __name__ == "__main__":
    test()