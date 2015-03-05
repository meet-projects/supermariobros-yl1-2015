from turtle import *
class Enemy(Turtle):
	def __init__ (self, canvas, x, y, dx, dy, height, width, ):
		RawTurtle.__init__(self, canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy= dy
		self.height = height
		self.width = width	
		self.shape("triangle")


	def getsize(self):
	    return self.size

	def getDX(self):
	    return self.dx

	def getDY(self):
	    return self.dy
	
	def setDX(self,dx):
	    self.dx = dx

	def setDY(self,dy):
	    self.dy = dy	

	def getwidth(self,width):
		return self.width

	def getheight(self,height):
		return self.height	   

	def move():
		x = self.xcor()
		y = self.ycor()
		x += self.dx
		y += self.dy
		self.goto(x,y)