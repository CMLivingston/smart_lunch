## Food class
## 

class Food:
    
    def __init__(self, name, chance):
        
        self.name = name
        self.chance = chance

    def __str__(self):
        return self.name
     
def test():
    f = Food("eggs", 1, .35)
    print f

if __name__ == "__main__":
    test()