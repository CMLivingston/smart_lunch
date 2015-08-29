## load_data.py
## the methods of this module parse comma-seperated value files and return a dictionary of 
## objects that have been instantiated with the data from the CSV
from venue import *
from classroom import *
from station import *
from food import *
from student import *
import random
import math
import copy

def give_me_stations():

    # create foods first...
    eggs_chance = 0.35
    eggs = Food("Eggs", eggs_chance)
    stirfry_chance = 0.35
    stirfry = Food("Stirfry", stirfry_chance)
    grill_chance = 0.5
    grill = Food("Grill Item", grill_chance)
    sandwich_chance = 0.3
    sandwich = Food("Sandwich", sandwich_chance)

    # ...then create stations...
    
    stations = {}
    
    egg_cook = 3
    egg_max = 4
    egg_station = Station("Eggs", egg_cook, egg_max, eggs)
    stirfry_cook = 5
    stirfry_max = 4
    stirfry_station = Station("Stirfry", stirfry_cook, stirfry_max, stirfry)
    grill_cook = 4
    grill_max = 10
    grill_station = Station("Grill", grill_cook, grill_max, grill)
    sandwich_cook = 4
    sandwich_max = 2
    sandwich_station = Station("Sandwich", sandwich_cook, sandwich_max, sandwich)

    # ...then create station arrays...
    hop_stations = []
    collis_stations = []
    novack_stations = [] # left empty
    
    # append whatever we want
    hop_stations.append(grill_station)
    hop_stations.append(sandwich_station)
    collis_stations.append(egg_station)
    collis_stations.append(stirfry_station)


    # add them to the dict for loading
    stations["hop_stations"] = hop_stations
    stations["collis_stations"] = collis_stations
    
    # give to dict back to caller so venues can ve constructed above in "give_me_venues"
    return stations
    


def give_me_venue_dict():
    
    venues = {}
    
    # get the stations created below
    stations = give_me_stations()
    
    # for each venue in data file, extract its attributes and populate venue dictionary for use in driver.py
    file_str = "./static/venues.txt"
    in_file = open(file_str, 'r')
    
    for line in in_file:
        # make an array of strings seperated by ,
        x = line.strip()
        s = x.split(',')
        
        # make empty station array
        arrayOfStations = []
        data_len = len(s)
        # fill with indexed 5 and up of s array (should be which stations it offers)
        if (data_len > 5):
            i = 5
            while (i != data_len):
                station_obj = stations[s[i]]
                arrayOfStations.append(station_obj)
                i = i+1
        else:
            print "(FUCK):data_err:stations are not input correctly in venues.txt"
        
        # construct a veune for placement into dict
        v = Venue(s[0],int(s[1]),int(s[2]),float(s[3]),int(s[4]), arrayOfStations)
      
        # put name string as index of dict
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
