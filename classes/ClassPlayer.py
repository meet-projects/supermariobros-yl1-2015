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
		self.direction = 0


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
		self.direction = 1

	def go_right(self):
		self.dx = 5
		self.direction = 2
	
	def jump(self):
		if self.ycor() == 0:
			self.dy = 1


	def move(self):
		x1 = self.xcor() + self.dx
		y1 = self.ycor() + self.dy
		if(y1 > 200):
			self.dy=-self.dy
		elif(y1<0):
			self.dy = 0
			y1 = 0
		self.goto(x1, y1)
		if (self.dy == 0 and self.direction == 0):
			self.dx = 0
		self.direction = 0

	def getRadius(self):
		return 4

        

