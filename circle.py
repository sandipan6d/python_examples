#!/usr/bin/python
from __future__ import print_function
import sys

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " radius")
	exit()

input_radius = sys.argv[1]

if not input_radius.isdigit():
	print('Input provided as radius should be integer data type!')
	exit()


class Circle(object):

    # class object attribute
	pi = 3.14

	def __init__(self,radius):

		self.radius = int(radius)

	def get_radius(self):

		return self.radius
        
	def get_area(self):

		area = Circle.pi * (self.radius**2)
		return area

	def get_perimeter(self):

		perimeter = 2 * Circle.pi * self.radius
		return perimeter

#class inheritance
class Diameter(Circle):

	def __init__(self,radius):
		Circle.__init__(self,radius)

	def get_diameter(self):
		return 2 * self.get_radius()



## Object initialization

c = Circle(radius = input_radius)
d = Diameter(radius = input_radius)

print('Area of the circle: {X}'.format(X=c.get_area()))
print('Perimeter of the circle: {Y}'.format(Y=c.get_perimeter()))
print('Diameter: {Z}'.format(Z=d.get_diameter()))



