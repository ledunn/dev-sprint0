# Flower excercise (4.2) from Week 0

# Name: Lauren Dunn


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay=.01

t=bob
# This is where you put code to move bob
def petal(t,r,theta):
	for i in range(2):
		arc(t,r,theta)
		lt(t, 180-angle)

def flower(t,n,r,theta):
	for i in range(n):
		petal(t,r,theta)
		lt(t,theta)

flower(bob,7,60,60)





wait_for_user()					

