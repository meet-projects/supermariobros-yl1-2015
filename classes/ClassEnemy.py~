from turtle import *
class Enemy(Turtle):
	def __init__ (self, canvas, x, dx):
		RawTurtle.__init__(self, canvas)
		self.penup()
		self.goto(x,7)
		self.dx = dx
		self.y=	7


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


