#Simulation of Stars birth
#One star has planets (Sun has Venus & Earth)
import numpy as np
import copy
import random
import math
from prettytable import PrettyTable
#Simulation: Stellar birth zone

#Classes------------------------------------------------
Au = 150e9 #Distance to the Sun from Earth.
numcom = 50 # Number of comets to be generated
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

Sun = objectlist()
Sun.name = "Sun"
Sun.mass = 2.0e30 
Sun.distance = [0,0]
Sun.velocity = [0,0]
Sun.track = copy.deepcopy(Sun.distance)
Sun.color = "yellow"
Sun.size = 40
Sun.radius = 700000e3

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
#---------------------
#Generate random stars ranging from M to B type:
i=0
stars = np.array([objectlist() for _ in range(20)])
b=1
a=1
f=1
g=1
k=1
m=1

while i<len(stars):
	stars[i].mass = np.random.uniform(0.1*Sun.mass,5*Sun.mass)**0.99

	stars[i].distance = [np.random.uniform(-100*Au,100*Au),np.random.uniform(-100*Au,100*Au)]
	stars[i].velocity = [random.uniform(-10000,10000),random.uniform(-10000,10000)]
	stars[i].track = copy.deepcopy(stars[i].distance)
	if stars[i].mass<0.45*Sun.mass:
		stars[i].name = "M-type"+str(m)
		stars[i].radius = 0.6*Sun.radius
		stars[i].color = "red"
		stars[i].size = 20
		m=m+1
	elif stars[i].mass<0.8*Sun.mass and stars[i].mass>0.45*Sun.mass :
		stars[i].name = "K-type"+str(k)
		stars[i].radius = 0.8*Sun.radius
		stars[i].color = "orange"
		stars[i].size = 30
		k=k+1
	elif stars[i].mass<1.04*Sun.mass and stars[i].mass>0.8*Sun.mass :
		stars[i].name = "G-type"+str(g)
		stars[i].radius = 1.08*Sun.radius
		stars[i].color = "yellow"
		stars[i].size = 40
		g=g+1
	elif stars[i].mass<1.4*Sun.mass and stars[i].mass>1.04*Sun.mass :
		stars[i].name = "F-type"+str(f)
		stars[i].radius = 1.3*Sun.radius
		stars[i].color = "yellow"
		stars[i].size = 50
		f=f+1
	elif stars[i].mass<2.1*Sun.mass and stars[i].mass>1.4*Sun.mass :
		stars[i].name = "F-type"+str(a)
		stars[i].radius = 1.6*Sun.radius
		stars[i].color = "darkblue"
		stars[i].size = 60
		a=a+1
	elif stars[i].mass<16*Sun.mass and stars[i].mass>2.1*Sun.mass :
		stars[i].name = "B-type"+str(b)
		stars[i].radius = 3.0*Sun.radius
		stars[i].color = "blue"
		a=a+1
		stars[i].size = 70
	i=i+1

l_obj = [Sun,Venus,Earth]
for j in range(len(stars)):
	l_obj = np.append(l_obj,stars[j])
print("Simulation: Stellar birth zone")
#for a in range(len(l_obj)):
#	print(l_obj[a].name, "{:.0e}".format(l_obj[a].mass))
	
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









