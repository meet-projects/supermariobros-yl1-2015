from turtle import *
class Blocks(Turtle):
	def __init__(self,canvas,dx,dy,x,y,height,width):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("Smallbrick.gif")

	def getDX(self):
	    return self.dx

	def getDY(self):
	    return self.dy
	
	def setDX(self,dx):
	    self.dx = dx

	def setDY(self,dy):
	    self.dy = dy
	
	def move(self):
		self.goto(self.xcor()+dx,self.ycor()+dy)