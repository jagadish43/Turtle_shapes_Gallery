from turtle import Turtle

def Circle(data):
	for i in range(100): # The parameter of Circle is 100. As I considered  
		data.fd(10)      # Length for forward direction. 
		data.lt(360/100) # Angle of Circle is 3.6. #Formula angle = total angle/parameter = 360/100 = 3.6

def Triangle(data):
	for i in range(3): #The parameter of Triangle is 3.
		data.fd(100)   # Length for forward direction.
		data.lt(120)    # Angle of triangle is 120. #Formula angle = total angle/parameter = 360/3 = 120

def Square(data):
	for i in range(4): #The parameter of square is 4.
		data.fd(100)   # Length for forward direction.
		data.lt(90)    # Angle of square is 90. #Formula angle = total angle/parameter = 360/4 = 90

def Pantagon(data):
	for i in range(5): # The parameter of pantagon is 5. 
		data.fd(100)   # Length for forward direction. 
		data.lt(72)    # Angle of pantagon is 72. #Formula angle = total angle/parameter = 360/5 = 72

def Hexagon(data):
	for i in range(6): # The parameter of Hexagon is 5. 
		data.fd(100)   # Length for forward direction. 
		data.lt(60)    # Angle of Hexagon is 60. #Formula angle = total angle/parameter = 360/6 = 60
	
def Star(data):
	for i in range(5): # The parameter of Star is 5. 
		data.fd(100)   # Length for forward direction. 
		data.lt(144)   # Angle of Star is 144. #Formula angle = total angle/parameter = 360/5 * 2 = 144

def Rectangle(data):
	for i in range(2): #The parameter of Rectangle is 2. Considering only 2 sides
		data.fd(150)   # Length for forward direction.
		data.lt(90)    # Angle of Rectangle is 180. #Formula angle = total angle/parameter = 360/4 = 180 
		data.fd(80)   #Width of the rectangle
		data.lt(90)    #But here considering only 2 sides soo 180/2 = 90   


