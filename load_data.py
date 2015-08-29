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

def make_foods(filepath):

    in_file = open(filepath, 'r')
    foods = []

    for line in in_file:
        # make an array of strings seperated by ,
        x = line.strip()
        s = x.split(',')
        f = Food(s[0], s[1])
        foods.append(f)

    return foods

def make_stations(filepath, foods):

    in_file = open(filepath, 'r')
    stations = {}
    hop_stations = []
    collis_stations = []
    novack_stations = []
    
    for line in in_file:
        # make an array of strings separated by ,
        x = line.strip()
        s = x.split(',')
        station_name = s[0]
        for food in foods:
            if station_name == food.name:
                station = Station(s[0], s[1], s[2], food)
                if s[3] == "hop":
                    hop_stations.append(station)
                elif s[3] == "collis":
                    collis_stations.append(station)
                break

    stations["hop_stations"] = hop_stations
    stations["collis_stations"] = collis_stations
    stations["novack_stations"] = novack_stations

    return stations

def make_venues(filepath, stations):
    
    venues = {}
    
    # for each venue in data file, extract its attributes and populate venue dictionary for use in driver.py
    in_file = open(filepath, 'r')
    
    for line in in_file:
        # make an array of strings seperated by ,
        x = line.strip()
        s = x.split(',')
        # construct a veune for placement into dict
        v = Venue(s[0],s[1],s[2],s[3],s[4],stations[s[5]])
      
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
   
    foods = make_foods("./static/foods.txt")
    stations = make_stations("./static/stations.txt", foods)
    venues = make_venues("./static/venues.txt", stations)
    for food in foods:
        print food.name, food.chance
    for station in stations:
        for s in stations[station]:
            print s.name
    for venue in venues:
        print venues[venue].name
        for station in venues[venue].stations:
            print station
            



if __name__ == "__main__":
    test()
