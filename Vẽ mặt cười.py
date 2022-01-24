import turtle
t = turtle.Turtle()
#define pen size
t.pensize(5) #cỡ viền
t.pencolor("Blue") #Màu viền

#for outer bigger circle
facesize = 200 ##Vẽ mặt
t.fillcolor("yellow")
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(facesize)
t.end_fill()

#for eyes
t.fillcolor("red") #màu nền mắt là màu đỏ
t.penup()
t.goto(-100,50)
t.pendown()

eye_size = 17.5 ##Khai báo biến lưu kích thước mắt
t.begin_fill()
t.circle(eye_size)
t.end_fill()
t.penup()

t.goto(100,50)
t.pendown()
t.begin_fill()
t.circle(eye_size)
t.end_fill()

#for nose
t.fillcolor("black")
t.penup()
t.goto(0,50)
t.pendown()
t.begin_fill()
t.circle(-70, steps = 3)
t.end_fill()

#for smile
t.fillcolor("pink")
t.penup()
t.goto(-100, -70)
t.pendown()
t.right(90)
t.begin_fill()
t.circle(100, 180)
t.left(90)
t.forward(200)
t.end_fill()
turtle.done()