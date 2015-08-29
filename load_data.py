## load_data.py
## the methods of this module parse comma-seperated value files and return a dictionary of 
## objects that have been instantiated with the data from the CSV
from venue import *
from classroom import *

def give_me_venue_dict():
    
    venues = {}
    
    file_str = "./static/venues.txt"
    
    # for each venue in data file, extract its attributes and populate venue dictionary for use in driver.py
    
    in_file = open(file_str, 'r')
    
    for line in in_file:
        
        x = line.strip()
        s = x.split(',')
        
        v = Venue(s[0],int(s[1]),int(s[2]),int(s[3]),int(s[4]))
      
        venues[s[0]] = v
    
    in_file.close()
    
    return venues



def give_me_classroom_dict():
    
    classes = {}
    
    file_str = "./static/classrooms.txt"
    
    # for each classroom in data file, extract its attributes and populate classroom dictionary for use in driver.py
    
    in_file = open(file_str, 'r')
    
    for line in in_file:
        
        x = line.strip()
        s = x.split(',')
        
        c = Classroom(s[0],int(s[1]),int(s[2]))
      
        classes[s[0]] = c
    
    in_file.close()
    
    return classes




def test():
   
   d = give_me_venue_dict()
   print d['foco']
   
   c = give_me_classroom_dict()
   print c['silsby hall']



if __name__ == "__main__":
    test()
