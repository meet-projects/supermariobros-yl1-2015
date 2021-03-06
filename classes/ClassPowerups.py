import turtle

class Powerups(turtle):
	def __init__(self,canvas,x,y,dx,dy,height,width,shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.height = height
		self.width = width
		self.dx = dx
		self.dy = dy
		self.shape="circle"
		

	def getheight(self):
		return self.height

	def getwidth(self):
		return self.width

	def getRadius(self):
		return 10

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
		self.goto(x+dx, y+dy)

	def go_left(self):
		self.dx = -5

	def go_right(self):
		self.dx = 5