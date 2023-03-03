#Simulation of Super massive black hole vicinity
#
import numpy as np
import copy
import random
import math
from prettytable import PrettyTable

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
Sun.distance = [2000*Au,0]
Sun.velocity = [-10000,0]
Sun.track = copy.deepcopy(Sun.distance)
Sun.color = "yellow"
Sun.size = 8
Sun.radius = 700000e3
#---------------------
#Generate random stars ranging from M to B type:
i=0
stars = np.array([objectlist() for _ in range(15)])
b=1
a=1
f=1
g=1
k=1
m=1

while i<len(stars):
	stars[i].mass = np.random.uniform(0.1*Sun.mass,5*Sun.mass)**0.99

	stars[i].distance = [np.random.uniform(-1000*Au,1000*Au),np.random.uniform(-1000*Au,1000*Au)]
	stars[i].velocity = [random.uniform(-1000000,1000000),random.uniform(-1000000,1000000)]
	stars[i].track = copy.deepcopy(stars[i].distance)
	if stars[i].mass<0.45*Sun.mass:
		stars[i].name = "M-type"+str(m)
		stars[i].radius = 0.6*Sun.radius
		stars[i].color = "red"
		stars[i].size = 5
		m=m+1
	elif stars[i].mass<0.8*Sun.mass and stars[i].mass>0.45*Sun.mass :
		stars[i].name = "K-type"+str(k)
		stars[i].radius = 0.8*Sun.radius
		stars[i].color = "orange"
		stars[i].size = 6
		k=k+1
	elif stars[i].mass<1.04*Sun.mass and stars[i].mass>0.8*Sun.mass :
		stars[i].name = "G-type"+str(g)
		stars[i].radius = 1.08*Sun.radius
		stars[i].color = "yellow"
		stars[i].size = 8
		g=g+1
	elif stars[i].mass<1.4*Sun.mass and stars[i].mass>1.04*Sun.mass :
		stars[i].name = "F-type"+str(f)
		stars[i].radius = 1.3*Sun.radius
		stars[i].color = "yellow"
		stars[i].size = 10
		f=f+1
	elif stars[i].mass<2.1*Sun.mass and stars[i].mass>1.4*Sun.mass :
		stars[i].name = "F-type"+str(a)
		stars[i].radius = 1.6*Sun.radius
		stars[i].color = "darkblue"
		stars[i].size = 15
		a=a+1
	elif stars[i].mass<16*Sun.mass and stars[i].mass>2.1*Sun.mass :
		stars[i].name = "B-type"+str(b)
		stars[i].radius = 3.0*Sun.radius
		stars[i].color = "blue"
		a=a+1
		stars[i].size = 20
	i=i+1

BH = objectlist()
BH.name = "Black Hole"
BH.mass = 1000000*Sun.mass
BH.distance = [0,0]
BH.velocity = [0,0]
BH.track = copy.deepcopy(BH.distance)
BH.color = "black"
BH.size = 10
BH.radius = 10*Sun.radius

l_obj = [Sun,BH]
for j in range(len(stars)):
	l_obj = np.append(l_obj,stars[j])
print("Simulation: Super massive black hole")
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





