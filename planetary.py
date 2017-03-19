from visual import *
#G*M*m = 10000

secene = display(width=600 ,height=600, center=(0,5,0))

Sun = sphere(pos=(0,0,0), radius=100, color=color.orange)
earth = sphere(pos=(-200,0,0),radius=10,materials=materials.plastic,make_trail = true)
earthv = vector(0,0,5)
for i in range(1000):
	rate(100)
	earth.pos = earth.pos + earthv
	dis = (earth.x**2+ earth.y**2+earth.z**2)**0.5
	RadialVector = (earth.pos-Sun.pos)/dis
	Fgrav= - 10000*RadialVector/dis**2
	earthv = earthv +Fgrav
	earth.pos += earthv
	if dis <= Sun.radius:break
