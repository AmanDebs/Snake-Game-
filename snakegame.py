import turtle
import time
import random

delay = 0.1


#set up the screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #turns off screen updates


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#score
score = 0
high_score = 0

#Score turtle
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))
Segments = []
#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)              
#key Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Main game loop
while True:
    wn.update()

    #Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in Segments:
            segment.goto(1000,1000)
        
        #clear the segments list
        Segments.clear()

        #Reset the delay
        delay = 0.1

        #Update the Score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score), align = "center", font = ("Courier", 24, "normal"))


    #check for collosion with food
    if head.distance(food) < 20:
    #move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        Segments.append(new_segment)
        
        #Increase the speed
        delay -= 0.001
        #Increase Score
        score += 10
        if score >= high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score), align = "center", font = ("Courier", 24, "normal"))
    #move the end segment first in reverse order
    for index in range(len(Segments)-1,0,-1):
        x = Segments[index-1].xcor()
        y = Segments[index-1].ycor()
        Segments[index].goto(x,y)
    
    #Move segment 0 to where the head is
    if len(Segments) > 0:
        x = head.xcor()
        y = head.ycor()
        Segments[0].goto(x,y)
        
    move()

    #Check for head and segment collision
    for segment in Segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            
            #hide the segments
            for segment in Segments:
                segment.goto(1000,1000)
        
            #clear the segments list
            Segments.clear()

            #Reset the delay
            delay = 0.1
            #Update the Score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score), align = "center", font = ("Courier", 24, "normal"))
    time.sleep(delay)



wn.mainloop()