from turtle import *
class Enemy(Turtle):
	def __init__ (self, canvas, x, y, dx, dy, height, width, EnemyType):
		RawTurtle.__init__(self, canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy= dy
		self.height = height
		self.width = width
		self.EnemyType = EnemyType
		self.shape("square")
	def move():
		x += dx
		y += dy
		self.goto(x,y)


screen.register_shape("assests/Goomba2.gif")
