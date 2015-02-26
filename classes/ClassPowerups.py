import turtle

class powerups(turtle):
	def __init__(self,canvas,x,y,dx,dy,height,width,powertype):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.height = height
		self.width = width
		self.dx = dx
		self.dy = dy
		self.powertype = powertype
		

	def getheight(self):
		return self.height

	def getwidth(self):
		return self.width

	def getDX(self):
		return self.DX

	def getDY(self):
		return self.DY 

	def getDX(self,dx):
		self.dx = dx

	def getDY(self,dy):
		self.dy = dy
		
	def move(self):
		x = self.xcor()
		y = self.ycor()
		x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX 
		y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
		self.goto(x,y)
