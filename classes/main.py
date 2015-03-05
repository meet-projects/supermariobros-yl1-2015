import turtle 

  def getRadius(self):
        return 4

def intersect(Player,Enemy):
        dist = math.sqrt((Player.xcor() - Enemy.xcor())**2 + (Player.ycor() - Enemy.ycor())**2)
        
        radius1 = Player.getRadius()
        radius2 = Enemy.getRadius()
      
        if dist <= radius1+radius2:
            return touching
        else:
            return no touching

def main():
    root = tkinter.Tk()
    root.title("Super Mario")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)

    def quitHandler():
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    
    ship = Player(cv,0,0,0,0)
    
    Enemy = []

 def play():
        ship.move()
        for Enemy in Enemies:
            if (intersect(ship,Enemy)):
                print("You Failed")
                quitHandler()
            Enemy.move()
        
        screen.ontimer(play, 10)
   
    screen.onkeypress(ship.turnLeft,"Left")
    screen.onkeypress(ship.turnRight,"Right")
    screen.onkeypress(ship.fireEngine,"Up")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
  main()
  


turtle.mainloop()
