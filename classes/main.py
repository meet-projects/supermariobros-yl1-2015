#This is a demo project for meet Yearlong 2014-15 Y1
from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import timeit
from ClassPlayer import Player

#These Four variables are the borders of the game world
screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500


def intersect(Player_var,Enemy_var):
    dist = math.sqrt((Player_var.xcor() - Enemy_var.xcor())**2 + (Player_var.ycor() - Enemy_var.ycor())**2)
    radius1 = Player_var.getRadius()
    radius2 = Enemy_var.getRadius()
    if dist <= radius1+radius2:
        return True
    else:
        return False

def main():
    # These 4 lines just to prepare the window of the game, no need to change them
    root = tkinter.Tk()
    root.title("Asteroids!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)

    #Here we prepre the new shapes of the game
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape(".gif")

    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    t.ht()

    def quitHandler():
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    
    # here we are using the class we defined above to create the spaceShip
    plr = Player(cv,0,0,0,0,0,0,0)
    
    # This is preparing a list that we will store all the enemies
    enemies = []

    for k in range(100):
        # preparing random variables 
        dx = random.random() * 10 - 5 #random speed in x (change in x)
        x = random.random() * (screenMaxX - screenMinX) + screenMinX # random starting x location

	enemies = Enemy (cv,dx,x)
        enemies.append(enemy)
       
    for enemy in enemies:
            if (intersect(plr,enemy)):
                print("Game Over")
                quitHandler()
            enemy.move()
    # here we a function that we will call it every 5 millisecond (THIS IS WHAT CODE KEEPS RUNNING WHILE THE GAME IS OPEN)
    # this we call it GAME LOOP
    # GAME LOOP (BEGIN)
    def play():
        # Tell all the elements of the game to move
        # Tell the ship to move
        plr.move()
        # go (loop) though each astroid in the astroids list and tell it to move as well check if it is toucing the ship
        # Set the timer to go off again in 5 milliseconds
        screen.ontimer(play,5)
    # GAME LOOP (ENDS)

    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play,5)
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the left arrow key is pushed in the keyboard
    screen.onkeypress(plr.go_left,"Left")
    # this means call the defined function in class spaceShip turrnRight for the ship everytime the right arrow key is pushed in the keyboard
    screen.onkeypress(plr.go_right,"Right")
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the up arrow key is pushed in the keyboard
    screen.onkeypress(plr.jump,"Up")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
    main()
