import.turtle

class player():
	def __init__(self,x,y,height,width,power,dx,dy)
		self.penup()
		self.goto(x,y)
		self.height=height
		self.width=width
		self.power=power
		self.dx=dx
		self.dy=dy
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
	def getDX (self,dx):
		self.dx=dx
	def getDY (self,dy):
		self.dy=dy
#we need help:P

