import numpy as np
import copy
import random
from prettytable import PrettyTable
#Simulation: Solar system objects

#Classes------------------------------------------------
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
#--------------------------------------------------------
#Objects
Mercury = objectlist()
Mercury.name="Mercury"
Mercury.mass= 3.30e23
Mercury.distance=[0.4667*Au, 0]
Mercury.velocity=[0,46000]
Mercury.track = copy.deepcopy(Mercury.distance)
Mercury.color = (125/255, 125/255, 125/255)
Mercury.size = 5
Mercury.radius = 2440e3     
    
Venus = objectlist()
Venus.name="Venus"
Venus.mass= 4.867e24 
Venus.distance=[0.72*Au, 0]
Venus.velocity=[0,34790]
Venus.track = copy.deepcopy(Venus.distance)
Venus.color = (255/255, 204/255, 102/255)
Venus.size = 5
Venus.radius = 6100e3  
    
Earth = objectlist()
Earth.name="Earth"
Earth.mass= 5.972e24
Earth.distance=[1.0167*Au, 0]
Earth.velocity=[0,29290]
Earth.track = copy.deepcopy(Earth.distance)
Earth.color = (0/255, 128/255, 255/255)
Earth.size = 5
Earth.radius = 6400e3    
    
Mars = objectlist()
Mars.name="Mars"
Mars.mass=6.39e23 
Mars.distance=[1.666*Au, 0]
Mars.velocity=[0,21970]
Mars.track = copy.deepcopy(Mars.distance)
Mars.color = (204/255, 51/255, 0/255)
Mars.size = 5
Mars.radius = 3400e3

Jupiter = objectlist()
Jupiter.name="Jupiter"
Jupiter.mass= 1.898e27
Jupiter.distance=[5.46*Au, 0]
Jupiter.velocity=[0,12400]
Jupiter.track = copy.deepcopy(Jupiter.distance)
Jupiter.color = (255/255, 215/255, 102/255)
Jupiter.size = 20
Jupiter.radius = 70000e3

Saturn = objectlist()
Saturn.name = "Saturn"
Saturn.mass = 5.683e26
Saturn.distance = [10.1238*Au,0]
Saturn.velocity = [0, 9090]
Saturn.track = copy.deepcopy(Saturn.distance)
Saturn.color = (231/255, 184/255, 128/255)
Saturn.size = 16
Saturn.radius = 60000e3

Uranus = objectlist()
Uranus.name = "Uranus"
Uranus.mass = 8.6810e25
Uranus.distance = [20.11*Au,0]
Uranus.velocity = [0, 6800]
Uranus.track = copy.deepcopy(Uranus.distance)
Uranus.color = (127/255, 179/255, 213/255)
Uranus.size = 12
Uranus.radius = 25362e3

Neptune = objectlist()
Neptune.name = "Neptune"
Neptune.mass = 1.0243e26
Neptune.distance = [30.07*Au,0]
Neptune.velocity = [0, 5430]
Neptune.track = copy.deepcopy(Neptune.distance)
Neptune.color = (67/255, 112/255, 153/255)
Neptune.size = 12
Neptune.radius = 24622e3


i=0 #Make comets
comet = np.array([comets() for _ in range(numcom)])
while i<len(comet):
    comet[i].name = "Comet"+str(i)
    comet[i].mass = np.random.uniform(1e14,1e16)
    comet[i].distance = [random.choice([-1, 1])*np.random.uniform(30,45)*Au,
                         random.choice([-1, 1])*np.random.uniform(-5,5)*Au]

    comet[i].velocity = [0,np.random.uniform(-1000,1000)] #small velocities far away
    comet[i].track = copy.deepcopy(comet[i].distance)
    comet[i].size = int(np.random.uniform(1,3))
    comet[i].radius = np.random.uniform(5e3,50e3)
    i=i+1

Sun = objectlist()
Sun.name = "Sun"
Sun.mass = 2.0e30 
Sun.distance = [0,0]
Sun.velocity = [0,0]
Sun.track = copy.deepcopy(Sun.distance)
Sun.color = "yellow"
Sun.size = 40
Sun.radius = 700000e3

print("Default simulation: Solar system planets and a comet")
l_obj = [Sun,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune,comet[0]]

table = PrettyTable()
table.field_names = ["Object", "Mass", "Distance x", "Distance y", "Radius", "Velocity x", "Velocity y"]
for a in range(len(l_obj)):
	table.add_row([l_obj[a].name,
	"{:.0e}".format(l_obj[a].mass),
	"{:.0e}".format(l_obj[a].distance[0]),
	"{:.0e}".format(l_obj[a].distance[1]), 
	"{:.0e}".format(l_obj[a].radius),
	"{:.0e}".format(l_obj[a].velocity[0]),
	"{:.0e}".format(l_obj[a].velocity[1])])
print(table)

