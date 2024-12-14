import turtle
import random#to generate random number
import time

delay=0.1
sc=0#score card
hs=0#highest score
bodies=[]

#creating screen
s=turtle.Screen()
s.title("Snake Game")#to give the title to screen
s.bgcolor("light blue")#background of screen
s.setup(height=600,width=600)#size of screen

#creating head
head=turtle.Turtle()#head created
head.color("blue")#color of head
head.speed(0)#speed of head
head.shape("circle")#shape of head
head.penup()#it is used to when head changes the position it does not reark
head.goto(0,0)#position of snake
head.direction="stop"

#creating a food
food=turtle.Turtle()
food.shape("square")
food.color("red")
food.speed(0)
food.penup()
food.ht()#hide a turtle
food.goto(150,200)
food.st()#show a turtle

#creating a score board
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-290,270)
sb.write("Score:0 || Heighest Score:o")

#creating a function for moving in all direction
def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveStop():
    head.direction="stop"

#to move
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#event handeling
s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveRight,"Right")
s.onkey(moveLeft,"Left")
s.onkey(moveStop,"space")

#main loop
while True:
    s.update()#to updaate the screen
    #to check the colision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
        
    #check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)#append the new body s list

        sc=sc+100#increase the score
        delay=delay-0.001#increase the speed

        if sc>hs:
            hs=sc#update highest score
        sb.clear()
        sb.write("Score:{} || Highest Score:{}".format(sc,hs))

        #move snake body
    for i in range(len(bodies)-1,0,-1):
         x=bodies[i-1].xcor()
         y=bodies[i-1].ycor()
         bodies[i].goto(x,y)
    if len(bodies)>0:
         x=head.xcor()
         y=head.ycor()
         bodies[0].goto(x,y)
    move()

     #check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
             time.sleep(1)
             head.goto(0,0)
             head.direction="stop"
             #hide bodies
             for body in bodies:
                 body.ht()
             bodies.clear()
             sc=0
             delay=0.1
             sb.clear()
             sb.write("Score:{} || Highest Score:{}".format(sc,hs))
    time.sleep(delay)

s.mainloop()         
         
            
        

        


        
