from visual import *
from math import sin, cos

initialHeight = 4.6
initialVelocity = 24
Angle = 65

#set up the display window
scene1 = display(title = "test",
                x=0, y=0, width=800, height=600,
                range=10, background=color.black,
                center = (10,initialHeight,0))

#Create our objects:
table = box(pos=(3,initialHeight - 1,0), size=(5,1,4))
ball1 = sphere(pos=(3,initialHeight,0),radius=1,
                 color=color.green, make_trail = true)

ball2 = sphere(pos=(3,initialHeight,0),radius=1,
                 color=color.red, make_trail = true)

floor = box(pos=(initialHeight-1,initialHeight-1,initialHeight-1), size=(100,0.25,10))

t=0
dt = 0.05
g = -32 #ft/s**2

Fgrav = vector(0,g*dt,0)

#velocity vector for ball1:
ball1v = vector(initialVelocity*cos(Angle*pi/180),
                initialVelocity*sin(Angle*pi/180),0)


#This loop puts it into motion:
while True:
    rate(30)#Speed
    ball1v = ball1v +Fgrav
    ball1.pos += ball1v*dt
    ball2.pos = (initialVelocity*cos(Angle*pi/180)*t,
                 initialHeight + initialVelocity*t*sin(Angle*pi/180) - 16*t**2)
    if ball1.y < 0: #ball1 hit the ground
        print "ball1.pos = ",ball1.pos,"t = ",t
        print "ball2.pos = ",ball2.pos
        break
	t += dt
