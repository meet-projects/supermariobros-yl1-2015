import.turtle

class player():
	def __init__(self,x,y,height,width,power,dx)
		self.penup()
		self.goto(x,y)
		self.height=height
		self.width=width
		self.power=power
		self.dx=dx
		self.dy=0
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


	def move(self):
		x1=self.xcor()
		y1=self.ycor()
		x2=x1+self.dx
		y2=y1+self.dy
		if self.dy<0
			self.dy=0
		self.dy=-self.dy

	def getRadius(self):
        return 4


turtle.mainloop()

        

