from visual import*
from math import sin, cos

initialHeight = 4.6
initialVelocity = 24
Angle = 65

#Set up the display

scene1 = display(title ="Projectile motion",x=0,y=0,width=800,Height=600,range=10,background=color.white,center =(10,initialHeight,0)

# Create objects:
table = box(pos=(2,initialHeight - 1,0), size=(5,1,4))
ball1 = sphere(pos=(2,initialHeight -1,0),radius=1,
				color=color.green, make_trail = true)
ball2 = sphere(pos=(2,initialHeight+1,0),radius=1,
				color=color.red,make_trail = true)

floor = box(pos(0,0,0), size(100,0.25,10))
t=0
dt= 0.01
g=-32  #ft/s**2

Fgrav = vector(0,g*dt,0)
# velocity for ball1

ballv = vector(initialVelocity*cos(Angle*pi/180),initialVelocity*sin(Angle*pi/180),0)

#start to be a motion
while True:
	rate(30) #speed up
	ball1v = ball1v + Fgrav
	ball1.pos += ball1v*dt
	ball2.pos = (initialVelocity*cos(Angle*pi/180)*t,
				iniitialHeight + initialVelocity*t*sin(Angle*pi/180)-16*t**2)
	if ball1.y < 0: #when ball1 hits the ground.....
		print "ball1.pos = ",ball1.pos,"t = ",t
		print "ball2.pos = ",ball2.pos
		break
	t += dt
