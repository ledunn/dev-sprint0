# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# # This is where you put code to move bob
# #Exercise 4.1:
# # Create a polygon function. Open up sib_polygon.py and place your code for the following excercise there.
# #Add a function named square() that uses a for loop to draw a square and puts the turtle back where it started. 
# #Write code to test the function.

# def square(bob):
#   for i in range (4):
#     fd(bob, 100)
#     lt(bob)

# square(bob)    

   
# #Generalize the function so that it takes a turtle and a length as parameters.


def square(bob, 100):
 	for i in range (4):
 		fd(bob, 100)
 		lt(bob)
 square(bob, 100)

def square(t, length):
 	for i in range (4):
 		fd(t, length)
 		lt(t)
 square(t, length)

#Generalize the function so that it takes an additional parameter, n, and draws an n-sided regular polygon.
#You might want to change the name of the function to polygon.
#Hint: lt() and rt() take an optional second argument that specifies the number of degrees to turn.
#Another hint: The angles of an n-sided regular polygon are 360/n degrees.
t=bob
def polygon(t, n, length):
	for i in range (n):
		fd(t,length)
		lt(t, 360/n)

polygon(bob, 6, 100)

#Write a function called circle() that takes a turtle and radius as parameters
#and that draws an approximate circle by invoking polygon with an appropriate length and number of sides.  
#Test your function with a range of values of r.
#Figure out the circumference of the circle and make sure that length * n = circumference.
import math
print math.pi














wait_for_user()					
