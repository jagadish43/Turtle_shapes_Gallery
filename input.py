from math_shapes import *
import turtle

print('''Supported Shapes:
--> Circle
--> Triangle
--> Square
--> Pantagon
--> Hexagon
--> Star
--> Rectangle''')

input("Press Enter to Start")
print("---------------------")

Shape = input("Enter the shape to draw:").title()

data = Turtle()

screen = data.getscreen()
screen.setup(width=600, height=700) 
screen.title("Drawing Shapes")  

# Try to set focus using the Turtle's screen window manager
canvas = screen.getcanvas().winfo_toplevel()
canvas.call('wm', 'attributes', '.', '-topmost', '1')  # Bring to front
canvas.call('wm', 'attributes', '.', '-topmost', '0')  # Allow other windows on top

if Shape=="Circle":
	Circle(data)
elif Shape=="Triangle":
	Triangle(data)
elif Shape=="Square":
	Rectangle(data)
elif Shape=="Pantagon":
	Pantagon(data)
elif Shape=="Hexagon":
	Hexagon(data)
elif Shape=="Star":
	Star(data)
elif Shape=="Rectangle":
	Rectangle(data)
else:
	print("Pls enter the correct shape")

print(f"The {Shape} has been drawn.")
