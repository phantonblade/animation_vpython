from visual import *
import ruler

g=9.8
size=0.25

scene=display(title='bouncing projectile',center=(0,5,0),width=1200,height=800,background=(0.5,0.5,0))
floor=box(length=30,height=0.01,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_tail=True)
ruler1=ruler.ruler(pos=vector(15,0,1),unit=2.0,length=30.0,thickness=0.2)
ruler2=ruler.ruler(pos=vector(-15,0,1),unit=1.0,length=10.0,thickness=0.2)

ball.pos=vector(-15.0,10.0,0.0)
ball.v=vector(2.0,0.0,0.0)
dt=0.001
while ball.pos.x<15.0:
	rate(1000)
	ball.pos+=ball.v*dt
	ball.v.y+=-g*dt
	if ball.v.y<=size and ball.v.y<0:
		ball.v.y=-ball.v.y
print 'end'
