## Food class
## 

class Food:
    
    def __init__(self, name, chance):
        
        self.name = name
        self.chance = chance
        self.cook_start = 0 # will edit this field once food starts cooking

    def __str__(self):
        return self.name
     
def test():
    f = Food("eggs", 1, .35)
    print f

if __name__ == "__main__":
    test()