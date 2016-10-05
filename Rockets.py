import sys
import os
from math import cos, sin
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Coordinates:
    def __init__(self):
        self.loc = [0]*3 #makes an array of three intagers: (lat, lon, alt), initialized at 0
        self.tim = 0; 

class rocket:
    def __init__(self):
        self.lat = 0;
        self.lon = 0;
        self.alt = 0;
        self.spd = 0;
        self.acc = 0;

    def print_status(self):
        print "Latitude: %d\nLongitude: %d\nAltitude: %d\nSpeed: %d\nAcceleration: %d\n" % (
            self.lat, self.lon, self.alt, self.spd, self.acc)    

class Flight_main:
    coord_num = 0
    def __init__(self):
        self.c = [] #creates a blank array to be filled with Coordinate objects
        data = [0]*4
    
    def get_coordinate(self):
        f = open('coordinates.txt', 'r+')
        str = f.readline()
 
        while len(str) > 4:  #reads in a line as a string from coordinates.txt until the next line is an empty string (realatively)
            i = self.coord_num

            self.data = str.split() #split makes the string into an array of 3 strings seperated at each space
            self.c.append(Coordinates()) #increases array size of Coordinate objects
            self.c[i].loc[0] = float(self.data[0])
            self.c[i].loc[1] = float(self.data[1])
            self.c[i].loc[2] = float(self.data[2])  
            
            self.coord_num += 1  # keeps track of how many data coordinates are recorded
            str = f.readline() # reads next line
        f.close

    def print_all_coordinates(self):
        for i in range (0, len(self.c)):
            print "Latitude: %f Longitude: %f Altitude: %f x: %d\n" % (
                self.c[i].loc[0], self.c[i].loc[1], self.c[i].loc[2], i)

    def generate_3d_graph(self): #this is where the matplotlib model is generated
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        for i in range (0, len(self.c)):
            ax.scatter(self.c[i].loc[0], self.c[i].loc[1], self.c[i].loc[2], c=40)

        plt.show()

def generate_coordinates():
    coords = [0]*3
    f = open('coordinates.txt', 'w')
    for i in range (-10, 11):
        coords[0] = i
        coords[1] = -i
        coords[2] = -i**2 + 100

        f.write(str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2]) + "\n")

    f.close


def main():
    generate_coordinates()
    
    flight = Flight_main()
    flight.get_coordinate()
    flight.print_all_coordinates()
    flight.generate_3d_graph()

    os.system("pause")
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))
