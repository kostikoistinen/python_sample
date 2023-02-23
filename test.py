import numpy as np
import copy
'''
Class file of celestial objects. Also declaring of objects are included

    objectlist and cometlist attributes:
        Name (str):       Name of the object
        Mass (float):     Mass of the object in kilograms
        Distance (list):  x and y coordinates of the object in meters. 
                          It is calculated as distance to the zeroth object (not the center of mass).
        Velocity (list):  x and y velocities in meters/second
        Track (list):     Record of trajectory of the object in shape (:,2)
        color (str):      Color of the object in animation
        size (int):       Size of the object in animation
        radius (float):   Radius of the object in meters.
        
    Variables:
        Au (float):       Distance from Sun to Earth in meters. 1 Au = 1 Astronomical unit
'''

Au = 150e9 #Distance to the Sun from Earth.
numcom = 5 # Number of comets to be generated
class objectlist:
    name          = ""
    mass          = 0 #kg
    distance      = [0,0] #In Au, works as coordinates
    velocity      = [0,0] #In Au?
    track         = [0,0]
    color         = ""
    size          = 1
    radius        = 10 #meters
    pass
class comets:
    name = "Comet"
    mass = np.random.uniform(1e13,1e17)
    distance = [np.random.uniform(20,35),0]
    velocity = [0,np.random.uniform(1000,25000)]
    track = [0,0]
    color = "grey"
    size = 1
    radius = 10
    
Mars = objectlist()
Mars.name="Mars"
Mars.mass=6.39e23 
Mars.distance=[1.666*Au, 0]
Mars.velocity=[0,21970]
Mars.track = copy.deepcopy(Mars.distance)
Mars.color = "darkred"
Mars.size = 5
Mars.radius = 3400e3

Jupiter = objectlist()
Jupiter.name="Jupiter"
Jupiter.mass= 1.898e27
Jupiter.distance=[5.46*Au, 0]
Jupiter.velocity=[0,12400]
Jupiter.track = copy.deepcopy(Jupiter.distance)
Jupiter.color = "orange"
Jupiter.size = 20
Jupiter.radius = 70000e3

Earth = objectlist()
Earth.name="Earth"
Earth.mass= 5.972e24
Earth.distance=[1.0167*Au, 0]
Earth.velocity=[0,29290]
Earth.track = copy.deepcopy(Earth.distance)
Earth.color = "blue"
Earth.size = 5
Earth.radius = 6400e3

i=0 #Make comets
comet = np.array([comets() for _ in range(numcom)])
while i<len(comet):
    comet[i].name = "Comet"+str(i)
    comet[i].mass = np.random.uniform(1e14,1e16)
    comet[i].distance = [np.random.uniform(30,45)*Au,0]
    comet[i].velocity = [np.random.uniform(-10000,-25000),-1000]
    comet[i].track = copy.deepcopy(comet[i].distance)
    comet[i].size = int(np.random.uniform(1,3))
    comet[i].radius = np.random.uniform(5e3,50e3)
    i=i+1

Saturn = objectlist()
Saturn.name = "Saturn"
Saturn.mass = 5.683e26
Saturn.distance = [10.1238*Au,0]
Saturn.velocity = [0, 9090]
Saturn.track = copy.deepcopy(Saturn.distance)
Saturn.color = "orange"
Saturn.size = 16
Saturn.radius = 60000e3

Sun = objectlist()
Sun.name = "Sun"
Sun.mass = 2.0e30 
Sun.distance = [0,0]
Sun.velocity = [0,0]
Sun.track = copy.deepcopy(Sun.distance)
Sun.color = "yellow"
Sun.size = 40
Sun.radius = 700000e3

BH = objectlist()
BH.name ="Black hole"
BH.mass = 8*Sun.mass
BH.distance = [0, 10*Au]
BH.velocity = [-10000,0]
BH.track = copy.deepcopy(BH.distance)
BH.color = "black"
BH.size = 5
BH.radius = 50e3
#Comet, Saturn, SMBH, BH

BD = objectlist()
BD.name="Brown Dwarf"
BD.mass =5*Jupiter.mass
BD.distance =[10*Au,0]
BD.velocity = [-1000,1000]
BD.track = copy.deepcopy(BD.distance)
BD.color = "brown"
BD.size = 30
BD.radius = 80000e3


# Center of mass coordinates
# Parameters defined from main program
CM = objectlist()
CM.name = "Center of Mass"
CM.mass = 0
CM.distance = [0,0]
CM.velocity = [0,0]
CM.track = copy.deepcopy(CM.distance)
CM.color = "darkgrey"
CM.size = 5
