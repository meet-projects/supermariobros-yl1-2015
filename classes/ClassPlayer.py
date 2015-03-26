from turtle import *

class Player(Turtle):
	def __init__(self, canvas, x, y, height, width, power, dx, shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.height=height
		self.width=width
		self.power=power
		self.dx=dx
		self.dy= 0
		self.shape("square")


	def getHeight(self):
		return self.height

	def getwidth(self):
		return self.width

	def getpower (self): 
		return self.power

	def getDX (self):
		return self.dx

	def getDY (self):
		return self.dy

	def setDX (self,dx):
		self.dx=dx

	def setDY (self,dy):
		self.dy=dy

	def go_left(self):
		self.dx = -5

	def go_right(self):
		self.dx = 5

	def move(self):
		x1=self.xcor()
		y1=self.ycor()
		x2=x1+self.dx
		y2=y1+self.dy
		self.goto(x2, y2)
		if self.dy<0:
			self.dy=0
		self.dy=-self.dy
		self.dx=0;


	def getRadius(self):
		return 4

        

