#!/usr/bin/python
#vim:set fileencoding:utf-8
from visual import *

g = 9.8             #gravtational acceration
size = 0.05         #ball 
r = 0.5             #ball_radius
k = 10              #spring constant
m = 0.2             #mass

scene = display(width=800, height=800, center=(0, -r*0.6, 0), background=(0.5,0.5,0))  #³]©wµe­±
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)                    #µe¤ÑªáªO
ball = sphere(radius = size,  color=color.red)                              #µe²y
spring = helix(radius=0.02, thickness =0.01)                                #µe¼uÂ®,¤£°ÊºÝ¦b(0,0,0)

ball.pos0 = vector(0, -r, 0) 					#²yªºªì¦ì¸m¡A§Y¼uÂ®¹B°ÊºÝªºªì¦ì¸m
ball.pos = vector(0, -r , 0)        					#
ball.v = vector(0, 0, 0)            					

dt = 0.00001
while True:
    rate(100000)
    spring.axis = ball.pos - spring.pos 		
    ball.a = vector(0, - g - k * (ball.pos.y - ball.pos0.y )/m , 0)

    ball.v +=   ball.a*dt 	#setting the ball velocity
    ball.pos += ball.v*dt
