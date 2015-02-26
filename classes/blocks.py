import turtle
class blocks(turtle):
	def __init__(self,canvas,dx,dy,x,y,height,width):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.size = size
		self.dx = dx
		self.dy = dy
		self.shape("squer"+str(size)

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


