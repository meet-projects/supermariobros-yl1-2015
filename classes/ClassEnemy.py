from turtle import *

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500
class Enemy(Turtle):
	def __init__ (self, canvas, x, dx):
		RawTurtle.__init__(self, canvas)
		self.penup()
		self.goto(x,0)
		self.dx = dx
		self.y=	0
		self.shape("ssmallergoomba2.gif")




	def getsize(self):
	    return self.size

	def getRadius(self):
		return 20


	def getDX(self):
	    return self.dx

	def getDY(self):
	    return self.dy
	
	def setDX(self,dx):
	    self.dx = dx

	
	def getwidth(self,width):
		return self.width

	def getheight(self,height):
		return self.height	   

	def move(self):
		x = self.xcor()
		x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
		self.goto(x,0)
