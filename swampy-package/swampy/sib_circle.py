from TurtleWorld import *
world= TurtleWorld()
bob=Turtle()

import math
print math.pi

def circle(t, n, r):
	circumfrence=2*math.pi*r
	length=circumfrence/360
	for i in range(n):
		fd(t,length)
		lt(t, 360/n)
		

bob.delay=0.01
circle(bob,360,50)


	
