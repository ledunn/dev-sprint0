from TurtleWorld import *
world= TurtleWorld()
bob=Turtle()

def arc(t, n, length, theta):
	theta=360/n
	arc_length=circumfrence*theta
	for i in range (n):
		fd(t, length)
		lt(t,theta)

arc(bob,120,theta)